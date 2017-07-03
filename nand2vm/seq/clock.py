#
# Copyright (c) 2017 Louie Lu. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#

from enum import Enum


class ClockPhase(Enum):
	LOW = 0
	POSITIVE_EDGE = 1
	HIGH = 2
	NEGATIVE_EDGE = 3
