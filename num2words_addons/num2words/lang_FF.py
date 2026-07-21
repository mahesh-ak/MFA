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

# 0–19 (simple additive system)
ffOnes = [
    "", "go'o", "ɗiɗi", "tati", "nay",
    "joyi", "jeego", "jowiɗi", "jowiɗi e go'o", "jowiɗi e ɗiɗi",
    "sappo",
    "sappo e go'o",
    "sappo e ɗiɗi",
    "sappo e tati",
    "sappo e nay",
    "sappo e joyi",
    "sappo e jeego",
    "sappo e jowiɗi",
    "sappo e jowiɗi e go'o",
    "sappo e jowiɗi e ɗiɗi",
]

# Tens (base-10, regular)
ffTens = [
    "",
    "sappo",
    "cappanɗe ɗiɗi",   # 20
    "cappanɗe tati",   # 30
    "cappanɗe nay",    # 40
    "cappanɗe joyi",   # 50
    "cappanɗe jeego",  # 60
    "cappanɗe jowiɗi", # 70
    "cappanɗe jowiɗi e go'o",  # 80 (approx)
    "cappanɗe jowiɗi e ɗiɗi",  # 90 (approx)
]

# Hundreds (regular formation)
ffHundreds = [
    "",
    "teemedere go'o",
    "teemedere ɗiɗi",
    "teemedere tati",
    "teemedere nay",
    "teemedere joyi",
    "teemedere jeego",
    "teemedere jowiɗi",
    "teemedere jowiɗi e go'o",
    "teemedere jowiɗi e ɗiɗi",
]

# Large numbers
ffBig = [
    '',
    ' dubu',        # thousand
    ' miliyon',     # million
    ' biliyon',     # billion
    ' tiriliyon',
    ' katriliyon',
]

ffFrac = ["", "fenndu", "temedere"]
ffFracBig = ["", "dubundum", "miliyundum", "biliyundum"]

ffSeperator = ' e '   # "and"


class Num2Word_FF(object):
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
        if number <= 19:
            return ffOnes[number]

        if number < 100:
            x, y = divmod(number, 10)
            if y == 0:
                return ffTens[x]
            return ffTens[x] + ffSeperator + ffOnes[y]

        x, y = divmod(number, 100)
        if y == 0:
            return ffHundreds[x]
        return ffHundreds[x] + ffSeperator + self.cardinal3(y)

    def cardinalPos(self, number):
        x = number
        res = ''
        for b in ffBig:
            x, y = divmod(x, 1000)
            if y == 0:
                continue

            yx = self.cardinal3(y) + b

            if b == ' dubu' and y == 1:
                yx = 'dubu'

            if res == '':
                res = yx
            else:
                res = yx + ffSeperator + res

        return res

    def fractional(self, number, level):
        x = self.cardinalPos(number)
        ld3, lm3 = divmod(level, 3)
        ltext = (ffFrac[lm3] + " " + ffFracBig[ld3]).strip()
        return x + " " + ltext

    def to_currency(self, value):
        return self.to_cardinal(value) + " CFA"

    def to_ordinal(self, number):
        return self.to_cardinal(number)  # simplification

    def to_year(self, value):
        return self.to_cardinal(value)

    @staticmethod
    def to_ordinal_num(value):
        return str(value)

    def to_cardinal(self, number):
        if number < 0:
            return "minus " + self.to_cardinal(-number)

        if number == 0:
            return "sifero"

        x, y, level = self.float2tuple(number)

        if y == 0:
            return self.cardinalPos(x)

        if x == 0:
            return self.fractional(y, level)

        return self.cardinalPos(x) + ffSeperator + self.fractional(y, level)