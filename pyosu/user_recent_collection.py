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

from .user_recent     import UserRecent
from .base_collection import BaseCollection

class UserRecentCollection(BaseCollection):
    """ User bests collection class """

    def __init__(self, api : 'OsuApi'):

        super().__init__(api, UserRecent)

    def get_user_recents(self):
        """ Returns the user recent of the collection """
        
        return self.get_content()

    def add_user_recent(self, user_recent : UserRecent):
        """ Adds a user recent to the collection """

        return self.add_content(user_recent)
 
    def remove_user_recent(self, user_recent : UserRecent):
        """ Removes a user recent from the collection """

        return self.remove_content(user_recent)