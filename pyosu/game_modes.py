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

#Trello card : https://trello.com/c/R5WkTqlO/5-game-modes-class

class GameMode():
    """
        Game mode class. Used to Represent the different game modes.

        Osu (std) = 0
        Taiko     = 1
        CtB       = 2
        osu!mania = 3

    """

    Osu   = 0
    Taiko = 1
    Catch = 2
    Mania = 3

    def __init__(self, mode : int):
        """ Inits the game mode """

        if mode not in [0, 1, 2, 3]:
            mode = 0

        self.mode = mode

    def __str__(self):
        """ Readable representation of the mode """

        if (self.mode is GameMode.Osu):
            return "Game mode : Osu"
        if (self.mode is GameMode.Taiko):
            return "Game mode : Taiko"
        if (self.mode is GameMode.Catch):
            return "Game mode : Catch the beat"
        if (self.mode is GameMode.Mania):
            return "Game mode : Mania"
        
        return "Game mode : Unknown"

    def __repr__(self):
        """ unambiguous representation of the mode """

        return self.__str__()