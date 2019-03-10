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

import datetime

from pyosu.models.base import BaseModel

class UserEvent(BaseModel):
    """ Contains events for a user """

    def __init__(self, *, api : 'OsuApi' = None, **data):
        
        super().__init__(api)

        self.display_html   =     data.get('display_html' , "")
        self.beatmap_id	    = int(data.get('beatmap_id'	  , 0 ))
        self.epicfactor	    = int(data.get('epicfactor'	  , 1 )) # How "epic" this event is (between 1 and 32)
        self.beatmapset_id	= int(data.get('beatmapset_id', 0 ))
        self.date		    = datetime.datetime.strptime(data.get('date', "1970-01-01 00:00:00"), "%Y-%m-%d %H:%M:%S")
