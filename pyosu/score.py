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

    def __init__(self):

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

    async def fetch(self, key, beatmap_id, session = None, user = None, mode = GameMode.Osu, type_str = None):
        """
            If any of the parameters used returns more than one score,
            the first one only will be used

            Parameters :

                'key' - api key (required).

                'beatmap_id' - specify a beatmap_id to return metadata from. (required)

                'session' - aiohttp session

                'user' - specify a user_id or a username to return metadata from.

                'type_str' - specify if 'user' is a user_id or a username. Use string for usernames or id 
                    for user_ids. Optional, default behaviour is automatic recognition
                    (may be problematic for usernames made up of digits only).

                'mode' - mode (0 = osu!, 1 = Taiko, 2 = CtB, 3 = osu!mania).
                    Optional, maps of all modes are returned by default.
        """

        route = Route('get_scores', key, b=beatmap_id, limit=1)

        route.param('u', user)
        route.param('m', mode)
        route.param('type', type_str)

        data = []
        if session is None:
            data = await route.fetch()
        else:
            data = await route.fetch_with_session(session)

        if len(data) is not 0:
            data = data[0]
        else:
            self.is_empty = True
            return

        # Assigning the fetched values to the variables
        self.is_empty = Utilities.apply_data(self, data)
        self.mode     = mode

    async def get_user_data(self, key, session = None, mode = None):
        """ Returns the data of the author of the score 

        If the user has already been fetched once, the data will be reused and no
        request will be sent to the osu api.
        """

        if self.is_empty or self.username == "":
            return User()

        if mode is None:
            mode = self.mode

        if self._user is None:
            user = User()
            await user.fetch(key, session=session, user=self.username, mode=mode)
            self._user = user

        return self._user