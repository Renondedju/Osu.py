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

from .http                import *
from .user                import *
from .utilities           import *
from .game_modes          import *
from .replay_availability import *

class Score():

    def __init__(self, api):

        self.score_id         = 0
        self.score            = 0.0
        self.username         = ""
        self.count300         = 0
        self.count100         = 0
        self.count50          = 0
        self.countmiss        = 0
        self.maxcombo         = 0
        self.countkatu        = 0
        self.countgeki        = 0
        self.perfect          = False # True = maximum combo of map reached, False otherwise
        self.enabled_mods     = 0     # Bitwise flag representation of mods used. see reference (GameModifier class)
        self.user_id          = 0
        self.date             = ""
        self.rank             = ""
        self.pp               = 0.0   # Float value , 4 decimals
        self.replay_available = ReplayAvailability.Unavailable
        self.mode             = 0

        self.is_empty = True
        self._user    = None
        self.api      = api

    async def get_user_data(self, mode = None):
        """ Returns the data of the author of the score 

        If the user has already been fetched once, the data will be reused and no
        request will be sent to the osu api.
        """

        if self.is_empty or self.username == "":
            return User(self.api)

        if mode is None:
            mode = self.mode

        if self._user is None:
            self._user = self.api.get_user(user=self.username, mode=self.mode)

        return self._user