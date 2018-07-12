# MIT License

# Copyright (c) 2018 Renondedju

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

from .http                   import Route, Request
from .user                   import User
from .score                  import Score
from .replay                 import Replay
from .beatmap                import Beatmap
from .user_best              import UserBest
from .user_event             import UserEvent
from .user_recent            import UserRecent
from .score_collection       import ScoreCollection
from .beatmap_collection     import BeatmapCollection
from .user_best_collection   import UserBestCollection
from .user_recent_collection import UserRecentCollection

import asyncio

class OsuApi():

    def __init__(self, api_key : str):

        self._api_key = api_key
        self._session = None

    async def __get_data(self, url : str, unique = True, **args):

        route = Route(url, self._api_key)

        for key, value in args.items():
            route.add_param(key, value)

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
            the first one only will be returned, if you want multiple beatmaps,
            use OsuApi.get_beatmaps() instead

            Parameters :

                beatmapset_id     - specify a beatmapset_id to return metadata from.
                beatmap_id        - specify a beatmap_id to return metadata from.
                user              - specify a user_id or a username to return metadata from.
                type_str          - specify if 'user' is a user_id or a username.
                                      Use string for usernames or id for user_ids.
                                      Optional, default behaviour is automatic recognition
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

        return Beatmap(self, **data)

    async def get_beatmaps(self, limit = None, since = None, type_str = None,
        beatmapset_id = None, include_converted = None, user = None, mode = None):
        """
            Do note that requesting a beatmap collection is way faster than 
            requesting beatmap by beatmap (and requiers only only one api request)

            Parameters :

                limit             - amount of results. Optional, default and maximum are 500.
                since             - return all beatmaps ranked or loved since this date.
                                    Must be a MySQL date.
                beatmapset_id     - specify a beatmapset_id to return metadata from.
                user              - specify a user_id or a username to return metadata from.
                type_str          - specify if 'user' is a user_id or a username.
                                    Use string for usernames or id for user_ids.
                                    Optional, default behaviour is automatic recognition
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

        beatmaps = BeatmapCollection(self)
        for data in datas:
            beatmaps.add_beatmap(Beatmap(self, **data))

        return beatmaps

    async def get_user(self, user = None, mode = None, type_str = None, event_days = None):
        """
            Fetches a user data

            Parameters :

                user       - specify a user_id or a username to return metadata from (required).
                mode       - mode (0 = osu!, 1 = Taiko, 2 = CtB, 3 = osu!mania).
                             Optional, default value is 0.    
                type_str   - specify if u is a user_id or a username.
                             Use string for usernames or id for user_ids.
                             Optional, default behaviour is automatic recognition
                             (may be problematic for usernames made up of digits only).
                event_days - Max number of days between now and last event date. 
                             Range of 1-31. Optional, default value is 1.
        """

        data = await self.__get_data('get_user', u = user, m = mode, type = type_str,
            event_days = event_days)

        user_events = []
        for event in data.get('events', []):
            user_events.append(UserEvent(**event))

        return User(self, user_events, **data)

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
                             Optional, default behaviour is automatic recognition
                             (may be problematic for usernames made up of digits only).
                mode       - mode (0 = osu!, 1 = Taiko, 2 = CtB, 3 = osu!mania).
                             Optional, maps of all modes are returned by default.
        """

        data = await self.__get_data('get_scores', b = beatmap_id, limit = 1, u = user,
            m = mode, type = type_str)

        score = Score(self, **data)
        if mode != None:
            score.mode = mode

        return score

    async def get_scores(self, beatmap_id, user = None, mode = None, mods = None, type_str = None, limit = None):
        """
            Do note that requesting a score collection is way faster than 
            requesting score by score (and requiers only only one api request)

            Parameters :

                beatmap_id - specify a beatmap_id to return score information from (required).
                user       - specify a user_id or a username to return score information for.
                mode       - mode (0 = osu!, 1 = Taiko, 2 = CtB, 3 = osu!mania).
                             Optional, default value is 0.
                mods       - specify a mod or mod combination (See the bitwise enum)
                type_str   - specify if user is a user_id or a username.
                             Use string for usernames or id for user_ids.
                             Optional, default behaviour is automatic recognition
                             (may be problematic for usernames made up of digits only).
                limit      - amount of results from the top (range between 1 and 100 - defaults to 50).
        """

        datas = await self.__get_data('get_scores', False, b = beatmap_id, u = user,
            m = mode, mods = mods, type = type_str, limit = limit)

        scores = ScoreCollection(self)
        for data in datas:
            scores.add_score(Score(self, **data))

        return scores

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

        return UserBest(self, **data)

    async def get_user_bests(self, user, mode = None, type_str = None, limit = None):
        """
            Parameters :

                user       - sspecify a user_id or a username to return best scores from (required).
                mode       - mode (0 = osu!, 1 = Taiko, 2 = CtB, 3 = osu!mania).
                             Optional, default value is 0.
                type_str   - specify if user is a user_id or a username.
                             Use string for usernames or id for user_ids.
                             Optional, default behaviour is automatic recognition
                             (may be problematic for usernames made up of digits only).
                limit      - amount of results from the top (range between 1 and 100 - defaults to 50).
        """

        datas = await self.__get_data('get_user_best', False, u = user, m = mode,
            type = type_str, limit = limit)

        bests = UserBestCollection(self)
        for data in datas:
            bests.add_user_best(UserBest(self, **data))

        return bests

    async def get_user_recent(self, user, mode = None, type_str = None):
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
        data = await self.__get_data('get_user_recent', u = user, limit = 1, m = mode,
            type = type_str)

        return UserRecent(self, **data)

    async def get_user_recents(self, user, mode = None, type_str = None, limit = None):
        """
            Parameters :

                user       - sspecify a user_id or a username to return best scores from (required).
                mode       - mode (0 = osu!, 1 = Taiko, 2 = CtB, 3 = osu!mania).
                             Optional, default value is 0.
                type_str   - specify if user is a user_id or a username.
                             Use string for usernames or id for user_ids.
                             Optional, default behaviour is automatic recognition
                             (may be problematic for usernames made up of digits only).
                limit      - amount of results from the top (range between 1 and 100 - defaults to 50).
        """

        datas = await self.__get_data('get_user_recent', False, u = user, m = mode,
            type = type_str, limit = limit)

        recents = UserRecentCollection(self)
        for data in datas:
            recents.add_user_recent(UserRecent(self, **data))

        return recents

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
        
        data = await self.__get_data('get_replay', False, u = user, m = mode, b = beatmap_id)

        if len(data) is not 0:
            data['user']       = user
            data['mode']       = mode
            data['beatmap_id'] = beatmap_id

        return Replay(self, **data)