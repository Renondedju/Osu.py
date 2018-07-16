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

from abc         import ABCMeta
from .exceptions import UnreferencedApi

class BaseCollection(list, metaclass=ABCMeta):
    """ Base collection object, you cannot instantiate it
        unless you create a child class of it
    """

    def __init__(self, items=[], *, api : 'OsuApi', collection_type):
        self.__api     = api
        self.__type    = collection_type

        for item in items:
            self._check_type(item)

        super().__init__(items)

    def _check_type(self, item):
        if not isinstance(item, self.__type):
            raise ValueError(
                f'The item type should be of type '
                f'\'{self.__type.__name__}\', not \'{type(item).__name__}\'')

    @property
    def api(self):
        """ api getter """
        if self.__api is None:
            raise UnreferencedApi("The osu api reference cannot be 'None'")
        return self.__api

    def append(self, item):
        """ Adds item to the collection. """

        if not item:
            return

        self._check_type(item)
        super().append(item)
