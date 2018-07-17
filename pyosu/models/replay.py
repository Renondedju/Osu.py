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

from pyosu.types import GameMode
from .base import BaseModel


class Replay(BaseModel):
    """ Replay model
    
        Ref : https://github.com/ppy/osu-api/wiki#response-6  
        Note that the binary data you get when you decode above base64-string,
        is not the contents of an .osr-file.
        It is the LZMA stream referred to by the osu-wiki here:

        >   The remaining data contains information about mouse movement and key
        >   presses in an wikipedia:LZMA stream
        >   https://osu.ppy.sh/help/wiki/osu!_File_Formats/Osr_(file_format)

        Ref : https://github.com/ppy/osu-api/wiki#rate-limiting  
        As this is quite a load-heavy request, it has special rules about rate limiting.
        You are only allowed to do 10 requests per minute.
        Also, please note that this request is ___not___ intended for batch retrievals.
    """

    def __init__(self, *, api : 'OsuApi' = None, **data):

        super().__init__(api)

        self.beatmap_id = data.get('beatmap_id', 0)
        self.encoding   = data.get('encoding'  , "base64")
        self.content    = data.get('content'   , "")       #base64-encoded replay
        self.user       = data.get('user'      , "")
        self.mode       = data.get('mode'      , GameMode.Osu)

    async def get_beatmap(self, **parameters):
        """ Returns the beatmap's data of the replay """

        return await self.api.get_beatmap(beatmap_id=self.beatmap_id, **parameters)

    async def get_user(self, **parameters):
        """ Returns the user's data of the replay """

        return await self.api.get_user(user=self.user, **parameters)
