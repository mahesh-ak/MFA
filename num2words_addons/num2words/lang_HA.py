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


hausaOnes = [
    "", "ɗaya", "biyu", "uku", "huɗu", "biyar", "shida", "bakwai", "takwas",
    "tara",
    "goma",
    "goma sha ɗaya",
    "goma sha biyu",
    "goma sha uku",
    "goma sha huɗu",
    "goma sha biyar",
    "goma sha shida",
    "goma sha bakwai",
    "goma sha takwas",
    "goma sha tara",
]

hausaTens = [
    "",
    "goma",
    "ashirin",
    "talatin",
    "arba'in",
    "hamsin",
    "sittin",
    "sab'in",
    "tamanin",
    "casa'in",
]

hausaHundreds = [
    "",
    "ɗari",
    "ɗari biyu",
    "ɗari uku",
    "ɗari huɗu",
    "ɗari biyar",
    "ɗari shida",
    "ɗari bakwai",
    "ɗari takwas",
    "ɗari tara",
]

hausaBig = [
    '',
    'dubu',
    'miliyan',
    'biliyan',
    'tiriliyan',
]

hausaSeperator = ' da '


class Num2Word_HA(object):

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
            return hausaOnes[number]

        if number < 100:
            x, y = divmod(number, 10)
            if y == 0:
                return hausaTens[x]
            return hausaTens[x] + hausaSeperator + hausaOnes[y]

        x, y = divmod(number, 100)
        if y == 0:
            return hausaHundreds[x]

        return hausaHundreds[x] + hausaSeperator + self.cardinal3(y)

    def cardinalPos(self, number):
        x = number
        res = ''

        for b in hausaBig:
            x, y = divmod(x, 1000)
            if y == 0:
                continue

            # special case: 1000 = "dubu" (not "ɗaya dubu")
            if b == 'dubu' and y == 1:
                yx = 'dubu'
            else:
                # Swap order: group first
                if b.strip()!='':
                    yx = b.strip() + ' ' + self.cardinal3(y)
                else:
                    yx = self.cardinal3(y)

            if res == '':
                res = yx
            else:
                res = yx + hausaSeperator + res

        return res

    def fractional(self, number, level):
        # simple fallback (Hausa fractions are not standardized here)
        return self.cardinalPos(number)

    def to_currency(self, value):
        return self.to_cardinal(value) + " kuɗi"

    def to_ordinal(self, number):
        # Hausa ordinals are usually analytic ("na farko", etc.)
        return "na " + self.to_cardinal(number)

    def to_year(self, value):
        return self.to_cardinal(value)

    @staticmethod
    def to_ordinal_num(value):
        return str(value)

    def to_cardinal(self, number):
        if number < 0:
            return "minus " + self.to_cardinal(-number)

        if number == 0:
            return "sifili"

        x, y, level = self.float2tuple(number)

        if y == 0:
            return self.cardinalPos(x)

        # decimals (simple digit reading)
        return (
            self.cardinalPos(x)
            + " da "
            + " ".join(hausaOnes[int(d)] for d in str(y))
        )