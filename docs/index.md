# Osu<span></span>..py documentation

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

### get_beatmaps()

### get_beatmap_file()

### get_user()

### get_score()

### get_scores()

### get_user_best()

### get_user_bests()

### get_user_recent()

### get_user_recents()

### get_replay()

### get_match()

## Models

> Bla

### BaseModel

> Metaclass : cannot be instanciated.

Fields : 

- property ``api`` : [OsuApi](index.md#osuapi)  
    Raises an [UnreferencedApi](index.md#unreferencedapi) error if null when requested.

- ``is_empty`` : bool  
    Tells if the current model is empty *(because of an invalid request or an error)*

### Beatmap

> Inherits from [BaseModel](index.md#basemodel)

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

Fields :

- ``display_html``  : str
- ``beatmap_id``    : int
- ``beatmapset_id`` : int
- ``date``          : str
- ``epicfactor``    : int

    How "epic" this event is (between 1 and 32)

### UserBest

> Inherits from [BaseModel](index.md#basemodel)

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

### Replay

> Inherits from [BaseModel](index.md#basemodel)

### MultiplayerMatch

> Inherits from [BaseModel](index.md#basemodel)

### MultiplayerGame

> Inherits from [BaseModel](index.md#basemodel)

### MultiplayerScore

> Inherits from [BaseModel](index.md#basemodel)

## Collections

> Bla

### BeatmapCollection

### ScoreCollection

### UserBestCollection

### UserRecentCollection

## Enums

> Bla

### BeatmapGenre

### BeatmapApprovedState

### GameMode

### GameModifier

### Language

### MultiplayerTeam

### ReplayAvailability

### ScoringType

### TeamType

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
