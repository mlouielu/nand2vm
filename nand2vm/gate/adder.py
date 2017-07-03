#
# Copyright (c) 2017 Louie Lu. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#

from typing import Tuple
from .. import gate
from ..bitarray import BitArray


def ha(a: bool, b: bool) -> Tuple[bool, bool]:
    """Return (sum, carry)"""
    return (
        gate.Xor(a, b),
        gate.And(a, b)
    )


def fa(a: bool, b: bool, c: bool) -> Tuple[bool, bool]:
    """Return (sum, carry)"""
    s1, c1 = gate.ha(a, b)
    s2, c2 = gate.ha(s1, c)
    return (s2, gate.Or(c1, c2))


def Add16(a: BitArray, b: BitArray) -> BitArray:
    assert len(a) == 16
    assert len(b) == 16

    s1, c1 = gate.fa(a[0], b[0], False)
    s2, c2 = gate.fa(a[1], b[1], c1)
    s3, c3 = gate.fa(a[2], b[2], c2)
    s4, c4 = gate.fa(a[3], b[3], c3)
    s5, c5 = gate.fa(a[4], b[4], c4)
    s6, c6 = gate.fa(a[5], b[5], c5)
    s7, c7 = gate.fa(a[6], b[6], c6)
    s8, c8 = gate.fa(a[7], b[7], c7)
    s9, c9 = gate.fa(a[8], b[8], c8)
    s10, c10 = gate.fa(a[9], b[9], c9)
    s11, c11 = gate.fa(a[10], b[10], c10)
    s12, c12 = gate.fa(a[11], b[11], c11)
    s13, c13 = gate.fa(a[12], b[12], c12)
    s14, c14 = gate.fa(a[13], b[13], c13)
    s15, c15 = gate.fa(a[14], b[14], c14)
    s16, c16 = gate.fa(a[15], b[15], c15)

    return BitArray([
        s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16],
        endian=False)
