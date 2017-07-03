#
# Copyright (c) 2017 Louie Lu. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#

from .. import gate
from ..bitarray import BitArray


def Not(a: bool) -> bool:
    return gate.Nand(a, a)


def Not16(a: BitArray) -> BitArray:
    assert len(a) == 16

    return BitArray([
        gate.Not(a[0]),
        gate.Not(a[1]),
        gate.Not(a[2]),
        gate.Not(a[3]),
        gate.Not(a[4]),
        gate.Not(a[5]),
        gate.Not(a[6]),
        gate.Not(a[7]),
        gate.Not(a[8]),
        gate.Not(a[9]),
        gate.Not(a[10]),
        gate.Not(a[11]),
        gate.Not(a[12]),
        gate.Not(a[13]),
        gate.Not(a[14]),
        gate.Not(a[15]),
    ], endian=False)
