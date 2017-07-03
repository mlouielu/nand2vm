#
# Copyright (c) 2017 Louie Lu. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#

import csv
import os
import unittest
from collections import namedtuple
from nand2vm import gate, BitArray


PACKAGE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
DATA_DIRECTORY = os.path.join(PACKAGE_DIRECTORY, 'data')


class ALUTest(unittest.TestCase):
    DATA = namedtuple('Data', ['x', 'y', 'zx', 'nx', 'zy', 'ny', 'f', 'no', 'out', 'zr', 'ng'])

    @classmethod
    def make_data(cls, data):
        data[0] = BitArray(data[0])
        data[1] = BitArray(data[1])
        data[2] = bool(int(data[2]))
        data[3] = bool(int(data[3]))
        data[4] = bool(int(data[4]))
        data[5] = bool(int(data[5]))
        data[6] = bool(int(data[6]))
        data[7] = bool(int(data[7]))
        data[8] = BitArray(data[8])
        data[9] = bool(int(data[9]))
        data[10] = bool(int(data[10]))

        return cls.DATA(*data)

    @classmethod
    def setUpClass(cls):
        with open(os.path.join(DATA_DIRECTORY, 'ALU.cmp'), newline='') as f:
            reader = csv.reader(f, delimiter='|')
            next(reader)
            cls.cases = [case for case in map(cls.make_data, reader)]

    def test_alu(self):
        for index, case in enumerate(self.cases):
            with self.subTest(caseid=index, zr=case.zr, ng=case.ng, out=case.out):
                out, zr, ng = gate.ALU(case.x, case.y, case.zx, case.nx,
                                       case.zy, case.ny, case.f, case.no)
                self.assertEqual(out, case.out)
                self.assertEqual(zr, case.zr)
                self.assertEqual(ng, case.ng)
