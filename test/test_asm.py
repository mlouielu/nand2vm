#
# Copyright (c) 2017 Louie Lu. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#

import os
import unittest
from . import DATA_DIRECTORY
from nand2vm import assembler


class AssemblerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import glob
        cls.asms = glob.glob(os.path.join(DATA_DIRECTORY, 'ASM', '*.asm'))
        cls.hacks = glob.glob(os.path.join(DATA_DIRECTORY, 'ASM', '*.hack'))
        cls.filenames = [path.split('/')[-1].split('.')[0] for path in cls.asms]

    def find_file(self, filename):
        for asm in self.asms:
            if filename == asm.split('/')[-1].split('.')[0]:
                break
        for hack in self.hacks:
            if filename in hack.split('/')[-1].split('.')[0]:
                break
        return asm, hack

    def read_hack(self, path):
        with open(path) as f:
            return [l.strip('\n') for l in f.readlines()]

    def test_asm(self):
        asmer = assembler.Assembler()
        for filename in self.filenames:
            asm, hack = self.find_file(filename)
            with self.subTest(filename=filename):
                asmer.read(asm)
                asmer.parse()
                self.assertEqual(asmer.machine_code, self.read_hack(hack))
