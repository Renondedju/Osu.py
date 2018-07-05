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


import json
import asyncio
import aiohttp
import inspect
import traceback

from pyosu import *

pass_count = 0
test_count = 0

async def test(function, loop = None):
    """ Tests a function and sends a report if it fails """

    global pass_count, test_count

    try :
        if inspect.iscoroutinefunction(function):
            print(f"starting couroutine test : {function.__name__}", end = '...')
            await function(loop)
        else:
            print(f"starting test : {function.__name__}", end = '...')
            function()

        print(" Success.")
        pass_count += 1

    except Exception as e:
        print(" Failed.")
        traceback.print_tb(e.__traceback__)
        print(e)

    test_count += 1

async def test_user(loop = None):

    user = User()
    
    with open('test-config.json') as config_file:
        settings = json.load(config_file)
        
        await user.fetch(settings.get('api_key'), user = 'Renondedju')
        await user.fetch(settings.get('api_key'), user = 'Renondedju', mode = GameMode.Mania)
        
        if user.is_empty:
            raise ValueError("User is empty and shouldn't be !")

async def test_route(loop = None):

    route = Route('get_beatmaps', '123', b=123456)

    try:
        await route.fetch()
    except WrongApiKey:
        pass

    route.path = 'wrong path'

    try:
        await route.fetch()
    except RouteNotFound:
        pass

async def test_beatmap(loop = None):

    beatmap = Beatmap()

    with open('test-config.json') as config_file:
        settings = json.load(config_file)
        async with aiohttp.ClientSession(loop=loop) as session:

            await beatmap.fetch(settings.get('api_key'), beatmapset_id = 65536, session=session)
            await beatmap.fetch(settings.get('api_key'), beatmap_id = 65536, session=session)
            await beatmap.fetch(settings.get('api_key'), beatmap_id = 65536, user = 'Renondedju', session=session)
            await beatmap.fetch(settings.get('api_key'), beatmap_id = 65536, mode = GameMode.Mania, include_converted = True, session=session)

async def test_beatmap_collection(loop = None):

    beatmaps = BeatmapCollection()

    with open('test-config.json') as config_file:
        settings = json.load(config_file)
        
        await beatmaps.fetch(settings.get('api_key'), beatmapset_id = 327680)

async def main(loop):

    await test(test_user)
    await test(test_route)
    await test(test_beatmap)
    await test(test_beatmap_collection)

    print('\n' + '-'*100)
    print(f"Tests done : {pass_count}/{test_count}")

    return

if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))