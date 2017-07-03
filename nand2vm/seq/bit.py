#
# Copyright (c) 2017 Louie Lu. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#

from .clock import ClockPhase
from .dff import DFF
from .. import gate


class Bit(object):
	def __init__(self):
		self.d = DFF()
		self.clock = ClockPhase.POSITIVE_EDGE

	def update(self, source: bool, load: bool, clock: ClockPhase=None) -> bool:
		if clock:
			self.clock = clock
		mux = gate.Mux(self.d.state, source, load)
		out = self.d.update(mux, self.clock)
		return out
