#
# Copyright (c) 2017 Louie Lu. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#

import unittest
from nand2vm import gate, BitArray


class GateTest(unittest.TestCase):

    def test_nand_gate(self):
        self.assertEqual(gate.Nand(False, False), True)
        self.assertEqual(gate.Nand(False, True), True)
        self.assertEqual(gate.Nand(True, False), True)
        self.assertEqual(gate.Nand(True, True), False)

    def test_and_gate(self):
        self.assertEqual(gate.And(False, False), False)
        self.assertEqual(gate.And(False, True), False)
        self.assertEqual(gate.And(True, False), False)
        self.assertEqual(gate.And(True, True), True)

    def test_or_gate(self):
        self.assertEqual(gate.Or(False, False), False)
        self.assertEqual(gate.Or(False, True), True)
        self.assertEqual(gate.Or(True, False), True)
        self.assertEqual(gate.Or(True, True), True)

    def test_not_gate(self):
        self.assertEqual(gate.Not(False), True)
        self.assertEqual(gate.Not(True), False)

    def test_xor_gate(self):
        self.assertEqual(gate.Xor(False, False), False)
        self.assertEqual(gate.Xor(False, True), True)
        self.assertEqual(gate.Xor(True, False), True)
        self.assertEqual(gate.Xor(True, True), False)

    def test_mux_gate(self):
        self.assertEqual(gate.Mux(False, False, False), False)
        self.assertEqual(gate.Mux(False, False, True), False)
        self.assertEqual(gate.Mux(False, True, False), False)
        self.assertEqual(gate.Mux(False, True, True), True)
        self.assertEqual(gate.Mux(True, False, False), True)
        self.assertEqual(gate.Mux(True, False, True), False)
        self.assertEqual(gate.Mux(True, True, False), True)
        self.assertEqual(gate.Mux(True, True, True), True)

    def test_mux_16_gate(self):
        a = BitArray([True] * 16)
        b = BitArray([False] * 16)
        self.assertEqual(gate.Mux16(a, b, False), a)
        self.assertEqual(gate.Mux16(a, b, True), b)

        a = BitArray('1100110000101101')
        b = BitArray('0010101011001100')
        self.assertEqual(gate.Mux16(a, b, False), a)
        self.assertEqual(gate.Mux16(a, b, True), b)

    def test_mux4way16_gate(self):
        a = BitArray([True, True, False, False] * 4)
        b = BitArray([True, False, True, False] * 4)
        c = BitArray([False, True, False, True] * 4)
        d = BitArray([False, False, True, True] * 4)

        self.assertEqual(gate.Mux4Way16(a, b, c, d, BitArray([False, False])), a)
        self.assertEqual(gate.Mux4Way16(a, b, c, d, BitArray([False, True])), b)
        self.assertEqual(gate.Mux4Way16(a, b, c, d, BitArray([True, False])), c)
        self.assertEqual(gate.Mux4Way16(a, b, c, d, BitArray([True, True])), d)

    def test_mux8way16_gate(self):
        a = BitArray([True, True, True, True] * 4)
        b = BitArray([True, True, True, False] * 4)
        c = BitArray([True, True, False, True] * 4)
        d = BitArray([True, False, True, True] * 4)
        e = BitArray([False, True, True, True] * 4)
        f = BitArray([False, False, True, False] * 4)
        g = BitArray([False, True, False, True] * 4)
        h = BitArray([False, False, False, True] * 4)

        self.assertEqual(gate.Mux8Way16(a, b, c, d, e, f, g, h,
                                        BitArray([False, False, False])), a)
        self.assertEqual(gate.Mux8Way16(a, b, c, d, e, f, g, h,
                                        BitArray([False, False, True])), b)
        self.assertEqual(gate.Mux8Way16(a, b, c, d, e, f, g, h,
                                        BitArray([False, True, False])), c)
        self.assertEqual(gate.Mux8Way16(a, b, c, d, e, f, g, h,
                                        BitArray([False, True, True])), d)
        self.assertEqual(gate.Mux8Way16(a, b, c, d, e, f, g, h,
                                        BitArray([True, False, False])), e)
        self.assertEqual(gate.Mux8Way16(a, b, c, d, e, f, g, h,
                                        BitArray([True, False, True])), f)
        self.assertEqual(gate.Mux8Way16(a, b, c, d, e, f, g, h,
                                        BitArray([True, True, False])), g)
        self.assertEqual(gate.Mux8Way16(a, b, c, d, e, f, g, h,
                                        BitArray([True, True, True])), h)

    def test_dmux_gate(self):
        self.assertEqual(gate.DMux(False, False), (False, False))
        self.assertEqual(gate.DMux(False, True), (False, False))
        self.assertEqual(gate.DMux(True, False), (True, False))
        self.assertEqual(gate.DMux(True, True), (False, True))

    def test_dmux4way(self):
        # source: False
        self.assertEqual(gate.DMux4Way(False, BitArray([False, False])),
                         (False, False, False, False))
        self.assertEqual(gate.DMux4Way(False, BitArray([False, True])),
                         (False, False, False, False))
        self.assertEqual(gate.DMux4Way(False, BitArray([True, False])),
                         (False, False, False, False))
        self.assertEqual(gate.DMux4Way(False, BitArray([True, True])),
                         (False, False, False, False))
        # source: True
        self.assertEqual(gate.DMux4Way(True, BitArray([False, False])),
                         (True, False, False, False))
        self.assertEqual(gate.DMux4Way(True, BitArray([False, True])),
                         (False, True, False, False))
        self.assertEqual(gate.DMux4Way(True, BitArray([True, False])),
                         (False, False, True, False))
        self.assertEqual(gate.DMux4Way(True, BitArray([True, True])),
                         (False, False, False, True))

    def test_dmux8way(self):
        # source: False
        self.assertEqual(gate.DMux8Way(False, BitArray([False, False, False])),
                         (False, False, False, False, False, False, False, False))
        self.assertEqual(gate.DMux8Way(False, BitArray([False, False, True])),
                         (False, False, False, False, False, False, False, False))
        self.assertEqual(gate.DMux8Way(False, BitArray([False, True, False])),
                         (False, False, False, False, False, False, False, False))
        self.assertEqual(gate.DMux8Way(False, BitArray([False, True, True])),
                         (False, False, False, False, False, False, False, False))
        self.assertEqual(gate.DMux8Way(False, BitArray([True, False, False])),
                         (False, False, False, False, False, False, False, False))
        self.assertEqual(gate.DMux8Way(False, BitArray([True, False, True])),
                         (False, False, False, False, False, False, False, False))
        self.assertEqual(gate.DMux8Way(False, BitArray([True, True, False])),
                         (False, False, False, False, False, False, False, False))
        self.assertEqual(gate.DMux8Way(False, BitArray([True, True, True])),
                         (False, False, False, False, False, False, False, False))
        # source: True
        self.assertEqual(gate.DMux8Way(True, BitArray([False, False, False])),
                         (True, False, False, False, False, False, False, False))
        self.assertEqual(gate.DMux8Way(True, BitArray([False, False, True])),
                         (False, True, False, False, False, False, False, False))
        self.assertEqual(gate.DMux8Way(True, BitArray([False, True, False])),
                         (False, False, True, False, False, False, False, False))
        self.assertEqual(gate.DMux8Way(True, BitArray([False, True, True])),
                         (False, False, False, True, False, False, False, False))
        self.assertEqual(gate.DMux8Way(True, BitArray([True, False, False])),
                         (False, False, False, False, True, False, False, False))
        self.assertEqual(gate.DMux8Way(True, BitArray([True, False, True])),
                         (False, False, False, False, False, True, False, False))
        self.assertEqual(gate.DMux8Way(True, BitArray([True, True, False])),
                         (False, False, False, False, False, False, True, False))
        self.assertEqual(gate.DMux8Way(True, BitArray([True, True, True])),
                         (False, False, False, False, False, False, False, True))

    def test_and_16_gate(self):
        t = BitArray([True] * 16)
        f = BitArray([False] * 16)

        self.assertEqual(len(gate.And16(f, f)), 16)
        self.assertEqual(gate.And16(f, f), f)
        self.assertEqual(gate.And16(t, f), f)
        self.assertEqual(gate.And16(f, t), f)
        self.assertEqual(gate.And16(t, t), t)

        a = BitArray('1100110000101101')
        b = BitArray('0010101011001100')
        r = BitArray('0000100000001100')
        self.assertEqual(gate.And16(a, b), a & b)
        self.assertEqual(gate.And16(a, b), r)

    def test_or_16_gate(self):
        t = BitArray([True] * 16)
        f = BitArray([False] * 16)

        self.assertEqual(len(gate.Or16(f, f)), 16)
        self.assertEqual(gate.Or16(f, f), f)
        self.assertEqual(gate.Or16(t, f), t)
        self.assertEqual(gate.Or16(f, t), t)
        self.assertEqual(gate.Or16(t, t), t)

        a = BitArray('1100110000101101')
        b = BitArray('0010101011001100')
        r = BitArray('1110111011101101')
        self.assertEqual(gate.Or16(a, b), a | b)
        self.assertEqual(gate.Or16(a, b), r)

    def test_not_16_gate(self):
        t = BitArray([True] * 16)
        f = BitArray([False] * 16)

        self.assertEqual(len(gate.Not16(f)), 16)
        self.assertEqual(gate.Not16(f), t)
        self.assertEqual(gate.Not16(t), f)

        a = BitArray('1100110000101101')
        r = BitArray('0011001111010010')
        self.assertEqual(gate.Not16(a), ~a)
        self.assertEqual(gate.Not16(a), r)

    def test_or8way_gate(self):
        a = BitArray('00001000')
        self.assertEqual(gate.Or8Way(a), True)

        a = BitArray('00000000')
        self.assertEqual(gate.Or8Way(a), False)

        a = BitArray('11111111')
        self.assertEqual(gate.Or8Way(a), True)

        a = BitArray('10101100')
        self.assertEqual(gate.Or8Way(a), True)


class AdderTest(unittest.TestCase):

    def test_half_adder(self):
        self.assertEqual(gate.ha(False, False), (False, False))
        self.assertEqual(gate.ha(False, True), (True, False))
        self.assertEqual(gate.ha(True, False), (True, False))
        self.assertEqual(gate.ha(True, True), (False, True))

    def test_full_adder(self):
        self.assertEqual(gate.fa(False, False, False), (False, False))
        self.assertEqual(gate.fa(False, False, True), (True, False))
        self.assertEqual(gate.fa(False, True, False), (True, False))
        self.assertEqual(gate.fa(False, True, True), (False, True))
        self.assertEqual(gate.fa(True, False, False), (True, False))
        self.assertEqual(gate.fa(True, False, True), (False, True))
        self.assertEqual(gate.fa(True, True, False), (False, True))
        self.assertEqual(gate.fa(True, True, True), (True, True))

    def test_add16(self):
        a_input = [
            '0000000000000000',
            '0000000000000000',
            '1111111111111111',
            '1010101010101010',
            '0011110011000011',
            '0001001000110100'
        ]

        b_input = [
            '0000000000000000',
            '1111111111111111',
            '1111111111111111',
            '0101010101010101',
            '0000111111110000',
            '1001100001110110'
        ]

        results = [
            '0000000000000000',
            '1111111111111111',
            '1111111111111110',
            '1111111111111111',
            '0100110010110011',
            '1010101010101010'
        ]

        for a, b, r in zip(a_input, b_input, results):
            a = BitArray(a)
            b = BitArray(b)
            r = BitArray(r)
            self.assertEqual(gate.Add16(a, b), r)

    def test_inc16(self):
        self.assertEqual(gate.Inc16(BitArray('0000000000000000')),
                         BitArray('0000000000000001'))
        self.assertEqual(gate.Inc16(BitArray('1111111111111111')),
                         BitArray('0000000000000000'))
        self.assertEqual(gate.Inc16(BitArray('0000000000000101')),
                         BitArray('0000000000000110'))
        self.assertEqual(gate.Inc16(BitArray('1111111111111011')),
                         BitArray('1111111111111100'))
