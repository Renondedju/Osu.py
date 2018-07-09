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

class UserBest():
    """ User best model """

    def __init__(self, api):

        self.beatmap_id   = 0
        self.score        = 0.0
        self.maxcombo     = 0
        self.count300     = 0
        self.count100     = 0
        self.count50      = 0
        self.countmiss    = 0
        self.countkatu    = 0
        self.countgeki    = 0
        self.perfect      = False        # True = maximum combo of map reached, False otherwise
        self.enabled_mods = 0            # bitwise flag representation of mods used. see reference (GameModifiers)
        self.user_id      = 0
        self.date         = ""
        self.rank         = ""
        self.pp           = 0.0          # Float value , 4 decimals

        self.is_empty     = True
        self.api          = api

        self._beatmap     = None
        self._user        = None

    async def get_user(self):

        if self._user is None:
            self._user = await self.api.get_user(user = self.user_id, type_str = 'id')

        return self._user

    async def get_beatmap(self):

        if self._beatmap is None:
            self._beatmap = await self.api.get_beatmap(beatmap_id = self.beatmap_id)

        return self._beatmap