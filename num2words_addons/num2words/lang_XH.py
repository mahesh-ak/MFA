# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.
# Copyright (c) 2018, Abdullah Alhazmy, Alhazmy13.  All Rights Reserved.
# Copyright (c) 2020, Hamidreza Kalbasi.  All Rights Reserved.
# Copyright (c) 2023, Nika Soltani Tehrani.  All Rights Reserved.

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

from decimal import Decimal
from math import floor


xhosaOnes = [
    "", "nye", "zimbini", "zintathu", "zine", "zintlanu", "zintandathu",
    "zisixhenxe", "zisibhozo", "zisithoba",
    "lishumi",
    "lishumi elinanye",
    "lishumi elinesibini",
    "lishumi elinesithathu",
    "lishumi elinesine",
    "lishumi elinesihlanu",
    "lishumi elinesithandathu",
    "lishumi elinesixhenxe",
    "lishumi elinesibhozo",
    "lishumi elinesithoba",
]

xhosaTens = [
    "",
    "lishumi",
    "amashumi amabini",
    "amashumi amathathu",
    "amashumi amane",
    "amashumi amahlanu",
    "amashumi amathandathu",
    "amashumi asixhenxe",
    "amashumi asibhozo",
    "amashumi asithoba",
]

xhosaHundreds = [
    "",
    "ikhulu elinye",
    "amakhulu amabini",
    "amakhulu amathathu",
    "amakhulu amane",
    "amakhulu amahlanu",
    "amakhulu amathandathu",
    "amakhulu asixhenxe",
    "amakhulu asibhozo",
    "amakhulu asithoba",
]

xhosaBig = [
    '',
    'iwaka',
    'isigidi',
    'ibhiliyoni',
    'ithriliyoni',
]


class Num2Word_XH(object):

    errmsg_toobig = "Too large"
    MAXNUM = 10 ** 36

    def __init__(self):
        self.number = 0

    # --- Xhosa assimilation ---
    def assimilate(self, word):
        mapping = {
            "enye": "nye",
            "zimbini": "mbini",
            "lishumi": "eshumi",
            "zintathu": "ntathu",
            "zine": "ne",
            "zintlanu": "ntlanu",
            "zintandathu": "ntandathu",
            "zisixhenxe": "sixhenxe",
            "zisibhozo": "sibhozo",
            "zisithoba": "sithoba",
        }
        return mapping.get(word, word)


    # --- phonological join ---
    def join_na(self, a, b):
        parts = b.split()
        first = self.assimilate(parts[0])
        sep = " na"
        if first[0] in ['a', 'e', 'o']:
            sep = " n"
        rest = " ".join([first] + parts[1:])

        # Xhosa: almost always "na" (NOT "no")
        return a + sep + rest

    def float2tuple(self, value):
        pre = int(value)
        self.precision = abs(Decimal(str(value)).as_tuple().exponent)

        post = abs(value - pre) * 10**self.precision
        if abs(round(post) - post) < 0.01:
            post = int(round(post))
        else:
            post = int(floor(post))
        return pre, post, self.precision

    def cardinal3(self, number):
        if number <= 19:
            return xhosaOnes[number]

        if number < 100:
            x, y = divmod(number, 10)
            if y == 0:
                return xhosaTens[x]

            # special: second part uses "ane-"
            ones = self.assimilate(xhosaOnes[y])
            return xhosaTens[x] + " ane" + ones

        x, y = divmod(number, 100)
        if y == 0:
            return xhosaHundreds[x]

        return self.join_na(xhosaHundreds[x], self.cardinal3(y))

    def cardinalPos(self, number):
        x = number
        res = ''

        for b in xhosaBig:
            x, y = divmod(x, 1000)
            if y == 0:
                continue

            # --- number part ---
            if y == 1:
                num = "enye"
            else:
                num = self.cardinal3(y)

            # --- group logic ---
            if b == '':
                yx = num

            elif b == 'iwaka':
                if y == 1:
                    yx = "iwaka elinye"
                else:
                    yx = "amawaka " + num

            else:
                # plural for >1
                if y == 1:
                    yx = b + " esinye"
                else:
                    plural = {
                        "isigidi": "izigidi",
                        "ibhiliyoni": "iibhiliyoni",
                        "ithriliyoni": "iithriliyoni",
                    }.get(b, b)
                    yx = plural + " " + num

            if res == '':
                res = yx
            else:
                res = self.join_na(yx, res)

        return res

    def fractional(self, number, level):
        return self.cardinalPos(number)

    def to_currency(self, value):
        return self.to_cardinal(value) + " imali"

    def to_ordinal(self, number):
        if number == 1:
            return "ye nye"
        return "ye " + self.to_cardinal(number)

    def to_year(self, value):
        return self.to_cardinal(value)

    @staticmethod
    def to_ordinal_num(value):
        return str(value)

    def to_cardinal(self, number):
        if number < 0:
            return "minus " + self.to_cardinal(-number)

        if number == 0:
            return "zero"

        x, y, level = self.float2tuple(number)

        if y == 0:
            return self.cardinalPos(x)

        return self.join_na(
            self.cardinalPos(x),
            " ".join(xhosaOnes[int(d)] for d in str(y))
        )