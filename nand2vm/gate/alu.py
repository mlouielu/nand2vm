#
# Copyright (c) 2017 Louie Lu. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#

from typing import List, Tuple
from .. import gate
from ..bitarray import BitArray


def ALU(x: BitArray, y: BitArray,
        zx: bool, nx: bool, zy: bool, ny: bool,
        f: bool, no: bool) -> Tuple[BitArray, bool, bool]:
    negx = gate.Not16(x)
    negy = gate.Not16(y)

    outx = gate.Mux4Way16(x, negx, gate.FALSE, gate.TRUE, select=BitArray([zx, nx]))
    outy = gate.Mux4Way16(y, negy, gate.FALSE, gate.TRUE, select=BitArray([zy, ny]))

    anded = gate.And16(outx, outy)
    added = gate.add16(outx, outy)
    result = gate.Mux16(anded, added, f)

    negresult = gate.Not16(result)
    out = gate.Mux16(result, negresult, no)

    out7 = out[:8]
    out14 = out[8: 16]
    ng = out[15]

    or7 = gate.Or8Way(out7)
    or14 = gate.Or8Way(out14)
    or714 = gate.Or(or7, or14)
    zr = gate.Not(or714)

    return (out, zr, ng)
