# Osu<span></span>.py library [![dev chat](https://discordapp.com/api/guilds/310348632094146570/widget.png?style=shield)](https://discord.gg/Qsw3yD5)

A simple python implementation for the Osu! api.

This library is developed for [Uso! bot](https://github.com/Renondedju/Uso_Bot_V2.0), a discord recommendation bot for osu beatmaps

## Requirements

- Python 3.6+ *(python 3.7 is partially unsupported due to the changes to asyncio)*
- The *aiohttp* library : [Install instructions](https://aiohttp.readthedocs.io/en/stable/)
- An internet connexion

## Installation

Open a terminal and write

    pip install git+https://github.com/Renondedju/Osu.py

Or from the source

    $ git clone https://github.com/Renondedju/Osu.py
    $ cd Osu.py
    $ pip install .

## Documentations

Link to the [docs](docs/index.md)

## Modifications

To get the current version of the library simply write and execute :

```py
import pyosu #Make sure your import path is the right one
print(pyosu.__version__)
```

Link to the [chagelogs](changelog.md)

## Thanks

Thanks to @ppy for [the osu api](https://github.com/ppy/osu-api/wiki)

## License

Osu<span></span>.py is released under the [MIT License](http://www.opensource.org/licenses/MIT). Check [the license](LICENSE) for more details.