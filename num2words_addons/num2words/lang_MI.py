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


class Num2Word_MI():
    # Basic numbers
    BASE = {
        0: ["kore"],
        1: ["tahi"],
        2: ["rua"],
        3: ["toru"],
        4: ["whā"],
        5: ["rima"],
        6: ["ono"],
        7: ["whitu"],
        8: ["waru"],
        9: ["iwa"],
    }

    # Scale words
    TENS_TO = {
        3: "mano",
        6: "miriona",
        9: "piriona",
        12: "tiriona",
    }

    errmsg_floatord = "Cannot treat float number as ordinal"
    errmsg_negord = "Cannot treat negative number as ordinal"
    errmsg_toobig = "Number is too large to convert to words (abs(%s) > %s)."
    MAXVAL = 10 ** 36

    def split_by_koma(self, number):
        return str(number).split('.')

    def split_by_3(self, number):
        blocks = ()
        length = len(number)

        if length < 3:
            blocks += ((number,),)
        else:
            len_first = length % 3

            if len_first > 0:
                blocks += ((number[0:len_first],),)

            for i in range(len_first, length, 3):
                blocks += ((number[i:i + 3],),)

        return blocks

    def spell(self, blocks):
        word_blocks = ()

        for block in blocks:
            num = block[0].zfill(3)
            h, t, u = num

            words = []

            # Hundreds
            if h != '0':
                if h == '1':
                    words += ["kotahi", "rau"]
                else:
                    words += self.BASE[int(h)] + ["rau"]

            # Tens + ones
            if t != '0':
                if t == '1':
                    words += ["tekau"]
                else:
                    words += self.BASE[int(t)] + ["tekau"]

                if u != '0':
                    words += ["mā"] + self.BASE[int(u)]


            else:
                words += self.BASE[int(u)]


            word_blocks += (block[0], words),

        return word_blocks

    def spell_float(self, float_part):
        words = []
        for d in float_part:
            words += self.BASE[int(d)]
        return " ira " + " ".join(words)

    def join(self, word_blocks, float_part):
        word_list = []
        length = len(word_blocks) - 1

        for i in range(len(word_blocks)):
            block_words = word_blocks[i][1]
            block_val = int(word_blocks[i][0])
            if not (block_val or float_part):
                continue

            word_list += block_words

            scale_idx = (length - i) * 3
            if scale_idx in self.TENS_TO:
                # special case: 1 thousand = "kotahi mano"
                if int(word_blocks[i][0]) == 1:
                    word_list = word_list[:-len(block_words)] + ["kotahi", self.TENS_TO[scale_idx]]
                else:
                    word_list += [self.TENS_TO[scale_idx]]

        return " ".join(word_list) + float_part

    def to_cardinal(self, number):
        if number >= self.MAXVAL:
            raise OverflowError(self.errmsg_toobig % (number, self.MAXVAL))

        minus = ''
        if number < 0:
            minus = 'tāpirihanga '  # or "minus"

        float_word = ''
        n = self.split_by_koma(abs(number))

        if len(n) == 2:
            float_word = self.spell_float(n[1])

        return minus + self.join(self.spell(self.split_by_3(n[0])), float_word)

    def to_ordinal(self, number):
        self.verify_ordinal(number)
        return "te " + self.to_cardinal(number)

    def to_ordinal_num(self, number):
        self.verify_ordinal(number)
        return str(number)

    def to_currency(self, value):
        return self.to_cardinal(value) + " tāra"

    def to_year(self, value):
        return self.to_cardinal(value)

    def verify_ordinal(self, value):
        if not value == int(value):
            raise TypeError(self.errmsg_floatord % value)
        if not abs(value) == value:
            raise TypeError(self.errmsg_negord % value)