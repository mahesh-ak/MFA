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


# 0–19
cebOnes = [
    "", "usa", "duha", "tulo", "upat", "lima",
    "unom", "pito", "walo", "siyam",
    "napulo",
    "onse",
    "dose",
    "trese",
    "katorse",
    "kinse",
    "dise-sais",
    "dise-siyete",
    "dise-otso",
    "dise-nwebe",
]

# Tens
cebTens = [
    "",
    "napulo",
    "baynte",
    "traynta",
    "kwarenta",
    "singkwenta",
    "sesenta",
    "setenta",
    "otsenta",
    "nubenta",
]

# Hundreds (use "ka")
cebHundreds = [
    "",
    "usa ka gatos",
    "duha ka gatos",
    "tulo ka gatos",
    "upat ka gatos",
    "lima ka gatos",
    "unom ka gatos",
    "pito ka gatos",
    "walo ka gatos",
    "siyam ka gatos",
]

# Large numbers
cebBig = [
    '',
    ' ka libo',
    ' ka milyon',
    ' ka bilyon',
    ' ka trilyon',
]

cebSeparator = ' ug '


class Num2Word_CEB(object):
    errmsg_toobig = "Too large"
    MAXNUM = 10 ** 36

    def __init__(self):
        self.number = 0

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
        # 0–19
        if number <= 19:
            return cebOnes[number]

        # 20–99
        if number < 100:
            x, y = divmod(number, 10)

            if y == 0:
                return cebTens[x]

            return cebTens[x] + cebSeparator + cebOnes[y]

        # 100–999
        x, y = divmod(number, 100)

        if y == 0:
            return cebHundreds[x]

        return cebHundreds[x] + cebSeparator + self.cardinal3(y)

    def cardinalPos(self, number):
        x = number
        res = ''

        for idx, b in enumerate(cebBig):
            x, y = divmod(x, 1000)

            if y == 0:
                continue

            if idx == 0:
                yx = self.cardinal3(y)
            else:
                if y == 1:
                    # Special case: "usa ka libo" → often just "usa ka libo"
                    yx = "usa" + b
                else:
                    yx = self.cardinal3(y) + b

            if res == '':
                res = yx
            else:
                res = yx + cebSeparator + res

        return res

    def fractional(self, number, level):
        x = self.cardinalPos(number)

        # Cebuano decimals are typically read digit-by-digit
        digits = str(number).zfill(level)
        return "punto " + " ".join(cebOnes[int(d)] for d in digits)

    def to_currency(self, value):
        return self.to_cardinal(value) + " pesos"

    def to_ordinal(self, number):
        # Simplified (true Cebuano ordinals are more complex)
        return "ika-" + self.to_cardinal(number)

    def to_year(self, value):
        return self.to_cardinal(value)

    @staticmethod
    def to_ordinal_num(value):
        return str(value)

    def to_cardinal(self, number):
        if number < 0:
            return "minus " + self.to_cardinal(-number)

        if number == 0:
            return "sero"

        x, y, level = self.float2tuple(number)

        if y == 0:
            return self.cardinalPos(x)

        if x == 0:
            return self.fractional(y, level)

        return self.cardinalPos(x) + " punto " + " ".join(
            cebOnes[int(d)] for d in str(y).zfill(level)
        )