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

from .team_type      import TeamType
from .game_modes     import GameMode
from .base_model     import BaseModel
from .scoring_type   import ScoringType
from .game_modifiers import GameModifier

class MultiplayerGame(BaseModel):
    """ Multiplayer match model """

    def __init__(self, api: 'OsuApi', game_scores : list, **data):

        super().__init__(api, **data)

        self.game_id      = data.get('game_id'     , 0)
        self.start_time   = data.get('start_time'  , "")
        self.end_time     = data.get('end_time'    , "")
        self.beatmap_id   = data.get('beatmap_id'  , 0)
        self.play_mode    = data.get('play_mode'   , GameMode.Osu)          # Gamemode played
        self.match_type   = data.get('match_type'  , 0)                     # couldn't find
        self.scoring_type = data.get('scoring_type', ScoringType.score)     # winning condition see ScoringType
        self.team_type    = data.get('team_type'   , TeamType.head_to_head) # team type : see TeamType
        self.mods         = data.get('mods'        , GameModifier.none)     # global mods, see GameModifiers

        self.scores = game_scores