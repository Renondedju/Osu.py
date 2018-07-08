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

from .language               import *
from .game_modes             import *
from .beatmap_genre          import *
from .beatmap_approved_state import *

class Beatmap():
    """ Beatmap class """

    def __init__(self, api):

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
        self.api              = api