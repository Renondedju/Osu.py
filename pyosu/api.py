# MIT License

# Copyright (c) 2018-2019 Renondedju

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import asyncio

from pyosu.http   import Route, Request
from pyosu.models import (
    User,
    Score,
    Replay,
    Beatmap,
    UserBest,
    UserEvent,
    UserRecent,
    BeatmapFile,
    ScoreCollection,
    MultiplayerGame,
    MultiplayerScore,
    MultiplayerMatch,
    BeatmapCollection,
    UserBestCollection,
    UserRecentCollection,
)
from pyosu.exceptions import ReplayUnavailable


class OsuApi():

    def __init__(self, api_key : str):

        self._api_key = api_key
        self._session = None

    async def __get_data(self, url : str, unique = True, **args):

        route = Route(url, self._api_key, **args)

        request = Request(route)
        await request.fetch(self._session)

        data = request.data

        if unique:
            if len(data) is not 0:
                data = data[0]
            else:
                data = {}

        return data

    async def get_beatmap(self, beatmapset_id = None, beatmap_id = None, user = None,
        type_str = None, mode = None, include_converted = None, hash_str = None):
        """
            If any of the parameters used returns more than one beatmap,
            the first one only will be returned.
            If you want multiple beatmaps, use OsuApi.get_beatmaps() instead

            Parameters :

                beatmapset_id     - specify a beatmapset_id to return metadata from.
                beatmap_id        - specify a beatmap_id to return metadata from.
                user              - specify a user_id or a username to return metadata from.
                type_str          - specify if 'user' is a user_id or a username.
                                      Use string for usernames or id for user_ids.
                                      Optional, default behavior is automatic recognition
                                      (may be problematic for usernames made up of digits only).
                mode              - mode (0 = osu!, 1 = Taiko, 2 = CtB, 3 = osu!mania).
                                      Optional, maps of all modes are returned by default.
                include_converted - specify whether converted beatmaps are included
                                      (0 = not included, 1 = included).
                                      Only has an effect if 'mode' is chosen and not 0.
                                      Converted maps show their converted difficulty rating.
                                      Optional, default is 0.
                hash_str          - the beatmap hash. It can be used, for instance,
                                      if you're trying to get what beatmap has a replay played in,
                                      as .osr replays only provide beatmap hashes
                                      (example of hash: a5b99395a42bd55bc5eb1d2411cbdf8b).
                                      Optional, by default all beatmaps are returned independently from the hash.
        """

        data = await self.__get_data('get_beatmaps', limit = 1, s = beatmapset_id,
            b = beatmap_id, u = user, m = mode, a = include_converted, h = hash_str,
            type = type_str)

        if len(data) == 0:
            return None

        return Beatmap(**data, api=self)

    async def get_beatmaps(self, limit = None, since = None, type_str = None,
        beatmapset_id = None, include_converted = None, user = None, mode = None):
        """
            Do note that requesting a beatmap collection is way faster than 
            requesting beatmap by beatmap (and requires only only one api request)

            Parameters :

                limit             - amount of results. Optional, default and maximum are 500.
                since             - return all beatmaps ranked or loved since this date.
                                    Must be a MySQL date.
                beatmapset_id     - specify a beatmapset_id to return metadata from.
                user              - specify a user_id or a username to return metadata from.
                type_str          - specify if 'user' is a user_id or a username.
                                    Use string for usernames or id for user_ids.
                                    Optional, default behavior is automatic recognition
                                    (may be problematic for usernames made up of digits only).
                mode              - mode (0 = osu!, 1 = Taiko, 2 = CtB, 3 = osu!mania).
                                    Optional, maps of all modes are returned by default.
                include_converted - specify whether converted beatmaps are included
                                    (0 = not included, 1 = included).
                                    Only has an effect if 'mode' is chosen and not 0.
                                    Converted maps show their converted difficulty rating.
                                    Optional, default is 0.
        """

        datas = await self.__get_data('get_beatmaps', False, limit = limit, since = since,
            type = type_str, s = beatmapset_id, a = include_converted, u = user, m = mode)

        if len(datas) == 0:
            return None
        return BeatmapCollection(
            (Beatmap(**data, api=self) for data in datas),
            api=self,
        )

    async def get_user(self, user, mode = None, type_str = None, event_days = None):
        """
            Fetches a user data

            Parameters :

                user       - specify a user_id or a username to return metadata from (required).
                mode       - mode (0 = osu!, 1 = Taiko, 2 = CtB, 3 = osu!mania).
                             Optional, default value is 0.    
                type_str   - specify if u is a user_id or a username.
                             Use string for usernames or id for user_ids.
                             Optional, default behavior is automatic recognition
                             (may be problematic for usernames made up of digits only).
                event_days - Max number of days between now and last event date. 
                             Range of 1-31. Optional, default value is 1.
        """

        data = await self.__get_data('get_user', u = user, m = mode, type = type_str,
            event_days = event_days)

        if len(data) == 0:
            return None

        return User(user_events=[UserEvent(**event) for event in data.get('events', [])], **data, api=self)

    async def get_score(self, beatmap_id, user = None, mode = None, type_str = None):
        """
            If any of the parameters used returns more than one score,
            the first one only will be used. If you want multiple scores use
            OsuApi.get_scores() instead

            Parameters :

                beatmap_id - specify a beatmap_id to return metadata from. (required)
                user       - specify a user_id or a username to return metadata from.
                type_str   - specify if 'user' is a user_id or a username.
                             Use string for usernames or id for user_ids.
                             Optional, default behavior is automatic recognition
                             (may be problematic for usernames made up of digits only).
                mode       - mode (0 = osu!, 1 = Taiko, 2 = CtB, 3 = osu!mania).
                             Optional, maps of all modes are returned by default.
        """

        data = await self.__get_data('get_scores', b = beatmap_id, limit = 1, u = user,
            m = mode, type = type_str)

        if len(data) == 0:
            return None

        score = Score(**data, api=self)
        if mode != None:
            score.mode = mode

        return score

    async def get_scores(self, beatmap_id, user = None, mode = None, mods = None, type_str = None, limit = None):
        """
            Do note that requesting a score collection is way faster than 
            requesting score by score (and requires only only one api request)

            Parameters :

                beatmap_id - specify a beatmap_id to return score information from (required).
                user       - specify a user_id or a username to return score information for.
                mode       - mode (0 = osu!, 1 = Taiko, 2 = CtB, 3 = osu!mania).
                             Optional, default value is 0.
                mods       - specify a mod or mod combination (See the bitwise enum)
                type_str   - specify if user is a user_id or a username.
                             Use string for usernames or id for user_ids.
                             Optional, default behavior is automatic recognition
                             (may be problematic for usernames made up of digits only).
                limit      - amount of results from the top (range between 1 and 100 - defaults to 50).
        """

        datas = await self.__get_data('get_scores', False, b = beatmap_id, u = user,
            m = mode, mods = mods, type = type_str, limit = limit)

        if len(datas) == 0:
            return None
        return ScoreCollection(
            [Score(**data, api=self) for data in datas],
            api=self
        )

    async def get_user_best(self, user, mode = None, type_str = None):
        """
            Returns the top play of a user. If you want more than one user best
            use OsuApi.get_user_bests() instead.

            Parameters :

                user     - specify a user_id or a username to return best scores from (required).
                mode     - mode (0 = osu!, 1 = Taiko, 2 = CtB, 3 = osu!mania).
                           Optional, default value is 0.
                type_str - specify if user is a user_id or a username.
                           Use 'string' for usernames or 'id' for user_ids.
                           Optional, default behavior is automatic recognition 
                           may be problematic for usernames made up of digits only).
        """
        data = await self.__get_data('get_user_best', u = user, limit = 1, m = mode,
            type = type_str)

        if len(data) == 0:
            return None

        return UserBest(**data, api=self)

    async def get_user_bests(self, user, mode = None, type_str = None, limit = None):
        """
            Parameters :

                user       - specify a user_id or a username to return best scores from (required).
                mode       - mode (0 = osu!, 1 = Taiko, 2 = CtB, 3 = osu!mania).
                             Optional, default value is 0.
                type_str   - specify if user is a user_id or a username.
                             Use string for usernames or id for user_ids.
                             Optional, default behavior is automatic recognition
                             (may be problematic for usernames made up of digits only).
                limit      - amount of results from the top (range between 1 and 100 - defaults to 50).
        """

        datas = await self.__get_data('get_user_best', False, u = user, m = mode,
            type = type_str, limit = limit)

        if len(datas) == 0:
            return None

        return UserBestCollection(
            (UserBest(**data, api=self) for data in datas),
            api=self,
        )

    async def get_user_recent(self, user, mode = None, type_str = None):
        """
            If you want more than one user recent use OsuApi.get_user_recent() instead.

            Parameters :

                user     - specify a user_id or a username to return best scores from (required).
                mode     - mode (0 = osu!, 1 = Taiko, 2 = CtB, 3 = osu!mania).
                           Optional, default value is 0.
                type_str - specify if user is a user_id or a username.
                           Use 'string' for usernames or 'id' for user_ids.
                           Optional, default behavior is automatic recognition 
                           may be problematic for usernames made up of digits only).
        """
        data = await self.__get_data('get_user_recent', u = user, limit = 1, m = mode,
            type = type_str)

        if len(data) == 0:
            return None
        return UserRecent(**data, api=self)

    async def get_user_recents(self, user, mode = None, type_str = None, limit = None):
        """
            Parameters :

                user       - specify a user_id or a username to return best scores from (required).
                mode       - mode (0 = osu!, 1 = Taiko, 2 = CtB, 3 = osu!mania).
                             Optional, default value is 0.
                type_str   - specify if user is a user_id or a username.
                             Use string for usernames or id for user_ids.
                             Optional, default behavior is automatic recognition
                             (may be problematic for usernames made up of digits only).
                limit      - amount of results from the top (range between 1 and 100 - defaults to 50).
        """

        datas = await self.__get_data('get_user_recent', False, u = user, m = mode,
            type = type_str, limit = limit)

        return UserRecentCollection(
           (UserRecent(**data, api=self) for data in datas),
            api=self,
        )

    async def get_replay(self, mode, beatmap_id, user):
        """
            Official doc : https://github.com/ppy/osu-api/wiki#get-replay-data

            Ref : https://github.com/ppy/osu-api/wiki#rate-limiting  
            As this is quite a load-heavy request, it has special rules about rate limiting.
            You are only allowed to do 10 requests per minute.
            Also, please note that this request is ___not___ intended for batch retrievals.

            Parameters:

                mode        - the mode the score was played in (required)
                beatmap_id  - the beatmap ID (not beatmap set ID!)
                              in which the replay was played (required).
                user        - the user that has played the beatmap (required).
        """

        try:
            data = await self.__get_data('get_replay', False, u = user, m = mode,
                b = beatmap_id)
        except ReplayUnavailable:
            return None

        if len(data) is not 0:
            data['user']       = user
            data['mode']       = mode
            data['beatmap_id'] = beatmap_id
        else:
            return None

        return Replay(**data, api=None)

    async def get_match(self, match_id):
        """
            Retrieve information about multiplayer match.

            Parameters :

                match_id - match id to get information from (required).
        """

        data = await self.__get_data('get_match', False, mp = match_id)

        if len(data) == 0:
            return None

        if type(data) == dict and data.get('match') == 0:
            return None
        else:
            data = data[0]

        games = []
        for game in data.get('games', []):

            scores = []
            for score in game.get('scores', []):
                scores.append(MultiplayerScore(self, **score))

            games.append(MultiplayerGame(self, scores, **game))

        return MultiplayerMatch(self, games, **data.get('match', {}))

    async def get_beatmap_file(self, beatmap_id):
        """
            This model is way heavier than a classic Beatmap object (3Kb to 1Mb) since
            it contains the beatmap file. If you don't really need it, don't use it !

            Parameters :

                beatmap_id - the beatmap ID (not beatmap set ID!) (required).
        """

        route   = Route(base = 'https://osu.ppy.sh/osu/', path = str(beatmap_id))
        request = Request(route, 1, False)

        await request.fetch()

        if request.data == '':
            return None

        return BeatmapFile(**{"content": request.data}, api=self)
