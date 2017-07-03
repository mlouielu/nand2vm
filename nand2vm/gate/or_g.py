#
# Copyright (c) 2017 Louie Lu. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#

from .. import gate
from ..bitarray import BitArray


def Or(a: bool, b: bool) -> bool:
    return gate.Not(gate.And(gate.Not(a), gate.Not(b)))


def Or16(a: BitArray, b: BitArray) -> BitArray:
    assert len(a) == 16
    assert len(b) == 16

    return BitArray([
        gate.Or(a[0], b[0]),
        gate.Or(a[1], b[1]),
        gate.Or(a[2], b[2]),
        gate.Or(a[3], b[3]),
        gate.Or(a[4], b[4]),
        gate.Or(a[5], b[5]),
        gate.Or(a[6], b[6]),
        gate.Or(a[7], b[7]),
        gate.Or(a[8], b[8]),
        gate.Or(a[9], b[9]),
        gate.Or(a[10], b[10]),
        gate.Or(a[11], b[11]),
        gate.Or(a[12], b[12]),
        gate.Or(a[13], b[13]),
        gate.Or(a[14], b[14]),
        gate.Or(a[15], b[15])
    ], endian=False)


def Or8Way(a: BitArray) -> bool:
    assert len(a) == 8

    a2 = gate.Or(a[0], a[1])
    a4 = gate.Or(a[2], a[3])
    a6 = gate.Or(a[4], a[5])
    a8 = gate.Or(a[6], a[7])
    a24 = gate.Or(a2, a4)
    a68 = gate.Or(a6, a8)

    return gate.Or(a24, a68)
