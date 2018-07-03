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

#Trello card : https://trello.com/c/HG9eXUE0/7-game-modifiers-class

class GameModifier():
    """
        Game modifier class. Used to represent game modifiers

        Game modifiers can be stacked
    """

    #Static variables
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

    def __init__(self, modifiers : int):
        """ Inits a game modifier """

        self.modifiers = modifiers

    def __add__(self, other):
        """ Adds two game modifiers """

        return self.modifiers | other.modifiers

    def __eq__(self, other):
        """ Checks if 2 GameModifier are equals """

        if type(other) == int:
            return self.modifiers == other
        
        if type(other) == GameModifier:
            return self.modifiers == other.modifiers

        return False

    def __str__(self):
        """ Returns the string version of the game modifier """

        return str(self.modifiers)
    
    def __repr__(self):
        """ Returns the string representation of the game modifier """

        string = "Mods :"
        for key, value in self.__dict__.items():
            try:
                if (self.has(int(value))):
                    string += " " + key
            except:
                pass

        return string

    def has(self, modifier):
        """ Checks if the current modifiers has one
        or multiples mod(s) """

        if type(modifier) == int:
            return (self.modifiers & modifier) == modifier

        if type(modifier) == GameModifier:
            return (self.modifiers & modifier.modifiers) == modifier.modifiers

        return False