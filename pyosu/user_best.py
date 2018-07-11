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

from .base_model import BaseModel

class UserBest(BaseModel):
    """ User best model """

    def __init__(self, api : 'OsuApi', **data):

        super().__init__(api, **data)

        self.beatmap_id   = data.get('beatmap_id'  , 0)
        self.score        = data.get('score'       , 0.0)
        self.maxcombo     = data.get('maxcombo'    , 0)
        self.count300     = data.get('count300'    , 0)
        self.count100     = data.get('count100'    , 0)
        self.count50      = data.get('count50'     , 0)
        self.countmiss    = data.get('countmiss'   , 0)
        self.countkatu    = data.get('countkatu'   , 0)
        self.countgeki    = data.get('countgeki'   , 0)
        self.perfect      = data.get('perfect'     , False)        # True = maximum combo of map reached, False otherwise
        self.enabled_mods = data.get('enabled_mods', 0)            # bitwise flag representation of mods used. see reference (GameModifiers)
        self.user_id      = data.get('user_id'     , 0)
        self.date         = data.get('date'        , "")
        self.rank         = data.get('rank'        , "")
        self.pp           = data.get('pp'          , 0.0)          # Float value , 4 decimals

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