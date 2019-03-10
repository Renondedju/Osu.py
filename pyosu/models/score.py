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

from pyosu.types       import ReplayAvailability
from pyosu.models.base import BaseModel

class Score(BaseModel):

    def __init__(self, *, api : 'OsuApi' = None, **data):

        super().__init__(api)

        self.rank             =       data.get('rank'             , "")
        self.username         =       data.get('username'         , "")
        self.mode             =   int(data.get('mode'             , 0))
        self.user_id          =   int(data.get('user_id'          , 0))
        self.count50          =   int(data.get('count50'          , 0))
        self.count100         =   int(data.get('count100'         , 0))
        self.count300         =   int(data.get('count300'         , 0))
        self.score_id         =   int(data.get('score_id'         , 0))
        self.maxcombo         =   int(data.get('maxcombo'         , 0))
        self.countmiss        =   int(data.get('countmiss'        , 0))
        self.countkatu        =   int(data.get('countkatu'        , 0))
        self.countgeki        =   int(data.get('countgeki'        , 0))
        self.enabled_mods     =   int(data.get('enabled_mods'     , 0))     # Bitwise flag representation of mods used. see reference (GameModifier class)
        self.replay_available =   int(data.get('replay_available' , ReplayAvailability.Unavailable))
        self.perfect          =  bool(data.get('perfect'          , False)) # True = maximum combo of map reached, False otherwise
        self.pp               = float(data.get('pp'               , 0.0))   # Float value , 4 decimals
        self.score            = float(data.get('score'            , 0.0))
        self.date             = datetime.datetime.strptime(data.get('date', "1970-01-01 00:00:00"), "%Y-%m-%d %H:%M:%S")

        self._user = None

    async def get_user_data(self, mode = None):
        """ Returns the data of the author of the score 

        If the user has already been fetched once, the data will be reused and no
        request will be sent to the osu api.
        """

        if mode is None:
            mode = self.mode

        if self._user is None:
            self._user = self.api.get_user(user=self.username, mode=self.mode)

        return self._user
