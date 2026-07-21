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

from decimal import Decimal
from math import floor


# Digits
DIGITS = [
    "tus", "benn", "ñaar", "ñett", "ñeent", "juróom",
    "juróom-benn", "juróom-ñaar", "juróom-ñett", "juróom-ñeent"
]

# 1–19 (hardcoded like Georgian)
ONES = [
    "", "benn", "ñaar", "ñett", "ñeent", "juróom",
    "juróom-benn", "juróom-ñaar", "juróom-ñett", "juróom-ñeent",
    "fukk", "fukk ak benn", "fukk ak ñaar", "fukk ak ñett",
    "fukk ak ñeent", "fukk ak juróom", "fukk ak juróom-benn",
    "fukk ak juróom-ñaar", "fukk ak juróom-ñett",
    "fukk ak juróom-ñeent",
]

# Exact tens (vigesimal style, but hardcoded like Georgian)
TENS = {
    20: "ñaar-fukk",
    30: "ñaar-fukk ak fukk",
    40: "ñaar ñaar-fukk",
    50: "ñaar ñaar-fukk ak fukk",
    60: "ñett ñaar-fukk",
    70: "ñett ñaar-fukk ak fukk",
    80: "ñeent ñaar-fukk",
    90: "ñeent ñaar-fukk ak fukk",
}

# Tens stems (used when unit follows)
TENS_STEM = {
    20: "ñaar-fukk ak",
    30: "ñaar-fukk ak fukk ak",
    40: "ñaar ñaar-fukk ak",
    50: "ñaar ñaar-fukk ak fukk ak",
    60: "ñett ñaar-fukk ak",
    70: "ñett ñaar-fukk ak fukk ak",
    80: "ñeent ñaar-fukk ak",
    90: "ñeent ñaar-fukk ak fukk ak",
}

# Hundreds
HUNDREDS = [
    "", "téeméer", "ñaar téeméer", "ñett téeméer", "ñeent téeméer",
    "juróom téeméer", "juróom-benn téeméer", "juróom-ñaar téeméer",
    "juróom-ñett téeméer", "juróom-ñeent téeméer"
]

# Big scales
BIG = [
    "",
    "junni",
    "milyoŋ",
    "milyaar",
    "tirilyoŋ",
]


class Num2Word_WO(object):

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
        # 1–19
        if number < 20:
            return ONES[number]

        # 20–99 (Georgian-style branching preserved)
        if number < 100:
            if number in TENS:
                return TENS[number]

            if number < 40:
                base = TENS_STEM[20]
                return base + " " + ONES[number - 20]

            if number < 60:
                base = TENS_STEM[40]
                return base + " " + ONES[number - 40]

            if number < 80:
                base = TENS_STEM[60]
                return base + " " + ONES[number - 60]

            base = TENS_STEM[80]
            return base + " " + ONES[number - 80]

        # 100–999
        x, y = divmod(number, 100)
        if y == 0:
            return HUNDREDS[x]

        return HUNDREDS[x] + " ak " + self.cardinal3(y)

    def cardinalPos(self, number):
        if number == 0:
            return DIGITS[0]

        parts = []
        x = number
        scale_idx = 0

        while x > 0:
            x, group = divmod(x, 1000)

            if group:
                if scale_idx == 0:
                    part = self.cardinal3(group)

                elif scale_idx == 1:
                    if group == 1:
                        part = "junni"
                    else:
                        part = self.cardinal3(group) + " junni"

                else:
                    scale = BIG[scale_idx]
                    if group == 1:
                        part = "benn " + scale
                    else:
                        part = self.cardinal3(group) + " " + scale

                parts.append(part)

            scale_idx += 1

        return " ak ".join(reversed(parts))

    def to_cardinal(self, number):
        if number < 0:
            return "minus " + self.to_cardinal(-number)

        if number == 0:
            return "tus"

        x, y, level = self.float2tuple(number)

        if y == 0:
            return self.cardinalPos(x)

        right = str(y).zfill(level)
        return self.cardinalPos(x) + " ak " + " ".join(
            DIGITS[int(d)] for d in right
        )

    def to_currency(self, value):
        return self.to_cardinal(value) + " xaalis"