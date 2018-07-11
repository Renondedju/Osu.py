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

class WrongApiKey(Exception):
    """ Wrong api key exception """

    def __init__(self, message):

        super().__init__(message)
        self.code = 401

class RouteNotFound(Exception):
    """ The route that was targetted was not found """

    def __init__(self, message, code):

        super().__init__(message)
        self.code = code

class InvalidArgument(Exception):
    """ Invalid argument passed 
    This event is raised by the Route class if a parameter
    send isn't in the list of accepted parameters :

    [a, h, k, m, b, u, s, mp, limit, type, mods, event_days, since]
    """

    def __init__(self, param):

        super().__init__(f'Invalid parameter used : \'{param}\'')
        self.code = 400

class HTTPError(Exception):
    """ Unhandeled http error """

    def __init__(self, code, message):

        super().__init__(message)

        self.message = message
        self.code = code

class UnreferencedApi(Exception):
    """ Api instance isn't known """

    def __init__(self, message):

        super().__init__(message)
        
        self.message = message