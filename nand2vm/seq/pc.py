#
# Copyright (c) 2017 Louie Lu. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#

from .. import gate, seq
from ..bitarray import BitArray


class PC(object):
    def __init__(self):
        self.register = seq.Register()

    def update(self, source, reset, load, inc, clock=None):
        reg = self.register.update(BitArray(0), False)
        plusone = gate.Inc16(reg)

        incmux = gate.Mux16(reg, plusone, inc)
        loadmux = gate.Mux16(incmux, source, load)
        resetmux = gate.Mux16(loadmux, gate.FALSE16, reset)
        out = self.register.update(resetmux, True, clock=clock)

        return out
