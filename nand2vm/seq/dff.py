#
# Copyright (c) 2017 Louie Lu. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#


from .. import gate
from .clock import ClockPhase


class DFF(object):
	def __init__(self):
		self._state = 0

	def update(self, source: bool, clock: ClockPhase) -> bool:
		prev_state = self._state
		if clock == ClockPhase.POSITIVE_EDGE:
			self._state = source
		return prev_state

	@property
	def state(self) -> bool:
		return self._state

	def __eq__(self, other):
		return self._state == other
