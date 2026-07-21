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


# Digits for decimals and standalone zero
DIGITS = [
    "ნული", "ერთი", "ორი", "სამი", "ოთხი", "ხუთი",
    "ექვსი", "შვიდი", "რვა", "ცხრა"
]

# Hardcoded 1–19
ONES = [
    "", "ერთი", "ორი", "სამი", "ოთხი", "ხუთი", "ექვსი",
    "შვიდი", "რვა", "ცხრა", "ათი", "თერთმეტი", "თორმეტი",
    "ცამეტი", "თოთხმეტი", "თხუთმეტი", "თექვსმეტი",
    "ჩვიდმეტი", "თვრამეტი", "ცხრამეტი",
]

# Exact tens
TENS = {
    20: "ოცი",
    30: "ოცდაათი",
    40: "ორმოცი",
    50: "ორმოცდაათი",
    60: "სამოცი",
    70: "სამოცდაათი",
    80: "ოთხმოცი",
    90: "ოთხმოცდაათი",
}

# Tens stems used when a unit follows
TENS_STEM = {
    20: "ოცდა",
    30: "ოცდათ",
    40: "ორმოცდა",
    50: "ორმოცდათ",
    60: "სამოცდა",
    70: "სამოცდათ",
    80: "ოთხმოცდა",
    90: "ოთხმოცდათ",
}

# Hundreds
HUNDREDS = [
    "", "ასი", "ორასი", "სამასი", "ოთხასი",
    "ხუთასი", "ექვსასი", "შვიდასი", "რვაასი", "ცხრაასი"
]

# Big scales
BIG = [
    "",
    "ათასი",
    "მილიონი",
    "მილიარდი",
    "ტრილიონი",
]


class Num2Word_KA(object):

    def _drop_i(self, word):
        return word[:-1] if word.endswith("ი") else word

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
        # 1–19 are hardcoded
        if number < 20:
            return ONES[number]

        # 20–99: Georgian stem + suffix pattern
        if number < 100:
            if number in TENS:
                return TENS[number]

            if number < 40:
                base = "ოცდა"
                return base + ONES[number - 20]

            if number < 60:
                base = "ორმოცდა"
                return base + ONES[number - 40]

            if number < 80:
                base = "სამოცდა"
                return base + ONES[number - 60]

            base = "ოთხმოცდა"
            return base + ONES[number - 80]
        # 100–999
        x, y = divmod(number, 100)
        if y == 0:
            return HUNDREDS[x]

        base = self._drop_i(HUNDREDS[x])
        return base + " " + self.cardinal3(y)

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
                        part = "ათასი"
                    else:
                        part = self.cardinal3(group) + " ათასი"

                else:
                    scale = BIG[scale_idx]
                    if group == 1:
                        part = "ერთი " + scale
                    else:
                        part = self.cardinal3(group) + " " + scale

                parts.append(part)

            scale_idx += 1

        return " ".join(reversed(parts))

    def to_cardinal(self, number):
        if number < 0:
            return "მინუს " + self.to_cardinal(-number)

        if number == 0:
            return "ნული"

        x, y, level = self.float2tuple(number)

        if y == 0:
            return self.cardinalPos(x)

        # Decimal part: keep digits, including zeros
        right = str(y).zfill(level)
        return self.cardinalPos(x) + " მთელი " + " ".join(
            DIGITS[int(d)] for d in right
        )

    def to_currency(self, value):
        return self.to_cardinal(value) + " ლარი"