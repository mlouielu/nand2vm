#
# Copyright (c) 2017 Louie Lu. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#

from collections import namedtuple
from enum import Enum


class DestMnemonic(Enum):
    null = '000'
    M = '001'
    D = '010'
    MD = '011'
    A = '100'
    AM = '101'
    AD = '110'
    AMD = '111'


Comp = namedtuple('Comp', ['a', 'c'])
CompMnemonic = {
    '0': Comp('0', '101010'),
    '1': Comp('0', '111111'),
    '-1': Comp('0', '111010'),
    'D': Comp('0', '001100'),
    'A': Comp('0', '110000'),
    '!D': Comp('0', '001101'),
    '!A': Comp('0', '110001'),
    '-D': Comp('0', '001111'),
    '-A': Comp('0', '110011'),
    'D+1': Comp('0', '011111'),
    'A+1': Comp('0', '110111'),
    'D-1': Comp('0', '001110'),
    'A-1': Comp('0', '110010'),
    'D+A': Comp('0', '000010'),
    'D-A': Comp('0', '010011'),
    'A-D': Comp('0', '000111'),
    'D&A': Comp('0', '000000'),
    'D|A': Comp('0', '010101'),
    'M': Comp('1', '110000'),
    '!M': Comp('1', '110001'),
    '-M': Comp('1', '110011'),
    'M+1': Comp('1', '110111'),
    'M-1': Comp('1', '110010'),
    'D+M': Comp('1', '000010'),
    'D-M': Comp('1', '010011'),
    'M-D': Comp('1', '000111'),
    'D&M': Comp('1', '000000'),
    'D|M': Comp('1', '010101')
}


class JumpMnemonic(Enum):
    null = '000'
    JGT = '001'
    JEQ = '010'
    JGE = '011'
    JLT = '100'
    JNE = '101'
    JLE = '110'
    JMP = '111'


class Assembler(object):

    def __init__(self):
        self.__pre_define_sym_table = {
            'R0': 0, 'R1': 1, 'R2': 2, 'R3': 3, 'R4': 4, 'R5': 5,
            'R6': 6, 'R7': 7, 'R8': 8, 'R9': 9, 'R10': 10, 'R11': 11,
            'R12': 12, 'R13': 13, 'R14': 14, 'R15': 15,
            'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3, 'THAT': 4,
            'SCREEN': 0x4000, 'KBD': 0x6000}
        self.sym_count = 16
        self.sym_table = self.__pre_define_sym_table
        self.label_table = {}
        self.instructions = []
        self.machine_code = []

    def binary(self, value, padding=0):
        return bin(value)[2:].rjust(padding, '0')

    def clean(self):
        self.sym_count = 16
        self.sym_table = self.__pre_define_sym_table
        self.label_table = {}
        self.instructions = []
        self.machine_code = []

    def read(self, path):
        self.clean()
        with open(path) as f:
            self.instructions = f.readlines()
        for index, inst in enumerate(self.instructions):
            self.instructions[index] = inst.strip('\n').replace(' ', '').split('//')[0]

        # Remove empty line
        self.instructions = list(filter(None, self.instructions))

    def parse(self):
        self.machine_code = []

        # Fetch label first
        for pc, inst in enumerate(self.instructions):
            if inst.startswith('(') and inst.endswith(')'):
                label = inst[1: -1]
                if label in self.label_table:
                    raise ValueError('Multiple defined label is not allowed')
                self.label_table[label] = pc - len(self.label_table)

        # Truly parsing
        for pc, inst in enumerate(self.instructions):
            if not inst:
                continue

            if inst.startswith('@'):
                # A-Instruction
                value = inst[1:]
                try:
                    value = int(value)
                except ValueError:
                    if value in self.label_table:
                        value = self.label_table[value]
                    elif value in self.sym_table:
                        value = self.sym_table[value]
                    else:
                        self.sym_table[value] = self.sym_count
                        value = self.sym_count
                        self.sym_count += 1

                value = self.binary(value, 15)
                self.machine_code.append('0' + value)
            elif inst.startswith('(') and inst.endswith(')'):
                # Label
                pass
            else:
                # C-Instruction
                if '=' in inst:
                    dest, comp = inst.split('=')
                    dest = getattr(DestMnemonic, dest)
                    comp = CompMnemonic[comp]
                    mc = '111' + comp.a + comp.c + dest.value + '000'
                elif ';' in inst:
                    comp, jump = inst.split(';')
                    comp = CompMnemonic[comp]
                    jump = getattr(JumpMnemonic, jump)
                    mc = '111' + comp.a + comp.c + '000' + jump.value
                self.machine_code.append(mc)


if __name__ == '__main__':
    asm = Assembler()
    asm.read('/tmp/nand2tetris/tools/a.asm')
    asm.parse()
    print(asm.instructions)
    print(asm.machine_code)
