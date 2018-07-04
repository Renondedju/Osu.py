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

#Trello card : https:#trello.com/c/iWdaEubw/4-beatmap-class

from .game_modes     import *
from .game_modifiers import *

from .http import *

class Beatmap():
    """ Beatmap class """

    def __init__(self):

        #Api data
        self.approved         = "" # 4 = loved, 3 = qualified, 2 = approved, 1 = ranked, 0 = pending, -1 = WIP, -2 = graveyard
        self.approved_date    = "" # date ranked, UTC+8 for now
        self.last_update      = "" # last update date, timezone same as above. May be after approved_date if map was unranked and reranked.
        self.artist           = ""
        self.beatmap_id       = "" # beatmap_id is per difficulty
        self.beatmapset_id    = "" # beatmapset_id groups difficulties into a set
        self.bpm              = ""
        self.creator          = ""
        self.difficultyrating = "" # The amount of stars the map would have ingame and on the website
        self.diff_size        = "" # Circle size value (CS)
        self.diff_overall     = "" # Overall difficulty (OD)
        self.diff_approach    = "" # Approach Rate (AR)
        self.diff_drain       = "" # Healthdrain (HP)
        self.hit_length       = "" # seconds from first note to last note not including breaks
        self.source           = ""
        self.genre_id         = "" # 0 = any, 1 = unspecified, 2 = video game, 3 = anime, 4 = rock, 5 = pop, 6 = other, 7 = novelty, 9 = hip hop, 10 = electronic (note that there's no 8)
        self.language_id      = "" # 0 = any, 1 = other, 2 = english, 3 = japanese, 4 = chinese, 5 = instrumental, 6 = korean, 7 = french, 8 = german, 9 = swedish, 10 = spanish, 11 = italian
        self.title            = "" # song name
        self.total_length     = "" # seconds from first note to last note including breaks
        self.version          = "" # difficulty name
        self.file_md5         = "" # md5 hash of the beatmap
        self.mode             = "" # game mode,
        self.tags             = "" # Beatmap tags separated by spaces.
        self.favourite_count  = "" # Number of times the beatmap was favourited. (americans: notice the ou!)
        self.playcount        = "" # Number of times the beatmap was played
        self.passcount        = "" # Number of times the beatmap was passed, completed (the user didn't fail or retry)
        self.max_combo        = "" # The maximum combo a user can reach playing this beatmap.

        #Additionals parameters
        self._playstyle = 0
        self._pp        = {GameModifier(GameModifier.none) : {100 : 0.0}}

    