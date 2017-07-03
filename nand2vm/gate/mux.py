#
# Copyright (c) 2017 Louie Lu. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#

from typing import List
from .. import gate
from ..bitarray import BitArray


def Mux(a: bool, b: bool, select: bool):
    return gate.Or(
        gate.And(a, gate.Not(select)),
        gate.And(b, select)
    )


def Mux16(a: List[bool], b: List[bool], select: bool) -> List[bool]:
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
    ])


def Mux4Way16(a: List[bool], b: List[bool], c: List[bool], d: List[bool],
              select: List[bool]):
    """4 way 16 bit multiplexor requiring 2 control inputs

    select[1]   select[0]  | out
       0           0       | a
       0           1       | b
       1           0       | c
       1           1       | d
    """
    q = gate.Mux16(a, b, select[0])
    r = gate.Mux16(c, d, select[0])
    return gate.Mux16(q, r, select[1])


def Mux8Way16(a: List[bool], b: List[bool], c: List[bool], d: List[bool],
              e: List[bool], f: List[bool], g: List[bool], h: List[bool],
              select: List[bool]):
    pass
