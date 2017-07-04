#
# Copyright (c) 2017 Louie Lu. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#

from typing import Tuple
from .. import gate
from ..bitarray import BitArray


def Mux(a: bool, b: bool, select: bool):
    return gate.Or(
        gate.And(a, gate.Not(select)),
        gate.And(b, select)
    )


def Mux16(a: BitArray, b: BitArray, select: bool) -> BitArray:
    assert len(a) == 16
    assert len(b) == 16

    return BitArray([
        gate.Mux(a[0], b[0], select),
        gate.Mux(a[1], b[1], select),
        gate.Mux(a[2], b[2], select),
        gate.Mux(a[3], b[3], select),
        gate.Mux(a[4], b[4], select),
        gate.Mux(a[5], b[5], select),
        gate.Mux(a[6], b[6], select),
        gate.Mux(a[7], b[7], select),
        gate.Mux(a[8], b[8], select),
        gate.Mux(a[9], b[9], select),
        gate.Mux(a[10], b[10], select),
        gate.Mux(a[11], b[11], select),
        gate.Mux(a[12], b[12], select),
        gate.Mux(a[13], b[13], select),
        gate.Mux(a[14], b[14], select),
        gate.Mux(a[15], b[15], select)
    ], endian=False)


def Mux4Way16(a: BitArray, b: BitArray, c: BitArray, d: BitArray,
              select: BitArray) -> BitArray:
    """4 way 16 bit multiplexor requiring 2 control inputs

    select[1]   select[0]  | out
       0           0       | a
       0           1       | b
       1           0       | c
       1           1       | d
    """
    assert len(a) == 16
    assert len(b) == 16
    assert len(c) == 16
    assert len(d) == 16
    assert len(select) == 2

    q = gate.Mux16(a, b, select[0])
    r = gate.Mux16(c, d, select[0])
    return gate.Mux16(q, r, select[1])


def Mux8Way16(a: BitArray, b: BitArray, c: BitArray, d: BitArray,
              e: BitArray, f: BitArray, g: BitArray, h: BitArray,
              select: BitArray) -> BitArray:
    assert len(a) == 16
    assert len(b) == 16
    assert len(c) == 16
    assert len(d) == 16
    assert len(e) == 16
    assert len(f) == 16
    assert len(g) == 16
    assert len(h) == 16
    assert len(select) == 3

    ab = gate.Mux16(a, b, select[0])
    cd = gate.Mux16(c, d, select[0])
    ef = gate.Mux16(e, f, select[0])
    gh = gate.Mux16(g, h, select[0])
    abcd = gate.Mux16(ab, cd, select[1])
    efgh = gate.Mux16(ef, gh, select[1])

    return gate.Mux16(abcd, efgh, select[2])


def DMux(source: bool, select: bool) -> Tuple[bool, bool]:
    return (
        gate.Mux(source, False, select),
        gate.Mux(False, source, select)
    )


def DMux4Way(source: bool, select: BitArray) -> Tuple[bool, bool, bool, bool]:
    assert len(select) == 2

    t1, t2 = gate.DMux(source, select[1])
    a, b = gate.DMux(t1, select[0])
    c, d = gate.DMux(t2, select[0])
    return (a, b, c, d)


def DMux8Way(source: bool, select: BitArray) -> Tuple[bool, bool, bool, bool,
                                                      bool, bool, bool, bool]:
    assert len(select) == 3

    t1, t2, t3, t4 = gate.DMux4Way(source, select[1:])
    a, b = gate.DMux(t1, select[0])
    c, d = gate.DMux(t2, select[0])
    e, f = gate.DMux(t3, select[0])
    g, h = gate.DMux(t4, select[0])
    return (a, b, c, d, e, f, g, h)
