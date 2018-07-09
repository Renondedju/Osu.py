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

from .user_best import UserBest

class UserBestCollection():
    """ User bests collection class """

    def __init__(self, api):

        self._user_bests = []
        self.api         = api

    @property
    def count(self):
        """ Returns the number of user bests of the collection """
        return len(self._user_bests)

    @property
    def user_bests(self):
        """ Returns the user bests of the collection """
        return self._user_bests

    @property
    def is_empty(self):
        """ Checks if the user bests collection si empty or not """
        return len(self._user_bests) == 0
    
    def add_user_best(self, best : UserBest):
        """ Adds a user best to the collection """

        if best is not None:
            self._user_bests.append(best)

        return

    def remove_score(self, best : UserBest):
        """ Removes a user best from the collection """

        if best is not None:
            self._user_bests.pop(best, None)

        return