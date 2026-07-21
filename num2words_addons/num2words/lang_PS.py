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
    "", "یو", "دوه", "درې", "څلور", "پنځه", "شپږ", ("اووه", "اوه"),  "اته",
    "نهه",
    "لس",
    "یوولس",
    "دولس",
    "دیارلس",
    "څوارلس",
    "پنځلس",
    "شپاړس",
    "اوولس",
    "اتلس",
    "نولس",
]

farsiTens = [
    "",
    "لس",
    "شل",
    "دېرش",
    "څلوېښت",
    "پنځوس",
    "شپېته",
    "اویا",
    "اتیا",
    "نوي",
]

farsiHundreds = [
    "",
    "سل",
    "دوه سوه",
    "درې سوه",
    "څلور سوه",
    "پنځه سوه",
    "شپږ سوه",
    "اووه سوه",
    "اته سوه",
    "نهه سوه",
]

# IMPORTANT: use "زر" not "زره"
farsiBig = [
    '',
    ' زر',
    ' میلیون',
    ' میلیارد',
    ' ټریلیون',
]

farsiFrac = ["", "لسم", "صدم"]
farsiFracBig = ["", "زریم", "میلیونیم", "میلیاردیم"]

farsiSeperator = ' او '

ORDINAL_EXCEPTIONS = {
    0: "صفرم",
    1: "لومړی",
    2: "دوهم",
    3: "درېیم",
    11: "یوولسم",
    12: "دوولسم",
    13: "دیارلسم",
    14: "څوارلسم",
    15: "پنځلسم",
    16: "شپاړسم",
    17: "اوولسم",
    18: "اتلسم",
    19: "نولسم",
}

TENS_ORDINALS = {
    20: "ویشتم",
    30: "دېرشم",
    40: "څلوېښتم",
    50: "پنځوسم",
    60: "شپېتم",
    70: "اویاوم",
    80: "اتیایم",
    90: "نويیم",
}


class Num2Word_PS(object):

    errmsg_toobig = "Too large"
    MAXNUM = 10 ** 36

    def __init__(self):
        self.number = 0
    
    def str_to_number(self, value):
        return Decimal(value)


    
    def get_one(self, n, in_compound=False):
        val = farsiOnes[n]
        if isinstance(val, tuple):
            return val[1] if in_compound else val[0]
        return val 

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
            return self.get_one(number)

        if number < 100:
            x, y = divmod(number, 10)

            if y == 0:
                return farsiTens[x]

            if number >= 90:
                return farsiTens[x] + farsiSeperator + self.get_one(y, in_compound=True)

            return self.get_one(y, in_compound=True) + " " + farsiTens[x]
        x, y = divmod(number, 100)
        if y == 0:
            return farsiHundreds[x]

        return farsiHundreds[x] + farsiSeperator + self.cardinal3(y)

    def cardinalPos(self, number):
        if number == 0:
            return "صفر"

        x = number
        res = ''

        for i, b in enumerate(farsiBig):
            x, y = divmod(x, 1000)
            if y == 0:
                continue

            # special: 1000 = "زر" not "یو زر"
            if i == 1:
                if y == 1:
                    yx = "زر"
                else:
                    yx = self.cardinal3(y) + " زره"
            else:
                self._in_compound = True
                yx = self.cardinal3(y) + b
                self._in_compound = False

            if res == '':
                res = yx
            else:
                res = yx + farsiSeperator + res

        return res

    def fractional(self, number, level):
        if number == 5 and level == 1:
            return "نیم"

        if number < 100:
            x = self.cardinal3(number)
        else:
            x = self.cardinalPos(number)

        ld3, lm3 = divmod(level, 3)
        ltext = (farsiFrac[lm3] + " " + farsiFracBig[ld3]).strip()

        return x + " " + ltext

    def to_currency(self, value):
        return self.to_cardinal(value) + " افغانۍ"

    def to_ordinal(self, number):
        if number in ORDINAL_EXCEPTIONS:
            return ORDINAL_EXCEPTIONS[number]

        # --- special 20–29 rule ---
        if 20 < number < 30:
            unit = number % 10
            return farsiOnes[unit] + " ویشتم"

        text = self.to_cardinal(number)
        parts = text.split(farsiSeperator)
        last = parts[-1]

        if last.endswith("درې"):
            last = "درېیم"
        elif last.endswith("دوه"):
            last = "دوهم"
        elif last.endswith("یو"):
            last = "لومړی"
        else:
            last = last + "م"

        parts[-1] = last
        return farsiSeperator.join(parts)

    def to_year(self, value):
        parts = []

        thousands = value // 1000
        remainder = value % 1000

        if thousands:
            if thousands == 1:
                parts.append("زر")
            else:
                parts.append(self.cardinal3(thousands) + " زر")

        if remainder:
            hundreds = remainder // 100
            last_two = remainder % 100

            if hundreds:
                parts.append(self.cardinal3(hundreds * 100))

            if last_two:
                tens, ones = divmod(last_two, 10)
                if ones:
                    parts.append(self.get_one(ones) + " " + farsiTens[tens])
                else:
                    parts.append(farsiTens[tens])

        return " او ".join(parts)

    @staticmethod
    def to_ordinal_num(self, number):
        if number in ORDINAL_EXCEPTIONS:
            return ORDINAL_EXCEPTIONS[number]

        return self.to_cardinal(number) + "م"

    def to_cardinal(self, number):
        if number < 0:
            return "منفي " + self.to_cardinal(-number)

        if number == 0:
            return "صفر"

        x, y, level = self.float2tuple(number)

        if y == 0:
            return self.cardinalPos(x)

        if x == 0:
            return self.fractional(y, level)

        # IMPORTANT: always include "او"
        return self.cardinalPos(x) + farsiSeperator + self.fractional(y, level)