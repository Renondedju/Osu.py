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

import abc

from .exceptions import UnreferencedApi

class BaseCollection(metaclass=abc.ABCMeta):
    """ Base collection object, you cannot instanciate it
        unless you create a child class of it
    """

    def __init__(self, api : 'OsuApi', collection_type):

        self._container = []
        self.__api     = api
        self.__type    = collection_type

    @property
    def api(self):
        """ api getter """

        if self.__api is None:
            raise UnreferencedApi("The osu api reference cannot be 'None'")
        
        return self.__api

    @api.setter
    def api(self, value : 'OsuApi'):
        """ api setter """

        self.__api = value
        return value

    @property
    def count(self):
        """ Returns the number of objects in the container of the collection """
        return len(self._container)

    @property
    def is_empty(self):
        """ Checks if the container of the collection is empty """
        return len(self._container) == 0

    def get_content(self):
        """ Returns the content of the collection """
        return self._container

    def add_content(self, content):
        """ Adds content to the collection. """

        if type(content) is not self.__type:
            raise ValueError(
                f'The content type should be of type '
                f'\'{self.__type.__name__}\', not \'{type(content).__name__}\'')

        if content is not None:
            self._container.append(content)

        return

    def remove_content(self, content):
        """ Removes content from the collection """

        if type(content) is not self.__type:
            raise ValueError(
                f'The content type should be of type '
                f'\'{self.__type.__name__}\', not \'{type(content).__name__}\'')

        return self._container.pop(content, None)