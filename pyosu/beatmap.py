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

from .language               import Language
from .game_modes             import GameMode
from .base_model             import BaseModel
from .beatmap_genre          import BeatmapGenre
from .beatmap_approved_state import BeatmapApprovedState

class Beatmap(BaseModel):
    """ Beatmap model """

    def __init__(self, api : 'OsuApi', **data):

        super().__init__(api, **data)

        #Api data
        self.approved         = data.get('approved'        , BeatmapApprovedState.Pending)
        self.approved_date    = data.get('approved_date'   , "")  # date ranked, UTC+8 for now
        self.last_update      = data.get('last_update'     , "")  # last update date, timezone same as above. May be after approved_date if map was unranked and reranked.
        self.artist           = data.get('artist'          , "")
        self.beatmap_id       = data.get('beatmap_id'      , 0)   # beatmap_id is per difficulty
        self.beatmapset_id    = data.get('beatmapset_id'   , 0)   # beatmapset_id groups difficulties into a set
        self.bpm              = data.get('bpm'             , 0.0)
        self.creator          = data.get('creator'         , "")
        self.difficultyrating = data.get('difficultyrating', 0.0) # The amount of stars the map would have ingame and on the website
        self.diff_size        = data.get('diff_size'       , 0.0) # Circle size value  (CS)
        self.diff_overall     = data.get('diff_overall'    , 0.0) # Overall difficulty (OD)
        self.diff_approach    = data.get('diff_approach'   , 0.0) # Approach Rate      (AR)
        self.diff_drain       = data.get('diff_drain'      , 0.0) # Healthdrain        (HP)
        self.hit_length       = data.get('hit_length'      , 0.0) # seconds from first note to last note not including breaks
        self.source           = data.get('source'          , "")
        self.genre_id         = data.get('genre_id'        , BeatmapGenre.Any)
        self.language_id      = data.get('language_id'     , Language.Any)
        self.title            = data.get('title'           , "")  # song name
        self.total_length     = data.get('total_length'    , 0.0) # seconds from first note to last note including breaks
        self.version          = data.get('version'         , "")  # difficulty name
        self.file_md5         = data.get('file_md5'        , "")  # md5 hash of the beatmap
        self.mode             = data.get('mode'            , GameMode.Osu) # game mode,
        self.tags             = data.get('tags'            , "")  # Beatmap tags separated by spaces.
        self.favourite_count  = data.get('favourite_count' , 0)   # Number of times the beatmap was favourited.
        self.playcount        = data.get('playcount'       , 0)   # Number of times the beatmap was played
        self.passcount        = data.get('passcount'       , 0)   # Number of times the beatmap was passed, completed (the user didn't fail or retry)
        self.max_combo        = data.get('max_combo'       , 0)   # The maximum combo a user can reach playing this beatmap.

    async def get_beatmapset(self):
        """ Returns a beatmap collection with every beatmap of the beatmapset """

        return await self.api.get_beatmaps(beatmapset_id=self.beatmapset_id)
