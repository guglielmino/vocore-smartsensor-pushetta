# The MIT License (MIT)
#
# Copyright (c) 2014 Stefan Wendler
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
##

"""
Digital IO on VoCode Board using SYSFS
"""

__author__ = 'Stefan Wendler, sw@kaltpost.de'

# Available pins on th VoCore
GPIO0 = 0
GPIO7 = 7
GPIO8 = 8
GPIO9 = 9
GPIO12 = 12
GPIO13 = 13
GPIO14 = 14
GPIO17 = 17
GPIO18 = 18
GPIO19 = 19
GPIO20 = 20
GPIO21 = 21
GPIO22 = 22
GPIO23 = 23
GPIO24 = 24
GPIO25 = 25
GPIO26 = 26


class Pin:

    pinId = None
    pinDir = ""

    def __init__(self, pinId):
        self.pinId = pinId
        self.export()

    def __del__(self):
        self.unexport()

    def state(self):
        f = file(self.pinDir + "value", "r")
        s = f.read()
        f.close()

        if s == "1\n":
            return 1

        return 0

    def export(self):
        f = file("/sys/class/gpio/export", "w")
        f.write("%d" % self.pinId)
        f.close()
        self.pinDir = "/sys/class/gpio/gpio%d/" % self.pinId

    def unexport(self):
        f = file("/sys/class/gpio/unexport", "w")
        f.write("%d" % self.pinId)
        f.close()

    def __str__(self):
        return ("P_%d" % self.pinId)


class PinIn(Pin):

    def __init__(self, pinId):
        Pin.__init__(self, pinId)
        f = file(self.pinDir + "direction", "w")
        f.write("in")
        f.close()


class PinOut(Pin):

    def __init__(self, pinId):
        Pin.__init__(self, pinId)
        f = file(self.pinDir + "direction", "w")
        f.write("out")
        f.close()

    def set(self):
        f = file(self.pinDir + "value", "w")
        f.write("1")
        f.close()

    def clear(self):
        f = file(self.pinDir + "value", "w")
        f.write("0")
        f.close()

    def toggle(self):
        if self.state() == 1:
            self.clear()
        else:
            self.set()


class DigitalIO:

    def __init__(self):
        pass

    @staticmethod
    def get_input(pinId):
        return PinIn(pinId)

    @staticmethod
    def get_output(pinId):
        return PinOut(pinId)

    @staticmethod
    def release(self, pin):
        del pin

