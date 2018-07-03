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

import pyosu

def test(function):
    """ Tests a function and sends a report if it fails """

    try :
        function()
        print(f"{function.__name__} : Success")

    except Exception as e:
        print(f"{function.__name__} : Failed !\n"
              f"{e}")

def test_GameMode():
    str(pyosu.GameMode(pyosu.GameMode.Osu))
    str(pyosu.GameMode(pyosu.GameMode.Taiko))
    str(pyosu.GameMode(pyosu.GameMode.Catch))
    str(pyosu.GameMode(pyosu.GameMode.Mania))

def test_GameModifier():

    modifier = pyosu.GameModifier(pyosu.GameModifier.SpunOut | pyosu.GameModifier.Nightcore)
    modifier += modifier

    if not (modifier == pyosu.GameModifier.SpunOut | pyosu.GameModifier.Nightcore):
        raise ValueError("modifier should be equals to 'pyosu.GameModifier.SpunOut | pyosu.GameModifier.Nightcore'")
    
    if not (modifier == modifier):
        raise ValueError("modifier should be equal to itself")

    modifier = pyosu.GameModifier(pyosu.GameModifier.SpunOut)

    if not modifier.has(pyosu.GameModifier.SpunOut):
        raise ValueError("Modifier should have pyosu.GameModifier.SpunOut")

def main():

    print('\n')

    test(test_GameMode)
    test(test_GameModifier)

    print("Tests done !")

if __name__ == '__main__':
    main()