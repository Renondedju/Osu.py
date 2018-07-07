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

#Trello card : https://trello.com/c/Deol8NYI/10-beatmap-collection

from .http      import *
from .beatmap   import *
from .utilities import *

class BeatmapCollection():
    """ Beatmap collection class """

    def __init__(self):

        self._beatmaps = []

    @property
    def count(self):
        """ Returns the number of beatmaps of the collection """
        return len(self._beatmaps)

    @property
    def beatmaps(self):
        """ Returns the beatmaps of the collection """
        return self._beatmaps

    def add_beatmap(self, beatmap : Beatmap):
        """ Adds a beatmap to the collection """

        if beatmap is not None:
            self._beatmaps.append(beatmap)

        return

    def remove_beatmap(self, beatmap : Beatmap):
        """ Removes a beatmap from the collection """

        if beatmap is not None:
            self._beatmaps.pop(beatmap, None)

        return

    async def fetch(self, key, session = None, limit = None, since = None, type_str = None,
        beatmapset_id = None, include_converted = None, user = None, mode = None):
        """
            Do note that requesting a beatmap collection is way faster than 
            requesting beatmap by beatmap (and requiers only only one api request)

            Parameters :

                session           - aiohttp session
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

        route = Route('get_beatmaps', key)

        route.param('limit', limit)
        route.param('since', since)
        route.param('type' , type_str)
        route.param('s'    , beatmapset_id)
        route.param('a'    , include_converted)
        route.param('u'    , user)
        route.param('m'    , mode)

        datas = []
        if session is None:
            datas = await route.fetch()
        else:
            datas = await route.fetch_with_session(session)

        for data in datas:
            beatmap = Beatmap()
            beatmap.is_empty = Utilities.apply_data(beatmap, data)

            self._beatmaps.append(beatmap)

        return