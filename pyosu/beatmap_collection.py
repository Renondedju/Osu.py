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

#Trello card : https://trello.com/c/Deol8NYI/10-beatmap-collection

from .http      import *
from .beatmap   import *
from .utilities import *

class BeatmapCollection():
    """ Beatmap collection class """

    def __init__(self):

        self._beatmaps = []

    @property
    def count(self):
        """ Returns the number of beatmaps of the collection """
        return len(self._beatmaps)

    @property
    def is_empty(self):
        """ Checks if the beatmap collection si empty or not """
        return len(self._beatmaps) == 0

    @property
    def beatmaps(self):
        """ Returns the beatmaps of the collection """
        return self._beatmaps

    def add_beatmap(self, beatmap : Beatmap):
        """ Adds a beatmap to the collection """

        if beatmap is not None:
            self._beatmaps.append(beatmap)

        return

    def remove_beatmap(self, beatmap : Beatmap):
        """ Removes a beatmap from the collection """

        if beatmap is not None:
            self._beatmaps.pop(beatmap, None)

        return