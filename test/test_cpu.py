#
# Copyright (c) 2017 Louie Lu. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#

import os
import unittest
from collections import namedtuple
from . import DATA_DIRECTORY
from nand2vm import arch, seq, BitArray


class CPUTest(unittest.TestCase):
    DATA = namedtuple('Data', ['time', 'inM', 'instruction', 'reset', 'outM',
                               'writeM', 'addr', 'pc', 'DRegiste', 'clock'])

    def prepare_data(self, path):
        data = []
        with open(path) as f:
            f.readline()
            for row in f.readlines():
                row = row.strip('\n').split('|')
                t = row[0]
                row[0] = seq.ClockPhase.POSITIVE_EDGE if t.endswith('+') else seq.ClockPhase.HIGH
                row[1] = BitArray(int(row[1]))
                row[2] = BitArray(row[2])
                row[3] = bool(int(row[3]))
                row[4] = BitArray(int(0 if row[4] == '*******' else row[4]))
                row[5] = bool(int(row[5]))
                row[6] = BitArray(int(row[6]))
                row[7] = BitArray(int(row[7]))
                row[8] = BitArray(int(row[8]))
                row.append(int(t.split('+')[0]))
                data.append(self.DATA(*row))
        return data

    def setUp(self):
        self.cpu = arch.CPU()

    def test_bit(self):
        data = self.prepare_data(os.path.join(DATA_DIRECTORY, 'CPU.cmp'))
        for index, d in enumerate(data):
            out, write, addr, pc = self.cpu.evaluate(d.inM, d.instruction, d.reset, clock=d.clock)
            self.assertEqual(out, d.outM, index)
            self.assertEqual(write, d.writeM, index)
            self.assertEqual(addr, d.addr, index)
            self.assertEqual(pc, d.pc, index)
