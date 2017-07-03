#
# Copyright (c) 2017 Louie Lu. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#

import unittest
from nand2vm import BitArray


class BitArrayTest(unittest.TestCase):
    def test_init_with_list(self):
        source = [True, True, False, False, True]

        b = BitArray(source, endian=True)
        self.assertEqual(b.data, source[::-1])

        b = BitArray(source, endian=False)
        self.assertEqual(b.data, source)

    def test_init_with_str(self):
        source = '11001'

        b = BitArray(source, endian=True)
        self.assertEqual(b.data, [True, False, False, True, True])

        b = BitArray(source, endian=False)
        self.assertEqual(b.data, [True, True, False, False, True])

    def test_init_with_int(self):
        source = 13

        b = BitArray(source, endian=True)
        self.assertEqual(b.data,
                         [True, False, True, True, False, False, False, False,
                          False, False, False, False, False, False, False, False])

        b = BitArray(source, endian=False)
        self.assertEqual(b.data,
                         [True, False, True, True, False, False, False, False,
                          False, False, False, False, False, False, False, False])

    def test_len(self):
        self.assertEqual(len(BitArray('110')), 3)

    def test_slice(self):
        source = [True, True, False, True]
        b = BitArray(source)

        self.assertIsInstance(b[:2], BitArray)
        self.assertEqual(b[:2], BitArray([False, True]))

        self.assertIsInstance(b[2:], BitArray)
        self.assertEqual(b[2:], BitArray([True, True]))
