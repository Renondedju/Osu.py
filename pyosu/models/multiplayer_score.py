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

from pyosu.types       import MultiplayerTeam
from pyosu.models.base import BaseModel


class MultiplayerScore(BaseModel):
    """ Multiplayer score model """

    def __init__(self, *, api: 'OsuApi' = None, **data):

        super().__init__(api)

        self.slot       =  int(data.get('slot'     , 0))     # 0 based index of player's slot
        self.team       =  int(data.get('team'     , MultiplayerTeam.none)) # Player's team
        self.rank       =  int(data.get('rank'     , 0))     # not used (Api side)
        self.score      =  int(data.get('score'    , 0))
        self.user_id    =  int(data.get('user_id'  , 0))
        self.count50    =  int(data.get('count50'  , 0))
        self.count100   =  int(data.get('count100' , 0))
        self.count300   =  int(data.get('count300' , 0))
        self.maxcombo   =  int(data.get('maxcombo' , 0))
        self.countmiss  =  int(data.get('countmiss', 0))
        self.countgeki  =  int(data.get('countgeki', 0))
        self.countkatu  =  int(data.get('countkatu', 0))
        self.perfect    = bool(data.get('perfect'  , False)) # full combo
        self.passed     = bool(data.get('pass'     , False)) # does the player passed the map at the end ?
