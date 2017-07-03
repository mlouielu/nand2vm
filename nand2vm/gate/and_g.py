#
# Copyright (c) 2017 Louie Lu. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#

from .. import gate
from ..bitarray import BitArray


def And(a: bool, b: bool) -> bool:
    return gate.Not(gate.Nand(a, b))


def And16(a: BitArray, b: BitArray) -> BitArray:
    assert len(a) == 16
    assert len(b) == 16

    return BitArray([
        gate.And(a[0], b[0]),
        gate.And(a[1], b[1]),
        gate.And(a[2], b[2]),
        gate.And(a[3], b[3]),
        gate.And(a[4], b[4]),
        gate.And(a[5], b[5]),
        gate.And(a[6], b[6]),
        gate.And(a[7], b[7]),
        gate.And(a[8], b[8]),
        gate.And(a[9], b[9]),
        gate.And(a[10], b[10]),
        gate.And(a[11], b[11]),
        gate.And(a[12], b[12]),
        gate.And(a[13], b[13]),
        gate.And(a[14], b[14]),
        gate.And(a[15], b[15])
    ], endian=False)
