#
# Copyright (c) 2017 Louie Lu. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#

from .clock import ClockPhase
from .register import Register
from .. import gate
from ..bitarray import BitArray


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

    def update(self, source: BitArray, load: bool, address: BitArray,
               clock: ClockPhase=None) -> BitArray:
        assert len(source) == 16

        if clock:
            self.clock = clock
        al, bl, cl, dl, el, fl, gl, hl = gate.DMux8Way(load, address[:3])
        return gate.Mux8Way16(
            self.a.update(source, al, clock=self.clock),
            self.b.update(source, bl, clock=self.clock),
            self.c.update(source, cl, clock=self.clock),
            self.d.update(source, dl, clock=self.clock),
            self.e.update(source, el, clock=self.clock),
            self.f.update(source, fl, clock=self.clock),
            self.g.update(source, gl, clock=self.clock),
            self.h.update(source, hl, clock=self.clock),
            select=address[:3]
        )


class RAM64(object):

    def __init__(self):
        self.a = RAM8()
        self.b = RAM8()
        self.c = RAM8()
        self.d = RAM8()
        self.e = RAM8()
        self.f = RAM8()
        self.g = RAM8()
        self.h = RAM8()
        self.clock = ClockPhase.HIGH

    def update(self, source: BitArray, load: bool, address: BitArray,
               clock: ClockPhase=None) -> BitArray:
        assert len(source) == 16

        if clock:
            self.clock = clock
        al, bl, cl, dl, el, fl, gl, hl = gate.DMux8Way(load, address[:3])
        return gate.Mux8Way16(
            self.a.update(source, al, address[3: 6], clock=self.clock),
            self.b.update(source, bl, address[3: 6], clock=self.clock),
            self.c.update(source, cl, address[3: 6], clock=self.clock),
            self.d.update(source, dl, address[3: 6], clock=self.clock),
            self.e.update(source, el, address[3: 6], clock=self.clock),
            self.f.update(source, fl, address[3: 6], clock=self.clock),
            self.g.update(source, gl, address[3: 6], clock=self.clock),
            self.h.update(source, hl, address[3: 6], clock=self.clock),
            select=address[:3]
        )


class RAM512(object):

    def __init__(self):
        self.a = RAM64()
        self.b = RAM64()
        self.c = RAM64()
        self.d = RAM64()
        self.e = RAM64()
        self.f = RAM64()
        self.g = RAM64()
        self.h = RAM64()
        self.clock = ClockPhase.HIGH

    def update(self, source: BitArray, load: bool, address: BitArray,
               clock: ClockPhase=None) -> BitArray:
        assert len(source) == 16

        if clock:
            self.clock = clock
        al, bl, cl, dl, el, fl, gl, hl = gate.DMux8Way(load, address[:3])
        return gate.Mux8Way16(
            self.a.update(source, al, address[3: 9], clock=self.clock),
            self.b.update(source, bl, address[3: 9], clock=self.clock),
            self.c.update(source, cl, address[3: 9], clock=self.clock),
            self.d.update(source, dl, address[3: 9], clock=self.clock),
            self.e.update(source, el, address[3: 9], clock=self.clock),
            self.f.update(source, fl, address[3: 9], clock=self.clock),
            self.g.update(source, gl, address[3: 9], clock=self.clock),
            self.h.update(source, hl, address[3: 9], clock=self.clock),
            select=address[:3]
        )


class RAM4K(object):

    def __init__(self):
        self.a = RAM512()
        self.b = RAM512()
        self.c = RAM512()
        self.d = RAM512()
        self.e = RAM512()
        self.f = RAM512()
        self.g = RAM512()
        self.h = RAM512()
        self.clock = ClockPhase.HIGH

    def update(self, source: BitArray, load: bool, address: BitArray,
               clock: ClockPhase=None) -> BitArray:
        assert len(source) == 16

        if clock:
            self.clock = clock
        al, bl, cl, dl, el, fl, gl, hl = gate.DMux8Way(load, address[:3])
        return gate.Mux8Way16(
            self.a.update(source, al, address[3: 12], clock=self.clock),
            self.b.update(source, bl, address[3: 12], clock=self.clock),
            self.c.update(source, cl, address[3: 12], clock=self.clock),
            self.d.update(source, dl, address[3: 12], clock=self.clock),
            self.e.update(source, el, address[3: 12], clock=self.clock),
            self.f.update(source, fl, address[3: 12], clock=self.clock),
            self.g.update(source, gl, address[3: 12], clock=self.clock),
            self.h.update(source, hl, address[3: 12], clock=self.clock),
            select=address[:3]
        )


class RAM16K(object):

    def __init__(self):
        self.a = RAM4K()
        self.b = RAM4K()
        self.c = RAM4K()
        self.d = RAM4K()
        self.clock = ClockPhase.HIGH

    def update(self, source: BitArray, load: bool, address: BitArray,
               clock: ClockPhase=None) -> BitArray:
        assert len(source) == 16

        if clock:
            self.clock = clock
        al, bl, cl, dl = gate.DMux4Way(load, address[:2])
        return gate.Mux4Way16(
            self.a.update(source, al, address[2: 14], clock=self.clock),
            self.b.update(source, bl, address[2: 14], clock=self.clock),
            self.c.update(source, cl, address[2: 14], clock=self.clock),
            self.d.update(source, dl, address[2: 14], clock=self.clock),
            select=address[:2]
        )
