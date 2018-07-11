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

from .base_model import BaseModel

class User(BaseModel):
    """ Contains users data """

    def __init__(self, api : 'OsuApi', user_events : list, **data):

        super().__init__(api, **data)
        
        self.user_id         = data.get('user_id'       , 0)
        self.username        = data.get('username'      , "")
        self.count300        = data.get('count300'      , 0)    # Total amount for all ranked, approved, and loved beatmaps played
        self.count100        = data.get('count100'      , 0)    # Total amount for all ranked, approved, and loved beatmaps played
        self.count50         = data.get('count50'       , 0)    # Total amount for all ranked, approved, and loved beatmaps played
        self.playcount       = data.get('playcount'     , 0)    # Only counts ranked, approved, and loved beatmaps
        self.ranked_score    = data.get('ranked_score'  , 0.0)  # Counts the best individual score on each ranked, approved, and loved beatmaps
        self.total_score     = data.get('total_score'   , 0.0)  # Counts every score on ranked, approved, and loved beatmaps
        self.pp_rank         = data.get('pp_rank'       , 0)
        self.level           = data.get('level'         , 0.0)
        self.pp_raw          = data.get('pp_raw'        , 0.0)  # For inactive players this will be 0 to purge them from leaderboards
        self.accuracy        = data.get('accuracy'      , 0.0)
        self.count_rank_ss   = data.get('count_rank_ss' , 0)
        self.count_rank_ssh  = data.get('count_rank_ssh', 0)
        self.count_rank_s    = data.get('count_rank_s'  , 0)    # Counts for SS/SSH/S/SH/A ranks on maps
        self.count_rank_sh   = data.get('count_rank_sh' , 0)
        self.count_rank_a    = data.get('count_rank_a'  , 0)    
        self.country         = data.get('country'       , "")   # Uses the ISO3166-1 alpha-2 country code naming.
                                                                # See this for more information: http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2/)
        self.pp_country_rank = data.get('pp_country_rank', 0)   # The user's rank in the country.
        self.events          = user_events                      # Contains events for this user