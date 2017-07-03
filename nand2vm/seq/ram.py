#
# Copyright (c) 2017 Louie Lu. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#

from .clock import ClockPhase
from .register import Register
from .. import gate


class RAM8(object):
    def __init__(self):
        self.a = Register()
        self.b = Register()
        self.c = Register()
        self.d = Register()
        self.e = Register()
        self.f = Register()
        self.g = Register()
        self.h = Register()
        self.clock = ClockPhase.HIGH

    def update(self, soruce: BitArray, load: bool, select: BitArray,
                     clock: ClockPhase=None) -> BitArray:
