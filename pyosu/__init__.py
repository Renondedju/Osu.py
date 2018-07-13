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

"""
Osu API Wrapper
~~~~~~~~~~~~~~~~~~~
A basic wrapper for the Osu API.

:copyright: (c) 2018 Renondedju
:license: MIT, see LICENSE for more details.
"""

__title__     = 'osu.py'
__author__    = 'Renondedju'
__license__   = 'MIT'
__copyright__ = 'Copyright 2018 Renondedju'
__version__   = '0.4.0'

from .api                    import OsuApi
from .user                   import User
from .score                  import Score
from .replay                 import Replay
from .beatmap                import Beatmap
from .language               import Language
from .team_type              import TeamType
from .user_best              import UserBest
from .user_event             import UserEvent
from .exceptions             import *
from .game_modes             import GameMode
from .user_recent            import UserRecent
from .beatmap_file           import BeatmapFile
from .scoring_type           import ScoringType
from .beatmap_genre          import BeatmapGenre
from .game_modifiers         import GameModifier
from .multiplayer_team       import MultiplayerTeam
from .multiplayer_game       import MultiplayerGame
from .score_collection       import ScoreCollection
from .multiplayer_score      import MultiplayerScore
from .multiplayer_match      import MultiplayerMatch
from .beatmap_collection     import BeatmapCollection
from .replay_availability    import ReplayAvailability
from .user_best_collection   import UserBestCollection
from .user_recent_collection import UserRecentCollection
from .beatmap_approved_state import BeatmapApprovedState
