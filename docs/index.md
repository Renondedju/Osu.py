# Osu<span></span>.py documentation

## Table of content

- [OsuApi](index.md#osuapi)
  - [get_beatmap()](index.md#get_beatmap)
  - [get_beatmaps()](index.md#get_beatmaps)
  - [get_beatmap_file()](index.md#get_beatmap_file)
  - [get_user()](index.md#get_user)
  - [get_score()](index.md#get_score)
  - [get_scores()](index.md#get_scores)
  - [get_user_best()](index.md#get_user_best)
  - [get_user_bests()](index.md#get_user_bests)
  - [get_user_recent()](index.md#get_user_recent)
  - [get_user_recents()](index.md#get_user_recents)
  - [get_replay()](index.md#get_replay)
  - [get_match()](index.md#get_match)

- [Models](index.md#models)
  - [BaseModel](index.md#basemodel)
  - [Beatmap](index.md#beatmap)
  - [BeatmapFile](index.md#beatmapfile)
  - [User](index.md#user)
  - [UserEvent](index.md#userevent)
  - [UserBest](index.md#userbest)
  - [UserRecent](index.md#userrecent)
  - [Score](index.md#score)
  - [Replay](index.md#replay)
  - [MultiplayerMatch](index.md#multiplayermatch)
  - [MultiplayerGame](index.md#multiplayergame)
  - [MultiplayerScore](index.md#multiplayerscore)

- [Collections](index.md#containers)
  - [BaseCollection](index.md#basecollection)
  - [BeatmapCollection](index.md#beatmapcollection)
  - [ScoreCollection](index.md#scorecollection)
  - [UserBestCollection](index.md#userbestcollection)
  - [UserRecentCollection](index.md#userrecentcollection)

- [Enums](index.md#enums)
  - [BeatmapGenre](index.md#beatmapgenre)
  - [BeatmapApprovedState](index.md#beatmapapprovedstate)
  - [GameMode](index.md#gamemode)
  - [GameModifier](index.md#gamemodifier)
  - [Language](index.md#language)
  - [MultiplayerTeam](index.md#multiplayerteam)
  - [ReplayAvailability](index.md#replayavailability)
  - [ScoringType](index.md#scoringtype)
  - [TeamType](index.md#teamtype)

- [Exceptions](index.md#exceptions)
  - [WrongApiKey](index.md#wrongapikey)
  - [RouteNotFound](index.md#routenotfound)
  - [InvalidArgument](index.md#invalidargument)
  - [HTTPError](index.md#httperror)
  - [UnreferencedApi](index.md#unreferencedapi)
  - [ReplayUnavailable](index.md#replayunavailable)

-----

## OsuApi

> This is the main library class

### get_beatmap()

> This function is a coroutine

__Retrieve general beatmap information.__

Function declaration :

```py
async def get_beatmap(self, beatmapset_id = None, beatmap_id = None, user = None, type_str = None, mode = None, include_converted = None, hash_str = None)
```

If any of the parameters used returns more than one beatmap, the first one only will be returned.  
If you want multiple beatmaps, use [OsuApi.get_beatmaps()](index.md#get_beatmaps) instead.  

Parameters :

    beatmapset_id     - specify a beatmapset_id to return metadata from.  

    beatmap_id        - specify a beatmap_id to return metadata from.  

    user              - specify a user_id or a username to return metadata from.  

    type_str          - specify if 'user' is a user_id or a username.  
                        Use `string` for usernames or `id` for user_ids.
                        Optional, default behavior is automatic recognition
                        (may be problematic for usernames made up of digits only).  

    mode              - mode (0 = osu!, 1 = Taiko, 2 = CtB, 3 = osu!mania).
                        Optional, maps of all modes are returned by default.  

    include_converted - specify whether converted beatmaps are included
                        (0 = not included, 1 = included).
                        Only has an effect if 'mode' is chosen and not 0.
                        Converted maps show their converted difficulty rating.
                        Optional, default is 0.  

    hash_str          - the beatmap hash. It can be used, for instance,
                        if you're trying to get what beatmap has a replay played in,
                        as .osr replays only provide beatmap hashes
                        (example of hash: a5b99395a42bd55bc5eb1d2411cbdf8b).
                        Optional, by default all beatmaps are returned independently from the hash.

-> Returns a [Beatmap](index.md#beatmap) model, None if the request failed

### get_beatmaps()

> This function is a coroutine

__Retrieve general beatmap information.__

Function declaration :

```py
async def get_beatmaps(self, limit = None, since = None, type_str = None, beatmapset_id = None, include_converted = None, user = None, mode = None)
```

Do note that requesting a beatmap collection is way faster than
requesting beatmap by beatmap *(and requires only only one api request)*

Parameters :

    limit             - amount of results. Optional, default and maximum are 500.

    since             - return all beatmaps ranked or loved since this date.  
                        Must be a MySQL date.  

    beatmapset_id     - specify a beatmapset_id to return metadata from.  

    user              - specify a user_id or a username to return metadata from.

    type_str          - specify if 'user' is a user_id or a username.
                        Use `string` for usernames or `id` for user_ids.
                        Optional, default behavior is automatic recognition
                        (may be problematic for usernames made up of digits only).

    mode              - mode see GameMode enum.  
                        Optional, maps of all modes are returned by default.

    include_converted - specify whether converted beatmaps are included
                        (0 = not included, 1 = included).
                        Only has an effect if 'mode' is chosen and not 0.
                        Converted maps show their converted difficulty rating.
                        Optional, default is 0.

-> Returns a [BeatmapCollection](index.md#beatmapcollection) collection, None if the request failed

### get_beatmap_file()

> This function is a coroutine

__Retrieve .osu beatmap file__

Function declaration :

```py
async def get_beatmap_file(self, beatmap_id)
```

This function doesn't use any api request.  
Fetching a [BeatmapFile](index.md#beatmapfile) model is way heavier than a classic [Beatmap](index.md#beatmap) model (3Kb to 1Mb) since it contains the beatmap file.  
If you don't really need it, don't use it !

Parameters :

    beatmap_id - the beatmap ID (not beatmap set ID!) (required).

-> Returns a [BeatmapFile](index.md#beatmapfile) model, None if the request failed

### get_user()

> This function is a coroutine

__Retrieve general user information.__

Function declaration :

```py
async def get_user(self, user, mode = None, type_str = None, event_days = None)
```

Parameters :

    user       - specify a user_id or a username to return metadata from (required).

    mode       - mode, see GameMode enum
                 Optional, default value is 0.

    type_str   - specify if u is a user_id or a username.
                 Use `string` for usernames or `id` for user_ids.
                 Optional, default behavior is automatic recognition
                 (may be problematic for usernames made up of digits only).

    event_days - Max number of days between now and last event date.  
                 Range of 1-31. Optional, default value is 1.

-> Returns a [User](index.md#user) model, None if the request failed

### get_score()

> This function is a coroutine

__Retrieve information about the top 100 scores of a specified beatmap.__

Function declaration :

```py
async def get_score(self, beatmap_id, user = None, mode = None, type_str = None)
```

If any of the parameters used returns more than one score, only the first one will be returned.  
If you want multiple scores use [OsuApi.get_scores()](index.md#get_scores) instead

Parameters :

    beatmap_id - specify a beatmap_id to return metadata from. (required)

    user       - specify a user_id or a username to return metadata from.

    type_str   - specify if 'user' is a user_id or a username.
                 Use `string` for usernames or `id` for user_ids.
                 Optional, default behavior is automatic recognition
                 (may be problematic for usernames made up of digits only).

    mode       - mode, see GameMode enum
                 Optional, maps of all modes are returned by default.

-> Returns a [Score](index.md#score) model, None if the request failed

### get_scores()

> This function is a coroutine

__Retrieve information about the top 100 scores of a specified beatmap.__

Function declaration :

```py
async def get_scores(self, beatmap_id, user = None, mode = None, mods = None, type_str = None, limit = None)
```

Do note that requesting a score collection is way faster than requesting score by score *(and requires only only one api request)*

Parameters :

    beatmap_id - specify a beatmap_id to return score information from (required).

    user       - specify a user_id or a username to return score information for.

    mode       - mode, see the GameMode enum
                 Optional, default value is 0 (Osu).

    mods       - specify a mod or mod combination (See the GameModifiers enum)

    type_str   - specify if user is a user_id or a username.
                 Use string for usernames or id for user_ids.
                 Optional, default behavior is automatic recognition
                 (may be problematic for usernames made up of digits only).

    limit      - amount of results from the top (range between 1 and 100 - defaults to 50).

-> Returns a [ScoreCollection](index.md#scorecollection) collection, None if the request failed

### get_user_best()

> This function is a coroutine

__Get the top score for the specified user.__

Function declaration :

```py
async def get_user_best(self, user, mode = None, type_str = None)
```

If you want more than one user best use [OsuApi.get_user_bests()](index.md#get_user_bests) instead.

Parameters :

    user     - specify a user_id or a username to return best scores from (required).

    mode     - mode, see the GameMode enum.
               Optional, default value is 0 (Osu).

    type_str - specify if user is a user_id or a username.
               Use 'string' for usernames or 'id' for user_ids.
               Optional, default behavior is automatic recognition
               may be problematic for usernames made up of digits only).

-> Returns a [UserBest](index.md#userbest) model, None if the request failed

### get_user_bests()

> This function is a coroutine

__Get the top scores for the specified user.__

Function declaration :

```py
async def get_user_bests(self, user, mode = None, type_str = None, limit = None)
```

Parameters :

    user       - specify a user_id or a username to return best scores from (required).

    mode       - mode, see the GameMode enum
                 Optional, default value is 0 (Osu).

    type_str   - specify if user is a user_id or a username.
                 Use 'string' for usernames or 'id' for user_ids.
                 Optional, default behavior is automatic recognition
                 (may be problematic for usernames made up of digits only).

    limit      - amount of results from the top (range between 1 and 100 - defaults to 50).

-> Returns a [UserBestCollection](index.md#userbestcollection) collection, None if the request failed

### get_user_recent()

> This function is a coroutine

__Gets the user's most recent play over the last 24 hours.__

Function declaration :

```py
async def get_user_recent(self, user, mode = None, type_str = None)
```

If you want more than one user recent use OsuApi.get_user_recent() instead.

Parameters :

    user     - specify a user_id or a username to return best scores from (required).

    mode     - mode, see the GameMode enum
               Optional, default value is 0 (Osu).

    type_str - specify if user is a user_id or a username.
               Use 'string' for usernames or 'id' for user_ids.
               Optional, default behavior is automatic recognition
               may be problematic for usernames made up of digits only).

-> Returns a [UserRecent](index.md#userrecent) model, None if the request failed

### get_user_recents()

> This function is a coroutine

__Gets the user's most recent plays over the last 24 hours.__

Function declaration :

```py
async def get_user_recents(self, user, mode = None, type_str = None, limit = None)
```

Parameters :

    user       - specify a user_id or a username to return best scores from (required).

    mode       - mode, see the GameMode enum
                 Optional, default value is 0 (Osu).

    type_str   - specify if user is a user_id or a username.
                 Use 'string' for usernames or 'id' for user_ids.
                 Optional, default behavior is automatic recognition
                 (may be problematic for usernames made up of digits only).

    limit      - amount of results from the top (range between 1 and 100 - defaults to 50).

-> Returns a [UserRecentCollection](index.md#userrecentcollection) collection, None if the request failed

### get_replay()

> This function is a coroutine

__Get the replay data of a user's score on a map.__

Function declaration :

```py
async def get_replay(self, mode, beatmap_id, user)
```

Official doc : https://github.com/ppy/osu-api/wiki#get-replay-data

Ref : https://github.com/ppy/osu-api/wiki#rate-limiting  
As this is quite a load-heavy request, it has special rules about rate limiting.
You are only allowed to do 10 requests per minute.
Also, please note that this request is ___not___ intended for batch retrievals.

Parameters:

    mode        - the mode the score was played in (required)

    beatmap_id  - the beatmap ID (not beatmap set ID!) in which the replay was played (required).

    user        - the user that has played the beatmap (required).

-> Returns a [Replay](index.md#replay) model, None if the request failed

### get_match()

> This function is a coroutine

__Retrieve information about multiplayer match.__

Function declaration :

```py
async def get_match(self, match_id)
```

Parameters :

    match_id - match id to get information from (required).

-> Returns a [MultiplayerMatch](index.md#multiplayermatch) model, None if the request failed

-----

## Models

> Models are classes that represents a JSON response from the osu api  
> Every [OsuApi](index.md#osuapi) method returns a model, empty or not

### BaseModel

> Metaclass : cannot be instantiated.

Fields :

- property ``api`` : [OsuApi](index.md#osuapi)  
    Raises an [UnreferencedApi](index.md#unreferencedapi) error if null when requested.

### Beatmap

> Inherits from [BaseModel](index.md#basemodel)

Represents a beatmap

Fields :

- ``approved``         : [BeatmapApprovedState](index.md#beatmapapprovedstate)  

    Approved state of the beatmap

- ``approved_date``    : str  

    Date ranked, UTC+8 for now  
    *example : '2013-07-02 01:01:12'*

- ``last_update``      : str  

    Last update date, timezone same as above.  
    May be after approved_date if map was unranked and reranked.  
    *example : '2013-07-02 01:01:12'*

- ``artist``           : str  

    Artist name of the song.

- ``beatmap_id``       : int  

    beatmap_id is per difficulty.

- ``beatmapset_id``    : int  

    beatmapset_id groups difficulties into a set.

- ``bpm``              : float  

    Beats per minute.

- ``creator``          : str  

    Creator of the beatmap.

- ``difficultyrating`` : float  

    The amount of stars the map would have ingame and on the website

- ``diff_size``        : float  

    Circle size value (CS)

- ``diff_overall``     : float  

    Overall difficulty (OD)

- ``diff_approach``    : float  

    Approach Rate (AR)

- ``diff_drain``       : float  

    Healthdrain (HP)

- ``hit_length``       : float  

    Seconds from first note to last note not including breaks

- ``source``           : str  

- ``genre_id``         : [BeatmapGenre](index.md#beatmapgenre)  

    Music genre of the beatmap

- ``language_id``      : [Language](index.md#language)  

    Language of the beatmap

- ``title``            : str  

    Song name

- ``total_length``     : float  

    Seconds from first note to last note including breaks

- ``version``          : str

    Difficulty name

- ``file_md5``         : str  

    md5 hash of the beatmap

- ``mode``             : [GameMode](index.md#gamemode)  

    Game mode

- ``tags``             : str  

    Beatmap tags separated by spaces.

- ``favourite_count``  : int  

    Number of times the beatmap was favourited.

- ``playcount``        : int  

    Number of times the beatmap was played

- ``passcount``        : int  

    Number of times the beatmap was passed, completed (the user didn't fail or retry)

- ``max_combo``        : int  

    The maximum combo a user can reach playing this beatmap.

Methods :

- ``get_beatmapset()``

    Returns a [BeatmapCollection](index.md#beatmapcollection) containing the beatmapset of the current beatmap.

### BeatmapFile

> Inherits from [BaseModel](index.md#basemodel)

Represents a beatmap .osu file  
This model is way heavier than a classic Beatmap object (3Kb to 1Mb+) since it contains the beatmap file.  
If you don't really need it, don't use it !

Fields :

- ``content`` : str

    Actual content of the beatmap file

- ``version`` : int

    Version of the beatmap file *(useful for parsing)*

Methods :

- ``get_category(category_name : str) -> str``

    Gets a file category  

    *Example :*  
    Calling get_category('Editor') on a file with version == 14
    might return something like :

    ```txt
    DistanceSpacing: 0.9  
    BeatDivisor: 2  
    GridSize: 4  
    TimelineZoom: 1.399999  
    ```

### User

> Inherits from [BaseModel](index.md#basemodel)

Represent users statistics

Fields :

- ``user_id``         : int
- ``username``        : str
- ``count300``        : int
- ``count100``        : int
- ``count50``         : int
- ``playcount``       : int

    Only counts ranked, approved, and loved beatmaps

- ``ranked_score``    : float

    Counts the best individual score on each ranked, approved, and loved beatmaps

- ``total_score``     : float

    Counts every score on ranked, approved, and loved beatmaps

- ``pp_rank``         : int
- ``level``           : float
- ``pp_raw``          : float

    For inactive players this will be 0 to purge them from leaderboards

- ``accuracy``        : float
- ``count_rank_ss``   : int
- ``count_rank_ssh``  : int
- ``count_rank_s``    : int
- ``count_rank_sh``   : int
- ``count_rank_a``    : int
- ``country``         : str

    Uses the ISO3166-1 alpha-2 country code naming.  
    See this for more information: *http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2/*

- ``pp_country_rank`` : int

    The user's rank in the country.

- ``events``          : list

    A list [UserEvent](index.md#userevent) for this user  

### UserEvent

> Inherits from [BaseModel](index.md#basemodel)

Represent a user event

Fields :

- ``display_html``  : str
- ``beatmap_id``    : int
- ``beatmapset_id`` : int
- ``date``          : str
- ``epicfactor``    : int

    How "epic" this event is (between 1 and 32)

### UserBest

> Inherits from [BaseModel](index.md#basemodel)

Represent a user best score

Fields :

- ``beatmap_id``   : int
- ``score``        : float
- ``maxcombo``     : int
- ``count300``     : int
- ``count100``     : int
- ``count50``      : int
- ``countmiss``    : int
- ``countkatu``    : int
- ``countgeki``    : int
- ``perfect``      : bool

    True = maximum combo of map reached, False otherwise

- ``enabled_mods`` : int

    Bitwise flag representation of mods used.  
    See reference [GameModifiers](index.md#gamemodifiers)

- ``user_id``      : int
- ``date``         : str
- ``rank``         : str
- ``pp``           : float

    Float value , 4 decimals

### UserRecent

> Inherits from [BaseModel](index.md#basemodel)

Represent a user recent score

Fields :

- ``beatmap_id``   : int
- ``score``        : float
- ``maxcombo``     : int
- ``count300``     : int
- ``count100``     : int
- ``count50``      : int
- ``countmiss``    : int
- ``countkatu``    : int
- ``countgeki``    : int
- ``perfect``      : bool

    True = maximum combo of map reached, False otherwise

- ``enabled_mods`` : int

    Bitwise flag representation of mods used.  
    See reference [GameModifiers](index.md#gamemodifiers)

- ``user_id``      : int
- ``date``         : str
- ``rank``         : str

### Score

> Inherits from [BaseModel](index.md#basemodel)

Represents a score

Fields :

- ``score_id``         : int
- ``score``            : float
- ``username``         : str
- ``count300``         : int
- ``count100``         : int
- ``count50``          : int
- ``countmiss``        : int
- ``maxcombo``         : int
- ``countkatu``        : int
- ``countgeki``        : int
- ``perfect``          : bool

    True = maximum combo of map reached, False otherwise

- ``enabled_mods``     : int

    Bitwise flag representation of mods used.  
    See reference [GameModifier](index.md#gamemodifier)

- ``user_id``          : int
- ``date``             : str
- ``rank``             : str
- ``pp``               : float
- ``replay_available`` : [ReplayAvailability](index.md#replayavailability)
- ``mode``             : int

Methods :

- ``get_user_data(mode = None)``

    Returns the data of the author of the score

    If the user has already been fetched once, the data will be reused and no
    request will be sent to the osu api.

### Replay

> Inherits from [BaseModel](index.md#basemodel)

Replay model

Ref : https://github.com/ppy/osu-api/wiki#response-6  
Note that the binary data you get when you decode above base64-string,  
is not the contents of an .osr-file.  
It is the LZMA stream referred to by the osu-wiki here:  

> The remaining data contains information about mouse movement and key  
> presses in an wikipedia:LZMA stream  
> [link](https://osu.ppy.sh/help/wiki/osu!_File_Formats/Osr_(file_format))

Ref : https://github.com/ppy/osu-api/wiki#rate-limiting  
As this is quite a load-heavy request, it has special rules about rate limiting.  
You are only allowed to do 10 requests per minute.  
Also, please note that this request is ___not___ intended for batch retrievals.  

Fields :

- ``beatmap_id`` : int
- ``encoding``   : str = "base64"
- ``content``    : str

    base64-encoded replay

- ``user``       : str
- ``mode``       : [GameMode](index.md#gamemode)

Methods :

- ``get_beatmap(**parameters)``

    Returns the beatmap's data of the replay

- ``get_user(**parameters)``

    Returns the user's data of the replay

### MultiplayerMatch

> Inherits from [BaseModel](index.md#basemodel)

Multiplayer match model

Fields :

- ``start_time``: str
- ``match_id``  : int
- ``end_time``  : None

    Not supported yet - always None (Api side)

- ``name``      : str
- ``games``     : list

    A list of [MultiplayerGame](index.md#multiplayergame)

### MultiplayerGame

> Inherits from [BaseModel](index.md#basemodel)

Multiplayer game model

Fields :

- ``game_id``      : int
- ``start_time``   : str
- ``end_time``     : str
- ``beatmap_id``   : int
- ``play_mode``    : [GameMode](index.md#gamemode)

    Gamemode played

- ``match_type``   : int
- ``scoring_type`` : [ScoringType](index.md#scoringtype)

    Winning condition

- ``team_type``    : [TeamType](index.md#teamtype)

    Team type

- ``mods``         : [GameModifier](index.md#gamemodifier)

    Global mods

- ``scores``       : list

    A list of [MultiplayerScore](index.md#multiplayerscore)

### MultiplayerScore

> Inherits from [BaseModel](index.md#basemodel)

Multiplayer score model

Fields :

- ``slot``      : int

    0 based index of player's slot

- ``team``      : [MultiplayerTeam](index.md#multiplayerteam)

    Player's team

- ``user_id``   : int
- ``score``     : int
- ``maxcombo``  : int
- ``rank``      : int

    Not used (Api side)

- ``count50``   : int
- ``count100``  : int
- ``count300``  : int
- ``countmiss`` : int
- ``countgeki`` : int
- ``countkatu`` : int
- ``perfect``   : bool

    Full combo

- ``passed``    : bool

    Does the player passed the map at the end ?

## Collections

> Collections are classes that stores a list of specific model.  
> Some api functions might return a collection if there is multiple results to the request sent.  
> *ex.* [OsuApi.get_beatmaps()](index.md#get_beatmaps)

### BaseCollection

> Metaclass : cannot be instanciated.  
> Inherits from list

Fields :

- property ``api`` : [OsuApi](index.md#osuapi)  
    raises an [UnreferencedApi](index.md#unreferencedapi) exception if the api is null.

Functions :

- ``append(item)``  
    Adds an item to the collection.

### BeatmapCollection

> Inherits from [BaseCollection](index.md#basecollection)

The BeatmapCollection.append() function is limited to the [Beatmap](index.md#beatmap) type

### ScoreCollection

> Inherits from [BaseCollection](index.md#basecollection)

The ScoreCollection.append() function is limited to the [Score](index.md#score) type

### UserBestCollection

> Inherits from [BaseCollection](index.md#basecollection)

The UserBestCollection.append() function is limited to the [UserBest](index.md#userbest) type

### UserRecentCollection

> Inherits from [BaseCollection](index.md#basecollection)

The UserRecentCollection.append() function is limited to the [UserRecent](index.md#userrecent) type

-----

## Enums

### BeatmapGenre

Beatmap music genre

```py
Any         = 0
Unspecified = 1
Video_game  = 2
Anime       = 3
Rock        = 4
Pop         = 5
Other       = 6
Novelty     = 7
Hip_hop     = 9    #Note that there is no 8
Electronic  = 10
```

### BeatmapApprovedState

Beatmaps approved states

```py
Graveyard = -2
WIP       = -1
Pending   = 0
Ranked    = 1
Approved  = 2
Qualified = 3
Loved     = 4
```

### GameMode

Game modes

```py
Osu   = 0 #Std
Taiko = 1
Catch = 2 #Ctb
Mania = 3
```

### GameModifier

Game mods.  
Bitwise enum representing a combination of enabled mods.  
Can be stacked using the | (pipe) operator
[Link](https://github.com/ppy/osu-api/wiki#mods) to the official docs

```py
none              = 0
NoFail            = 1 << 0
Easy              = 1 << 1
TouchDevice       = 1 << 2
Hidden            = 1 << 3
HardRock          = 1 << 4
SuddenDeath       = 1 << 5
DoubleTime        = 1 << 6
Relax             = 1 << 7
HalfTime          = 1 << 8
Nightcore         = 1 << 9  # Only set along with DoubleTime. i.e: NC only gives 576
Flashlight        = 1 << 10
Autoplay          = 1 << 11
SpunOut           = 1 << 12
Relax2            = 1 << 13 # Autopilot
Perfect           = 1 << 14 # Only set along with SuddenDeath. i.e: PF only gives 16416  
Key4              = 1 << 15
Key5              = 1 << 16
Key6              = 1 << 17
Key7              = 1 << 18
Key8              = 1 << 19
FadeIn            = 1 << 20
Random            = 1 << 21
Cinema            = 1 << 22
Target            = 1 << 23
Key9              = 1 << 24
KeyCoop           = 1 << 25
Key1              = 1 << 26
Key3              = 1 << 27
Key2              = 1 << 28
ScoreV2           = 1 << 29
LastMod           = 1 << 30
KeyMod            = Key1 | Key2 | Key3 | Key4 | Key5 | Key6 | Key7 | Key8 | Key9 | KeyCoop
FreeModAllowed    = NoFail | Easy | Hidden | HardRock | SuddenDeath | Flashlight | FadeIn | Relax | Relax2 | SpunOut | KeyMod
ScoreIncreaseMods = Hidden | HardRock | DoubleTime | Flashlight | FadeIn
```

### Language

Language id's

```py
Any          = 0
Other        = 1
English      = 2
Japanese     = 3
Chinese      = 4
Instrumental = 5 #Yep ! Instrumental is a language :)
Korean       = 6
French       = 7
German       = 8
Swedish      = 9
Spanish      = 10
Italian      = 11
```

### MultiplayerTeam

Multiplayer team

```py
none = 0 # Teams where not supported this game
blue = 1
red  = 2
```

### ReplayAvailability

Availability states of a replay.  
*If you really want to, a boolean can be used instead*

```py
Unavailable = 0
Available   = 1
```

### ScoringType

Multiplayer winning condition

```py
score    = 0
accuracy = 1
combo    = 2
score_v2 = 3
```

### TeamType

Multiplayer team type

```py
head_to_head = 0
tag_co_op    = 1
team_vs      = 2
tag_team_vs  = 3
```

-----

## Exceptions

> Main library exceptions

### WrongApiKey

Fields :

    message : str
    code    : int = 401

Exception raised by the osu API when the api key you provided is invalid.  
To get a valid api key, follow this [link](https://osu.ppy.sh/p/api).

### RouteNotFound

Fields :

    message : str
    code    : int = 404 or 302

Exception raised when the route you asked for don't exists or gets redirected to another url.  
This exception might be raised only if the api changes the valid paths.

### InvalidArgument

Fields :

    message : str
    code    : int = 400

Exception raised when one of the argument sent to the api isn't valid.
This exception should not be raised since all the arguments are processed by the library.

### HTTPError

Fields :

    message : str
    code    : int

Exception raised when an unhandeled exception is raised by the osu api.  

### UnreferencedApi

Fields :

    message : str

Exception raised by the library if you are trying to call a shorthand function on a invalid instance of a model.

### ReplayUnavailable

Fields :

        message : str
        code    : int = 400

Raised and handeled by the library when an unavaliable replay is requested.
