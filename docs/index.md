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

### Beatmap

### BeatmapFile

### User

### UserEvent

### UserBest

### UserRecent

### Score

### Replay

### MultiplayerMatch

### MultiplayerGame

### MultiplayerScore

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
