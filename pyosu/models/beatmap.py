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

import datetime

from pyosu.types       import BeatmapGenre, BeatmapApprovedState, GameMode, Language
from pyosu.models.base import BaseModel

class Beatmap(BaseModel):
    """ Beatmap model """

    def __init__(self, *, api : 'OsuApi' = None, **data):

        super().__init__(api)

        #Api data
        self.bpm              = float(data.get('bpm'             , 0.0))
        self.diff_size        = float(data.get('diff_size'       , 0.0))            # Circle size value  (CS)
        self.diff_drain       = float(data.get('diff_drain'      , 0.0))            # Healthdrain        (HP)
        self.hit_length       = float(data.get('hit_length'      , 0.0))            # seconds from first note to last note not including breaks
        self.diff_overall     = float(data.get('diff_overall'    , 0.0))            # Overall difficulty (OD)
        self.total_length     = float(data.get('total_length'    , 0.0))            # seconds from first note to last note including breaks
        self.diff_approach    = float(data.get('diff_approach'   , 0.0))            # Approach Rate      (AR)
        self.difficultyrating = float(data.get('difficultyrating', 0.0))            # The amount of stars the map would have ingame and on the website
        self.mode             =   int(data.get('mode'            , GameMode.Osu))   # game mode,
        self.approved         =   int(data.get('approved'        , BeatmapApprovedState.Pending))
        self.genre_id         =   int(data.get('genre_id'        , BeatmapGenre.Any))
        self.playcount        =   int(data.get('playcount'       , 0))              # Number of times the beatmap was played
        self.passcount        =   int(data.get('passcount'       , 0))              # Number of times the beatmap was passed, completed (the user didn't fail or retry)
        self.max_combo        =   int(data.get('max_combo'       , 0))              # The maximum combo a user can reach playing this beatmap.
        self.beatmap_id       =   int(data.get('beatmap_id'      , 0))              # beatmap_id is per difficulty
        self.language_id      =   int(data.get('language_id'     , Language.Any))
        self.beatmapset_id    =   int(data.get('beatmapset_id'   , 0))              # beatmapset_id groups difficulties into a set
        self.favourite_count  =   int(data.get('favourite_count' , 0))              # Number of times the beatmap was favourited.
        self.tags             =       data.get('tags'            , "")              # Beatmap tags separated by spaces.
        self.title            =       data.get('title'           , "")              # song name
        self.source           =       data.get('source'          , "")
        self.artist           =       data.get('artist'          , "")
        self.version          =       data.get('version'         , "")              # difficulty name
        self.creator          =       data.get('creator'         , "")
        self.file_md5         =       data.get('file_md5'        , "")              # md5 hash of the beatmap
        self.approved_date    = datetime.datetime.strptime(data.get('approved_date' , "1970-01-01 00:00:00") , "%Y-%m-%d %H:%M:%S") # date ranked, UTC+8 for now
        self.last_update      = datetime.datetime.strptime(data.get('last_update'   , "1970-01-01 00:00:00") , "%Y-%m-%d %H:%M:%S") # last update date, timezone same as above. May be after approved_date if map was unranked and reranked.

    async def get_beatmapset(self):
        """ Returns a beatmap collection with every beatmap of the beatmapset """

        return await self.api.get_beatmaps(beatmapset_id=self.beatmapset_id)
