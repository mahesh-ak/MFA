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

farsiOnes = [
    "", "یەک", "دوو", "سێ", "چوار", "پێنج", "شەش", "حەوت", "هەشت",
    "نۆ",
    "دە",
    "یازدە",
    "دوازدە",
    "سێزدە",
    "چواردە",
    "پازدە",
    "شانزە",
    "حەڤدە",
    "هەژدە",
    "نۆزدە",
]

farsiTens = [
    "",
    "دە",
    "بیست",
    "سی",
    "چل",
    "پەنجا",
    "شەست",
    "حەفتا",
    "هەشتا",
    "نەوەد",
]

farsiHundreds = [
    "",
    "سەد",
    "دووسەد",
    "سێسەد",
    "چوارسەد",
    "پێنجسەد",
    "شەشسەد",
    "حەوتسەد",
    "هەشتسەد",
    "نۆسەد",
]

farsiBig = [
    '',
    ' هەزار',
    ' ملیۆن',
    " ملیار",
    ' تریلیۆن',
    " تریلیارد",
]

farsiFrac = ["", "دەیەم", "سەدەم"]
farsiFracBig = ["", "هەزارەم", "ملیۆنەم", "ملیارەم"]

farsiSeperator = ' و '


class Num2Word_CKB(object):
    errmsg_toobig = "Too large"
    MAXNUM = 10 ** 36

    def __init__(self):
        self.number = 0
    
    def str_to_number(self, value):
        return Decimal(value)


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
            return farsiOnes[number]
        if number < 100:
            x, y = divmod(number, 10)
            if y == 0:
                return farsiTens[x]
            return farsiTens[x] + farsiSeperator + farsiOnes[y]
        x, y = divmod(number, 100)
        if y == 0:
            return farsiHundreds[x]
        return farsiHundreds[x] + farsiSeperator + self.cardinal3(y)

    def cardinalPos(self, number):
        x = number
        res = ''
        for b in farsiBig:
            x, y = divmod(x, 1000)
            if y == 0:
                continue
            yx = self.cardinal3(y) + b
            if b == ' هەزار' and y == 1:
                yx = 'هەزار'
            if res == '':
                res = yx
            else:
                res = yx + farsiSeperator + res
        return res

    def fractional(self, number, level):
        if number == 5:
            return "نیو"  # half
        x = self.cardinalPos(number)
        ld3, lm3 = divmod(level, 3)
        ltext = (farsiFrac[lm3] + " " + farsiFracBig[ld3]).strip()
        return x + " " + ltext

    def to_currency(self, value):
        return self.to_cardinal(value) + " دینار"

    def to_ordinal(self, number):
        r = self.to_cardinal(number)

        # special cases (must come first)
        if r.endswith("دوازدە"):
            return r + "یەم"

        if r.endswith("ە"):
            return r[:-1] + "ەم"

        if r.endswith(("ێ", "ی", "و")):
            return r + "یەم"

        return r + "ەم"

    def to_year(self, value):
        return self.to_cardinal(value)

    @staticmethod
    def to_ordinal_num(value):
        return str(value) + "ەم"

    def to_cardinal(self, number):
        if number < 0:
            return "منفی " + self.to_cardinal(-number)
        if number == 0:
            return "سفر"
        x, y, level = self.float2tuple(number)
        if y == 0:
            return self.cardinalPos(x)
        if x == 0:
            return self.fractional(y, level)
        return self.cardinalPos(x) + farsiSeperator + self.fractional(y, level)