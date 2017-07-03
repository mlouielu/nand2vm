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
            self.assertEqual(gate.add16(a, b), r)
