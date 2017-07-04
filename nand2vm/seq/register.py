#
# Copyright (c) 2017 Louie Lu. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#

from .bit import Bit
from .clock import ClockPhase
from .. import gate
from ..bitarray import BitArray


class Register(object):
    def __init__(self):
        self.bits = BitArray([Bit(), Bit(), Bit(), Bit(),
                              Bit(), Bit(), Bit(), Bit(),
                              Bit(), Bit(), Bit(), Bit(),
                              Bit(), Bit(), Bit(), Bit()])
        self.clock = ClockPhase.HIGH

    def update(self, source: BitArray, load: bool, clock: ClockPhase=None) -> BitArray:
        assert len(source) == 16

        if clock:
            self.clock = clock
        o1 = self.bits[0].update(source[0], load, clock=self.clock)
        o2 = self.bits[1].update(source[1], load, clock=self.clock)
        o3 = self.bits[2].update(source[2], load, clock=self.clock)
        o4 = self.bits[3].update(source[3], load, clock=self.clock)
        o5 = self.bits[4].update(source[4], load, clock=self.clock)
        o6 = self.bits[5].update(source[5], load, clock=self.clock)
        o7 = self.bits[6].update(source[6], load, clock=self.clock)
        o8 = self.bits[7].update(source[7], load, clock=self.clock)
        o9 = self.bits[8].update(source[8], load, clock=self.clock)
        o10 = self.bits[9].update(source[9], load, clock=self.clock)
        o11 = self.bits[10].update(source[10], load, clock=self.clock)
        o12 = self.bits[11].update(source[11], load, clock=self.clock)
        o13 = self.bits[12].update(source[12], load, clock=self.clock)
        o14 = self.bits[13].update(source[13], load, clock=self.clock)
        o15 = self.bits[14].update(source[14], load, clock=self.clock)
        o16 = self.bits[15].update(source[15], load, clock=self.clock)

        return BitArray([o1, o2, o3, o4, o5, o6, o7, o8,
                         o9, o10, o11, o12, o13, o14, o15, o16],
                         endian=False)
