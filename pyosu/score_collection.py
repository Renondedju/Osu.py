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

from .http      import *
from .score     import *
from .utilities import *

class ScoreCollection():
    """ Score collection class """

    def __init__(self, api):

        self._scores = []
        self.api     = api

    @property
    def count(self):
        """ Returns the number of scores of the collection """
        return len(self._scores)

    @property
    def scores(self):
        """ Returns the scores of the collection """
        return self._scores
    
    @property
    def is_empty(self):
        """ Checks if the score collection si empty or not """
        return len(self._scores) == 0
    
    def add_score(self, score : Score):
        """ Adds a score to the collection """

        if score is not None:
            self._scores.append(score)

        return

    def remove_beatmap(self, score : Score):
        """ Removes a score from the collection """

        if score is not None:
            self._scores.pop(score, None)

        return