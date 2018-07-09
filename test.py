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
api = Api(json.load(open('test-config.json'))['api_key'])

async def test(function):
    """ Tests a function and sends a report if it fails """

    global pass_count, test_count

    try :
        if inspect.iscoroutinefunction(function):
            print(f"starting couroutine test : {function.__name__}", end = '...')
            await function()
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

async def test_score():
    score = await api.get_score(1461701)
    if score.is_empty:
        raise ValueError('Empty score !')

async def test_user():
    user = await api.get_user(user = 'Renondedju', mode = GameMode.Mania)
    if user.is_empty:
        raise ValueError('Empty user !')

async def test_beatmap():
    beatmap = await api.get_beatmap(beatmap_id=1461701)
    if beatmap.is_empty:
        raise ValueError('Empty beatmap !')

async def test_beatmap_collection():
    beatmapset = await api.get_beatmaps(beatmapset_id=690687)
    if beatmapset.is_empty:
        raise ValueError('Empty beatmapset !')

async def test_score_collection():
    scores = await api.get_scores(1461701)
    if scores.is_empty:
        raise ValueError('Empty scores !')

async def main():

    await test(test_user)
    await test(test_beatmap)
    await test(test_beatmap_collection)
    await test(test_score)
    await test(test_score_collection)

    print('\n' + '-'*100)
    print(f"Tests done : {pass_count}/{test_count}")

    return

if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())