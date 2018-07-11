# Changelogs

> Osu<span></span>.py library changelogs

## Version 0.2.0

> User bests and recent are now avaliable !

- Improved loading times and reworked the base architecture of the api
- Created The BaseModel and BaseCollection classes for easier extensions
- Renamed Api class to OsuApi to avoid confusions
- Added OsuApi.get_user_best()
- Added OsuApi.get_user_bests()
- Added User Best model
- Added OsuApi.get_user_recent()
- Added OsuApi.get_user_recents()
- Added User Recent model

## Version 0.1.0

> Player scores are here !

- Added Score model 
- Added Replay Availability Enum
- Added Score collection model
- Created a chengelog :)
- Added the *\_\_version\_\_*, *\_\_copyright\_\_*, *\_\_license\_\_*, *\_\_author\_\_*
and *\_\_title\_\_* properties of the library
- New api system : everything can be get from one and unique class.
Everything returned is now a valid instance and client apps don't have to manage sessions themselves.
Just create an Api instance, and it manages everything
- Every model has now a pointer on the api instance
- Added the method get_beatmapset() on the beatmap model

-------

## Version 0.0.0

> This version is the first version of the library, there is verry fiew api
> features supported, everything here is subject to modifications

- Added Beatmaps class 
- Added Users class 
- Added Beatmap collections class 
- Added Language Enum
- Added Requests class (Route)
- Added Exceptions 
- Added User events class 
- Added Beatmap approved state Enum
- Added Game modifiers (mods)  
- Added Game modes (mode) Enum
- Added Beatmap genre (music genre) Enum
