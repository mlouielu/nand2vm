#
# Copyright (c) 2017 Louie Lu. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#

from typing import Sized


class BitArray(Sized):
    """This bitarray data is store with small endian, display with big endian"""
    DEFAULT_BITS = 16

    def __init__(self, source, endian=True):
        """endian -> True: big endian, False: small endian
        """
        self.data = []
        if isinstance(source, list):
            self.data = source[:]
        elif isinstance(source, str):
            self.data = [bool(int(s)) for s in source]
        elif isinstance(source, int):
            neg = False
            if source < 0:
                neg = True
                source = -source - 1

            self.data = [bool(int(s)) for s in bin(source)[2:].rjust(
                self.DEFAULT_BITS, '0')][::-1]

            if neg:
                self.data = self.__invert__().data
        else:
            raise NotImplementedError('Not support to convert %s to bitarray' % (
                                      type(source)))

        if endian and not isinstance(source, int):
            # Convert big endian to small endian
            self.data.reverse()

    def __getitem__(self, key):
        if isinstance(key, slice):
            return BitArray(self.data[key], endian=False)
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __repr__(self):
        """Display big endian for debugging"""
        if not isinstance(self.data[0], bool):
            # Assume this is a Bit
            return ''.join('1' if b.state else '0' for b in self.data[::-1])
        return ''.join(['1' if s else '0' for s in self.data[::-1]])

    def __len__(self) -> int:
        return len(self.data)

    def __eq__(self, other):
        if not isinstance(other, BitArray):
            raise NotImplementedError('Not support to compare with ', type(other))

        return self.data == other.data

    def __and__(self, other):
        if not isinstance(other, BitArray):
            raise NotImplementedError('Not support to & with ', type(other))

        return BitArray([a and b for a, b in zip(self.data, other.data)], False)

    def __or__(self, other):
        if not isinstance(other, BitArray):
            raise NotImplementedError('Not support to | with ', type(other))

        return BitArray([a or b for a, b in zip(self.data, other.data)], False)

    def __invert__(self):
        return BitArray([not a for a in self.data], False)
