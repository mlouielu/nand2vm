#
# Copyright (c) 2017 Louie Lu. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#

import os
import unittest
from collections import namedtuple
from nand2vm import seq, BitArray
from . import DATA_DIRECTORY


class DFFTest(unittest.TestCase):
    def setUp(self):
        self.d = seq.DFF()

    def test_dff(self):
        self.assertEqual(self.d.update(True, seq.ClockPhase.LOW), False)
        self.assertEqual(self.d.update(True, seq.ClockPhase.POSITIVE_EDGE), False)
        self.assertEqual(self.d.update(False, seq.ClockPhase.NEGATIVE_EDGE), True)
        self.assertEqual(self.d.update(False, seq.ClockPhase.HIGH), True)
        self.assertEqual(self.d.update(False, seq.ClockPhase.POSITIVE_EDGE), True)
        self.assertEqual(self.d.update(True, seq.ClockPhase.HIGH), False)
        self.assertEqual(self.d.state, False)


class BitTest(unittest.TestCase):
    DATA = namedtuple('Data', ['time', 'source', 'load', 'out'])

    def prepare_data(self, path):
        data = []
        with open(path) as f:
            f.readline()
            for row in f.readlines():
                row = row.strip('\n').split('|')
                row[0] = seq.ClockPhase.POSITIVE_EDGE if row[0].endswith('+') else seq.ClockPhase.HIGH
                row[1] = bool(int(row[1]))
                row[2] = bool(int(row[2]))
                row[3] = bool(int(row[3]))
                data.append(self.DATA(*row))
        return data

    def setUp(self):
        self.bit = seq.Bit()

    def test_bit(self):
        data = self.prepare_data(os.path.join(DATA_DIRECTORY, 'Bit.cmp'))
        for d in data:
            out = self.bit.update(d.source, d.load, clock=d.time)
            self.assertEqual(out, d.out)


class RegisterTest(unittest.TestCase):
    DATA = namedtuple('Data', ['time', 'source', 'load', 'out'])

    def prepare_data(self, path):
        data = []
        with open(path) as f:
            f.readline()
            for row in f.readlines():
                row = row.strip('\n').split('|')
                row[0] = seq.ClockPhase.POSITIVE_EDGE if row[0].endswith('+') else seq.ClockPhase.HIGH
                row[1] = BitArray(int(row[1]))
                row[2] = bool(int(row[2]))
                row[3] = BitArray(int(row[3]))
                data.append(self.DATA(*row))
        return data

    def setUp(self):
        self.register = seq.Register()

    def test_register(self):
        data = self.prepare_data(os.path.join(DATA_DIRECTORY, 'Register.cmp'))
        for d in data:
            out = self.register.update(d.source, d.load, clock=d.time)
            self.assertEqual(out, d.out)


class PCTest(unittest.TestCase):
    DATA = namedtuple('Data', ['clock', 'source', 'reset', 'load', 'inc', 'out', 'time'])

    def prepare_data(self, path):
        data = []
        with open(path) as f:
            f.readline()
            for row in f.readlines():
                row = row.strip('\n').split('|')
                t = row[0]
                row[0] = seq.ClockPhase.POSITIVE_EDGE if t.endswith('+') else seq.ClockPhase.HIGH
                row[1] = BitArray(int(row[1]))
                row[2] = bool(int(row[2]))
                row[3] = bool(int(row[3]))
                row[4] = bool(int(row[4]))
                row[5] = BitArray(int(row[5]))
                row.append(int(t.split('+')[0]))
                data.append(self.DATA(*row))
        return data

    def setUp(self):
        self.pc = seq.PC()

    def test_pc(self):
        data = self.prepare_data(os.path.join(DATA_DIRECTORY, 'PC.cmp'))
        for d in data:
            out = self.pc.update(d.source, d.reset, d.load, d.inc, clock=d.clock)
            self.assertEqual(out, d.out, d)
