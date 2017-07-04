#
# Copyright (c) 2017 Louie Lu. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#

from .. import gate
from ..bitarray import BitArray

TRUE16 = BitArray(2 ** BitArray.DEFAULT_BITS - 1)
FALSE16 = BitArray(0)
