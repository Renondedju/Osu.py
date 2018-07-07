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

    def __init__(self):

        self._scores = []

    @property
    def count(self):
        """ Returns the number of scores of the collection """
        return len(self._scores)

    @property
    def scores(self):
        """ Returns the scores of the collection """
        return self._scores

    
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

    async def fetch(self, key, beatmap_id, user = None, mode = None, mods = None, session = None, type_str = None, limit = None):
        """
            Do note that requesting a score collection is way faster than 
            requesting score by score (and requiers only only one api request)

            Parameters :

                key        - api key (required).
                beatmap_id - specify a beatmap_id to return score information from (required).
                user       - specify a user_id or a username to return score information for.
                mode       - mode (0 = osu!, 1 = Taiko, 2 = CtB, 3 = osu!mania).
                             Optional, default value is 0.
                mods       - specify a mod or mod combination (See the bitwise enum)
                type_str   - specify if user is a user_id or a username.
                             Use string for usernames or id for user_ids.
                             Optional, default behaviour is automatic recognition
                             (may be problematic for usernames made up of digits only).
                limit      - amount of results from the top (range between 1 and 100 - defaults to 50).
                session    - aiohttp session
        """

        route = Route('get_scores', key, b=beatmap_id)

        route.param('u', user)
        route.param('m', mode)
        route.param('mods', mods)
        route.param('type', type_str)
        route.param('limit', limit)

        datas = []
        if session is None:
            datas = await route.fetch()
        else:
            datas = await route.fetch_with_session(session)

        for data in datas:
            score = Score()
            score.is_empty = Utilities.apply_data(score, data)

            self._scores.append(score)

        return