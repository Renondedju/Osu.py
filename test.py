# MIT License

# Copyright (c) 2018-2019 Renondedju

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
import inspect
import traceback

from pyosu import OsuApi
from pyosu.types import *

pass_count = 0
test_count = 0

with open('test-config.json') as f:
    config = json.load(f)

    api      = OsuApi(config['api_key'])
    username = config['username']

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
    if score is None:
        raise ValueError('Empty score !')

async def test_user():
    user = await api.get_user(user = username, mode = GameMode.Osu)
    if user is None:
        raise ValueError('Empty user !')

async def test_beatmap():
    beatmap = await api.get_beatmap(beatmap_id=1461701)
    if beatmap is None:
        raise ValueError('Empty beatmap !')

async def test_beatmap_collection():
    beatmapset = await api.get_beatmaps(beatmapset_id=690687)
    if beatmapset is None:
        raise ValueError('Empty beatmapset !')

async def test_score_collection():
    scores = await api.get_scores(1461701)
    if scores is None:
        raise ValueError('Empty scores !')

async def test_user_best():
    best = await api.get_user_best(username, mode = GameMode.Osu)
    if best is None:
        raise ValueError('Empty best !')
    
    if await best.get_beatmap() is None:
        raise ValueError('Empty best.get_beatmap() !')

    if await best.get_user() is None:
        raise ValueError('Empty best.get_user() !')

async def test_user_bests():
    bests = await api.get_user_bests(username)
    if bests is None:
        raise ValueError('User bests is empty, there should be 10 scores')

async def test_user_recent():
    await api.get_user_recent(username)

async def test_user_recents():
    await api.get_user_recents(username)

async def test_replay():
    await api.get_replay(GameMode.Osu, 390057, username)

async def test_match():

    await api.get_match(0)
    # Cannot test too much things here since a match is temporary

async def test_beatmap_file():

    b = await api.get_beatmap_file(390057)
    if b is None:
        raise ValueError('The beatmap file shouldn\'t be empty')

async def main():

    await test(test_user)
    await test(test_match)
    await test(test_score)
    #await test(test_replay)
    await test(test_beatmap)
    await test(test_user_best)
    await test(test_user_bests)
    await test(test_user_recent)
    await test(test_user_recents)
    await test(test_beatmap_file)
    await test(test_score_collection)
    await test(test_beatmap_collection)

    print('\n' + '-'*100)
    print(f"Tests done : {pass_count}/{test_count}")

    return

if __name__ == '__main__':
    asyncio.run(main())