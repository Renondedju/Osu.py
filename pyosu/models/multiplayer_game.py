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

from pyosu.types       import TeamType, GameMode, ScoringType, GameModifier
from pyosu.models.base import BaseModel

class MultiplayerGame(BaseModel):
    """ Multiplayer game model """

    def __init__(self, *, api: 'OsuApi' = None, game_scores : list, **data):

        super().__init__(api)

        
        self.start_time   = datetime.datetime.strptime(data.get('start_time', "1970-01-01 00:00:00") , "%Y-%m-%d %H:%M:%S")
        self.end_time     = datetime.datetime.strptime(data.get('end_time'  , "1970-01-01 00:00:00") , "%Y-%m-%d %H:%M:%S")

        self.mods         = int(data.get('mods'        , GameModifier.none))     # global mods, see GameModifiers
        self.game_id      = int(data.get('game_id'     , 0))
        self.play_mode    = int(data.get('play_mode'   , GameMode.Osu))          # Gamemode played
        self.team_type    = int(data.get('team_type'   , TeamType.head_to_head)) # team type : see TeamType
        self.beatmap_id   = int(data.get('beatmap_id'  , 0))
        self.match_type   = int(data.get('match_type'  , 0))                     # couldn't find
        self.scoring_type = int(data.get('scoring_type', ScoringType.score))     # winning condition see ScoringType

        self.scores = game_scores
