#
# Copyright (c) 2017 Louie Lu. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#

from .. import gate


def Xor(a: bool, b: bool):
    return gate.Or(
        gate.And(gate.Not(a), b),
        gate.And(a, gate.Not(b))
    )
