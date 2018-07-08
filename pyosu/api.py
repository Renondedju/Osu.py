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

from .http      import *
from .beatmap   import *
from .utilities import *

import asyncio
import aiohttp

class Api():

    def __init__(self, api_key : str):

        self._api_key = api_key
        self._session = None

    async def get_beatmap(self, beatmapset_id = None, beatmap_id = None, user = None,
        type_str = None, mode = None, include_converted = None, hash_str = None):
        """
            If any of the parameters used returns more than one beatmap,
            the first one only will be returned, if you want multiple beatmaps,
            use Api.get_beatmaps() instead

            Parameters :

                'beatmapset_id'     - specify a beatmapset_id to return metadata from.
                'beatmap_id'        - specify a beatmap_id to return metadata from.
                'user'              - specify a user_id or a username to return metadata from.
                'type_str'          - specify if 'user' is a user_id or a username.
                                      Use string for usernames or id for user_ids.
                                      Optional, default behaviour is automatic recognition
                                      (may be problematic for usernames made up of digits only).
                'mode'              - mode (0 = osu!, 1 = Taiko, 2 = CtB, 3 = osu!mania).
                                      Optional, maps of all modes are returned by default.
                'include_converted' - specify whether converted beatmaps are included
                                      (0 = not included, 1 = included).
                                      Only has an effect if 'mode' is chosen and not 0.
                                      Converted maps show their converted difficulty rating.
                                      Optional, default is 0.
                'hash_str'          - the beatmap hash. It can be used, for instance,
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

        beatmap = Beatmap()
        request = Request(route)

        if self._session is None:
            await request.fetch()
        else:
            await request.fetch_with_session(self._session)

        data = request.data
        if len(data) is not 0:
            data = data[0]
        else:
            beatmap.is_empty = True
            return

        # Assigning the fetched values to the variables
        beatmap.is_empty = Utilities.apply_data(beatmap, data)

        return beatmap