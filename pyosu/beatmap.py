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

#Trello card : https://trello.com/c/iWdaEubw/4-beatmap-class

from .http                   import *
from .language               import *
from .game_modes             import *
from .beatmap_genre          import *
from .beatmap_approved_state import *


class Beatmap():
    """ Beatmap class """

    def __init__(self):

        #Api data
        self.approved         = BeatmapApprovedState.Pending
        self.approved_date    = ""  # date ranked, UTC+8 for now
        self.last_update      = ""  # last update date, timezone same as above. May be after approved_date if map was unranked and reranked.
        self.artist           = ""
        self.beatmap_id       = 0   # beatmap_id is per difficulty
        self.beatmapset_id    = 0   # beatmapset_id groups difficulties into a set
        self.bpm              = 0.0
        self.creator          = ""
        self.difficultyrating = 0.0 # The amount of stars the map would have ingame and on the website
        self.diff_size        = 0.0 # Circle size value  (CS)
        self.diff_overall     = 0.0 # Overall difficulty (OD)
        self.diff_approach    = 0.0 # Approach Rate      (AR)
        self.diff_drain       = 0.0 # Healthdrain        (HP)
        self.hit_length       = 0.0 # seconds from first note to last note not including breaks
        self.source           = ""
        self.genre_id         = BeatmapGenre.Any
        self.language_id      = Language.Any
        self.title            = ""  # song name
        self.total_length     = 0.0 # seconds from first note to last note including breaks
        self.version          = ""  # difficulty name
        self.file_md5         = ""  # md5 hash of the beatmap
        self.mode             = GameMode.Osu # game mode,
        self.tags             = ""  # Beatmap tags separated by spaces.
        self.favourite_count  = 0   # Number of times the beatmap was favourited.
        self.playcount        = 0   # Number of times the beatmap was played
        self.passcount        = 0   # Number of times the beatmap was passed, completed (the user didn't fail or retry)
        self.max_combo        = 0   # The maximum combo a user can reach playing this beatmap.

        self.is_empty         = True

    def apply_data(self, data : dict):
        """ Applies datas from a dict to the attributes of the beatmap """

        self.is_empty = len(data) is 0

        for key, value in data.items():
            attribute = getattr(self, key)
            if attribute is not None and value is not None:
                setattr(self, key, (type(attribute))(value))
        
        return

    async def fetch(self, key, session = None, beatmapset_id = None, beatmap_id = None,
            user = None, type_str = None, mode = None, include_converted = None,
            hash_str = None):

        """
            If any of the parameters used returns more than one beatmap,
            the first one only will be used

            Parameters :

                'session' - aiohttp session

                'beatmapset_id' - specify a beatmapset_id to return metadata from.

                'beatmap_id' - specify a beatmap_id to return metadata from.

                'user' - specify a user_id or a username to return metadata from.

                'type_str' - specify if 'user' is a user_id or a username. Use string for usernames or id 
                    for user_ids. Optional, default behaviour is automatic recognition
                    (may be problematic for usernames made up of digits only).

                'mode' - mode (0 = osu!, 1 = Taiko, 2 = CtB, 3 = osu!mania).
                    Optional, maps of all modes are returned by default.

                'include_converted' - specify whether converted beatmaps are included (0 = not included, 1 = included).
                    Only has an effect if 'm' is chosen and not 0.
                    Converted maps show their converted difficulty rating. Optional, default is 0.

                'hash_str' - the beatmap hash. It can be used, for instance,
                    if you're trying to get what beatmap has a replay played in,
                    as .osr replays only provide beatmap hashes
                    (example of hash: a5b99395a42bd55bc5eb1d2411cbdf8b).
                    Optional, by default all beatmaps are returned independently from the hash.
        """

        route = Route('get_beatmaps', key, limit=1)

        route.param('s'   , beatmapset_id)
        route.param('b'   , beatmap_id)
        route.param('u'   , user)
        route.param('m'   , mode)
        route.param('a'   , include_converted)
        route.param('h'   , hash_str)
        route.param('type', type_str)

        data = {}
        if session is None:
            data = await route.fetch()
        else:
            data = await route.fetch_with_session(session)

        if len(data) is not 0:
            data = data[0]
        else:
            return

        # Assigning the fetched values to the variables
        self.apply_data(data)