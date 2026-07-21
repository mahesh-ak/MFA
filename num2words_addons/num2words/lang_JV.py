# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA

from __future__ import print_function, unicode_literals

class Num2Word_JV():
    BASE = {
        0: [],
        1: ["siji"],
        2: ["loro"],
        3: ["telu"],
        4: ["papat"],
        5: ["lima"],
        6: ["enem"],
        7: ["pitu"],
        8: ["wolu"],
        9: ["sanga"]
    }

    TENS_TO = {
        3: "ewu",          # ribu → ewu
        6: "yuta",         # juta → yuta
        9: "milyar",       # miliar → milyar
        12: "triliun",
        15: "kuadriliun",
        18: "kuintiliun",
        21: "sekstiliun",
        24: "septiliun",
        27: "oktiliun",
        30: "noniliun",
        33: "desiliun"
    }

    errmsg_floatord = "Ora bisa ngowahi angka pecahan dadi ordinal"
    errmsg_negord = "Ora bisa ngowahi angka negatif dadi ordinal"
    errmsg_toobig = "Angka kegedhen (abs(%s) > %s)."
    MAXVAL = 10 ** 36

    def split_by_koma(self, number):
        return str(number).split('.')

    def split_by_3(self, number):
        blocks = ()
        length = len(number)

        if length < 3:
            blocks += ((number,),)
        else:
            len_of_first_block = length % 3

            if len_of_first_block > 0:
                blocks += ((number[0:len_of_first_block],),)

            for i in range(len_of_first_block, length, 3):
                blocks += ((number[i:i + 3],),)

        return blocks

    def spell(self, blocks):
        word_blocks = ()
        first_block = blocks[0]

        if len(first_block[0]) == 1:
            if first_block[0] == '0':
                spelling = ['nol']
            else:
                spelling = self.BASE[int(first_block[0])]

        elif len(first_block[0]) == 2:
            spelling = self.puluh(first_block[0])

        else:
            spelling = (
                self.ratus(first_block[0][0]) +
                self.puluh(first_block[0][1:3])
            )

        word_blocks += (first_block[0], spelling),

        for block in blocks[1:]:
            spelling = self.ratus(block[0][0]) + self.puluh(block[0][1:3])
            word_blocks += (block[0], spelling),

        return word_blocks

    # --- hundreds ---
    def ratus(self, number):
        if number == '1':
            return ['satus']      # seratus → satus
        elif number == '0':
            return []
        else:
            return self.BASE[int(number)] + ['atus']   # dua ratus → loro atus

    # --- tens / teens ---
    def puluh(self, number):
        if number[0] == '1':
            if number[1] == '0':
                return ['sepuluh']   # stays same in Javanese
            elif number[1] == '1':
                return ['sewelas']   # sebelas → sewelas
            else:
                return self.BASE[int(number[1])] + ['welas']  # belas → welas

        elif number[0] == '0':
            return self.BASE[int(number[1])]
        
        elif number[0] == '8':
            return ['wolung', 'puluh'] + self.BASE[int(number[1])]

        else:
            return (
                self.BASE[int(number[0])] + ['puluh'] +
                self.BASE[int(number[1])]
            )

    # --- decimals ---
    def spell_float(self, float_part):
        word_list = []
        for n in float_part:
            if n == '0':
                word_list += ['nol']
            else:
                word_list += self.BASE[int(n)]
        return ' '.join(['', 'koma'] + word_list)

    def join(self, word_blocks, float_part):
        word_list = []
        length = len(word_blocks) - 1
        first_block = word_blocks[0],
        start = 0

        # 1000 special case
        if length == 1 and first_block[0][0] == '1':
            word_list += ['sewu']   # seribu → sewu
            start = 1

        for i in range(start, length + 1):
            word_list += word_blocks[i][1]
            if not word_blocks[i][1]:
                continue
            if i == length:
                break
            word_list += [self.TENS_TO[(length - i) * 3]]

        return ' '.join(word_list) + float_part

    def to_cardinal(self, number):
        if number >= self.MAXVAL:
            raise OverflowError(self.errmsg_toobig % (number, self.MAXVAL))

        minus = ''
        if number < 0:
            minus = 'minus '

        float_word = ''
        n = self.split_by_koma(abs(number))

        if len(n) == 2:
            float_word = self.spell_float(n[1])

        return minus + self.join(self.spell(self.split_by_3(n[0])), float_word)

    def to_ordinal(self, number):
        self.verify_ordinal(number)
        out_word = self.to_cardinal(number)

        if out_word == "siji":
            return "pisanan"   # pertama → pisanan

        return "ke-" + out_word

    def to_ordinal_num(self, number):
        self.verify_ordinal(number)
        return "ke-" + str(number)

    def to_currency(self, value):
        return self.to_cardinal(value) + " rupiah"

    def to_year(self, value):
        return self.to_cardinal(value)

    def verify_ordinal(self, value):
        if not value == int(value):
            raise TypeError(self.errmsg_floatord)
        if not abs(value) == value:
            raise TypeError(self.errmsg_negord)