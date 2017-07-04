#
# Copyright (c) 2017 Louie Lu. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#


from .. import gate
from .. import seq
from ..bitarray import BitArray


class CPU(object):

    def __init__(self):
        self.alu_out = gate.FALSE16
        self.pc = seq.PC()
        self.a = seq.Register()
        self.d = seq.Register()
        self.clock = seq.ClockPhase.HIGH

    def evaluate(self, inM: BitArray, instruction: BitArray, reset: bool, clock=None):
        assert len(inM) == 16
        assert len(instruction) == 16

        a_inst = gate.Not(instruction[15])
        c_inst = gate.Not(a_inst)

        alu_to_a = gate.And(c_inst, instruction[5])
        a_reg_in = gate.Mux16(instruction, self.alu_out, alu_to_a)

        load_a = gate.Or(a_inst, alu_to_a)
        a_out = self.a.update(a_reg_in, load_a, clock=clock)

        am_out = gate.Mux16(a_out, inM, select=instruction[12])

        load_d = gate.And(c_inst, instruction[4])
        d_out = self.d.update(self.alu_out, load_d)

        self.alu_out, zr_out, ng_out = gate.ALU(
            d_out, am_out, instruction[11], instruction[10],
            instruction[9], instruction[8], instruction[7],
            instruction[6])

        address_m = gate.Or16(gate.FALSE16, a_out)
        out_m = gate.Or16(gate.FALSE16, self.alu_out)
        write_m = gate.And(c_inst, instruction[3])

        jeq = gate.And(zr_out, instruction[1])
        jlt = gate.And(ng_out, instruction[2])
        zr_or_ng = gate.Or(zr_out, ng_out)
        positive = gate.Not(zr_or_ng)
        jgt = gate.And(positive, instruction[0])
        jle = gate.Or(jeq, jlt)
        jump_to_a = gate.Or(jle, jgt)
        pc_load = gate.And(c_inst, jump_to_a)
        pc_inc = gate.Not(pc_load)

        pc = self.pc.update(a_out, pc_inc, pc_load, reset, clock=clock)

        return (out_m, write_m, address_m, pc)
