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

# Trello card : https://trello.com/c/rXyJNvUD/9-http-module

import asyncio
import aiohttp
import json

from .exceptions import *

class Route:

    BASE = 'https://osu.ppy.sh/api/'

    def __init__(self, path : str, api_key : str, **parameters):

        self.retry_count = 5 # Number of retrys to do before throwing any errors
        self.path        = path
        self.api_key     = api_key
        self.parameters  = parameters

    @property
    def route(self):
        """ Returns the current route """
        params = ''
        for key, value in self.parameters.items():
            params += f'&{key}={value}'

        return f"{Route.BASE}{self.path}?k={self.api_key}{params}"
        
    def param(self, key, value):
        """ Adds or updates a prameter """

        self.parameters[key] = value
        return

    def remove_param(self, key):
        """ Removes a parameter from the route """

        return self.parameters.pop(key, None) != None

    async def get_json(self, response, *args):
        """ Returns the json version of an api response """
        text = await response.text()

        if (text == None or text == ''):
            return {}

        data = json.loads(text)

        if len(args) == 0:
            return data

        for key in args:

            try:
                data = data[args]
            except KeyError:
                return ''

        return data

    def check_params(self):
        """ Raise the InvalidArgument Exception if one of the parameters that is
        being used isn't in the following list : 
        
        [a, h, k, m, b, u, s, mp, limit, type, mods, event_days, since]
        """
        accepted_params = ['a', 'h', 'k', 'm', 'b', 'u', 's', 'mp',
            'limit', 'type', 'mods', 'event_days', 'since']

        for key in self.parameters.keys():
            if (key not in accepted_params):
                raise InvalidArgument(key)

        return

    def check_path(self):
        """ Raise the RouteNotFound Exception if the path isn't in the following list :

            [get_beatmaps, get_user, get_scores, get_user_best, get_user_recent, get_match, get_replay]
        """

        accepted_paths = ['get_beatmaps', 'get_user', 'get_scores',
            'get_user_best', 'get_user_recent',' get_match', 'get_replay']

        if self.path not in accepted_paths:
            raise RouteNotFound(f'The route {self.route} does not exists.', 404)
        
        return

    async def fetch_with_session(self, session):
        """ Fetches some data with a session using the actual route """

        self.check_params()
        self.check_path()

        for i in range(self.retry_count):
            async with session.get(self.route) as response:
                    
                if response.status == 401: #Unauthorized
                    raise WrongApiKey(await self.get_json(response, 'error'))

                if response.status in [302, 404]: #Redirection or route not found
                    raise RouteNotFound(f'{self.route} was not found.', response.status)

                if response.status != 200 and i == self.retry_count: #Unknown error
                    raise HTTPError(response.status, await self.get_json(response, 'error'))

                if response.status == 200:
                    return await self.get_json(response)

    async def fetch(self):
        """ Fetches some data using the actual route """

        async with aiohttp.ClientSession() as session:
            return await self.fetch_with_session(session)