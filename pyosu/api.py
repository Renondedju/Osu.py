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
from .beatmap                import Beatmap
from .user_best              import UserBest
from .user_event             import UserEvent
from .user_recent            import UserRecent
from .score_collection       import ScoreCollection
from .beatmap_collection     import BeatmapCollection
from .user_best_collection   import UserBestCollection

import asyncio
import aiohttp

class OsuApi():

    def __init__(self, api_key : str):

        self._api_key = api_key
        self._session = None

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

        route = Route('get_beatmaps', self._api_key, limit=1)

        route.add_param('s'   , beatmapset_id)
        route.add_param('b'   , beatmap_id)
        route.add_param('u'   , user)
        route.add_param('m'   , mode)
        route.add_param('a'   , include_converted)
        route.add_param('h'   , hash_str)
        route.add_param('type', type_str)

        request = Request(route)

        await request.fetch(self._session)

        data = request.data
        if len(data) is not 0:
            data = data[0]
        else:
            data = {}

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

        route = Route('get_beatmaps', self._api_key)

        route.add_param('limit', limit)
        route.add_param('since', since)
        route.add_param('type' , type_str)
        route.add_param('s'    , beatmapset_id)
        route.add_param('a'    , include_converted)
        route.add_param('u'    , user)
        route.add_param('m'    , mode)

        request = Request(route)
        await request.fetch(self._session)

        beatmaps = BeatmapCollection(self)
        for data in request.data:
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

        route = Route('get_user', self._api_key)

        route.add_param('u', user)
        route.add_param('m', mode)
        route.add_param('type', type_str)
        route.add_param('event_days', event_days)

        request = Request(route)

        await request.fetch(self._session)

        data = request.data
        if len(data) is not 0:
            data = data[0]
        else:
            data = {}

        user = User(self, **data)

        #Adding events
        for event in data['events']:
            user_event = UserEvent(**event)
            user.events.append(user_event)

        return user

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

        route = Route('get_scores', self._api_key, b=beatmap_id, limit=1)

        route.add_param('u', user)
        route.add_param('m', mode)
        route.add_param('type', type_str)

        request = Request(route)
        await request.fetch(self._session)

        data = request.data
        if len(data) is not 0:
            data = data[0]
        else:
            data = {}

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

        route = Route('get_scores', self._api_key, b=beatmap_id)

        route.add_param('u', user)
        route.add_param('m', mode)
        route.add_param('mods', mods)
        route.add_param('type', type_str)
        route.add_param('limit', limit)

        request = Request(route)
        await request.fetch(self._session)

        scores = ScoreCollection(self)
        for data in request.data:
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
        route = Route('get_user_best', self._api_key, u=user, limit=1)

        route.add_param('m', mode)
        route.add_param('type', type_str)
        
        request = Request(route)
        await request.fetch(self._session)

        data = request.data
        if len(data) is not 0:
            data = data[0]
        else:
            data = {}

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

        route = Route('get_user_best', self._api_key, u=user)

        route.add_param('m', mode)
        route.add_param('type', type_str)
        route.add_param('limit', limit)

        request = Request(route)
        await request.fetch(self._session)

        bests = UserBestCollection(self)
        for data in request.data:
            bests.add_user_best(UserBest(self, **data))

        return bests