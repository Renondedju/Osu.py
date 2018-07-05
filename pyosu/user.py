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

#Trello card : https://trello.com/c/IXr5hLdu/11-user

import asyncio

from .http       import *
from .utilities  import *
from .user_event import *

class User():
    """ Contains users data """

    def __init__(self):
        
        self.user_id         = 0
        self.username        = ""
        self.count300        = 0    # Total amount for all ranked, approved, and loved beatmaps played
        self.count100        = 0    # Total amount for all ranked, approved, and loved beatmaps played
        self.count50         = 0    # Total amount for all ranked, approved, and loved beatmaps played
        self.playcount       = 0    # Only counts ranked, approved, and loved beatmaps
        self.ranked_score    = 0.0  # Counts the best individual score on each ranked, approved, and loved beatmaps
        self.total_score     = 0.0  # Counts every score on ranked, approved, and loved beatmaps
        self.pp_rank         = 0
        self.level           = 0.0
        self.pp_raw          = 0.0  # For inactive players this will be 0 to purge them from leaderboards
        self.accuracy        = 0.0
        self.count_rank_ss   = 0
        self.count_rank_ssh  = 0
        self.count_rank_s    = 0    # Counts for SS/SSH/S/SH/A ranks on maps
        self.count_rank_sh   = 0
        self.count_rank_a    = 0    
        self.country         = ""   # Uses the ISO3166-1 alpha-2 country code naming.
                                    # See this for more information: http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2/)
        self.pp_country_rank = 0    # The user's rank in the country.
        self.events          = []   # Contains events for this user

        self.is_empty = True

    async def fetch(self, key, session = None, user = None, mode = None,
        type_str = None, event_days = None):
        """
            Fetches a user data

            Parameters :

                'user'       - specify a user_id or a username to return metadata from (required).

                'mode'       - mode (0 = osu!, 1 = Taiko, 2 = CtB, 3 = osu!mania).
                               Optional, default value is 0.
                               
                'type_str'   - specify if u is a user_id or a username.
                               Use string for usernames or id for user_ids.
                               Optional, default behaviour is automatic recognition
                               (may be problematic for usernames made up of digits only).

                'event_days' - Max number of days between now and last event date. 
                               Range of 1-31. Optional, default value is 1.
        """

        route = Route('get_user', key)

        route.param('u', user)
        route.param('m', mode)
        route.param('type', type_str)
        route.param('event_days', event_days)

        data = []
        if session is None:
            data = await route.fetch()
        else:
            data = await route.fetch_with_session(session)

        if len(data) is not 0:
            data = data[0]
        else:
            return

        #Adding events
        for event in data['events']:
            user_event = UserEvent()
            Utilities.apply_data(user_event, event)
            self.events.append(user_event)

        # Assigning the fetched values to the variables
        self.is_empty = Utilities.apply_data(self, data, ['events'])