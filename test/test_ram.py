#
# Copyright (c) 2017 Louie Lu. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#

import sys
import os
import unittest
from collections import namedtuple
from nand2vm import seq, BitArray
from . import DATA_DIRECTORY


class RAMTest(object):
    DATA = namedtuple('Data', ['clock', 'source', 'load', 'address', 'out', 'time'])

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
                row[3] = BitArray(int(row[3]))
                row[4] = BitArray(int(row[4]))
                row.append(int(t.split('+')[0]))
                data.append(self.DATA(*row))
        return data

    def test_ram(self):
        data = self.prepare_data(os.path.join(DATA_DIRECTORY, self.CMP_DATA))
        for d in data:
            out = self.ram.update(d.source, d.load, d.address, clock=d.clock)
            self.assertEqual(out, d.out, d)


class RAM8Test(unittest.TestCase, RAMTest):
    RAM = seq.RAM8
    CMP_DATA = 'RAM8.cmp'
    ram = RAM()


class RAM64Test(unittest.TestCase, RAMTest):
    RAM = seq.RAM64
    CMP_DATA = 'RAM64.cmp'
    ram = RAM()


class RAM512Test(unittest.TestCase, RAMTest):
    RAM = seq.RAM512
    CMP_DATA = 'RAM512.cmp'
    ram = RAM()


class RAM4KTest(unittest.TestCase, RAMTest):
    RAM = seq.RAM4K
    CMP_DATA = 'RAM4K.cmp'
    ram = RAM()


class RAM16KTest(unittest.TestCase, RAMTest):
    RAM = seq.RAM16K
    CMP_DATA = 'RAM16K.cmp'
    ram = RAM()
