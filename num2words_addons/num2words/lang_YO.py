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


class Num2Word_YO(object):
    # Standalone digits (also useful for decimal parts)
    DIGITS = [
        "odo", "ọ̀kan", "méjì", "mẹ́ta", "mẹ́rin",
        "márùn-ún", "mẹ́fà", "méje", "mẹ́jọ", "mẹ́sàn-án",
    ]

    # Simple exact forms up to 10 and the traditional 11–19 block.
    SMALL = {
        0: "odo",
        1: "ọ̀kan",
        2: "méjì",
        3: "mẹ́ta",
        4: "mẹ́rin",
        5: "márùn-ún",
        6: "mẹ́fà",
        7: "méje",
        8: "mẹ́jọ",
        9: "mẹ́sàn-án",
        10: "ẹ̀wá",
        11: "ọ̀kanlá",
        12: "méjìlá",
        13: "mẹ́tàlá",
        14: "mẹ́rìnlá",
        20: "ogún",
        30: "ọgbọ̀n",
        40: "ogójì",
        50: "àádọ́ta",
        60: "ọgọ́ta",
        70: "àádọ́rin",
        80: "ọgọ́rin",
        90: "àádọ́rùn-ún",
    }

    # Hard subtractive forms from the next base.
    # These are intentionally explicit so the vigesimal template stays visible.
    SUBTRACTIVE = {
        15: "márùn-dín-lógún",
        16: "mẹ́rìndínlógún",
        17: "mẹ́tàdínlógún",
        18: "mẹ́jìdínlógún",
        19: "ọ̀kàndínlógún",
        25: "márùn-dín-lọ́gbọ̀n",
        26: "mẹ́rìndínlọ́gbọ̀n",
        27: "mẹ́tàdínlọ́gbọ̀n",
        28: "mẹ́jìdínlọ́gbọ̀n",
        29: "ọ̀kàndínlọ́gbọ̀n",
        35: "márùn-dín-lógójì",
        36: "mẹ́rìndínlógójì",
        37: "mẹ́tàdínlógójì",
        38: "mẹ́jìdínlógójì",
        39: "ọ̀kàndínlógójì",
        45: "márùn-dín-àádọ́ta",
        46: "mẹ́rìndín-àádọ́ta",
        47: "mẹ́tàdín-àádọ́ta",
        48: "mẹ́jìdín-àádọ́ta",
        49: "ọ̀kàndín-àádọ́ta",
        55: "márùn-dín-ọgọ́ta",
        56: "mẹ́rìndín-ọgọ́ta",
        57: "mẹ́tàdín-ọgọ́ta",
        58: "mẹ́jìdín-ọgọ́ta",
        59: "ọ̀kàndín-ọgọ́ta",
        65: "márùn-dín-àádọ́rin",
        66: "mẹ́rìndín-àádọ́rin",
        67: "mẹ́tàdín-àádọ́rin",
        68: "mẹ́jìdín-àádọ́rin",
        69: "ọ̀kàndín-àádọ́rin",
        75: "márùn-dín-ọgọ́rin",
        76: "mẹ́rìndín-ọgọ́rin",
        77: "mẹ́tàdín-ọgọ́rin",
        78: "mẹ́jìdín-ọgọ́rin",
        79: "ọ̀kàndín-ọgọ́rin",
        85: "márùn-dín-àádọ́rùn-ún",
        86: "mẹ́rìndín-àádọ́rùn-ún",
        87: "mẹ́tàdín-àádọ́rùn-ún",
        88: "mẹ́jìdín-àádọ́rùn-ún",
        89: "ọ̀kàndín-àádọ́rùn-ún",
        95: "márùn-dín-ọgọ́rùn-ún",
        96: "mẹ́rìndín-ọgọ́rùn-ún",
        97: "mẹ́tàdín-ọgọ́rùn-ún",
        98: "mẹ́jìdín-ọgọ́rùn-ún",
        99: "ọ̀kàndín-ọgọ́rùn-ún",
    }

    # Exact hundred words are irregular in Yoruba, so they are explicit.
    HUNDREDS = {
        1: "ọgọ́rùn-ún",
        2: "igba",
        3: "ọ̀ọ́dúnrún",
        4: "irínwó",
        5: "ẹ̀ẹ́dẹ́gbẹ̀ta",
        6: "ẹgbẹ̀ta",
        7: "ẹ̀ẹ́dẹ́gbẹ̀rin",
        8: "ẹgbẹ̀rin",
        9: "ẹ̀ẹ́dẹ́gbẹ̀rún",
    }

    # Larger scales are kept simple and compositional.
    BIG = [
        "",
        "ẹgbẹ̀rún",
        "mílíọ̀nù",
        "bílíọ̀nù",
        "trílíọ̀nù",
        "kàtrílíọ̀nù",
    ]

    def _drop_i(self, word):
        return word[:-1] if word.endswith("i") else word

    def float2tuple(self, value):
        pre = int(value)
        self.precision = abs(Decimal(str(value)).as_tuple().exponent)

        post = abs(value - pre) * 10 ** self.precision
        if abs(round(post) - post) < 0.01:
            post = int(round(post))
        else:
            post = int(floor(post))

        return pre, post, self.precision

    def cardinal2(self, number):
        if number in self.SMALL:
            return self.SMALL[number]
        if number in self.SUBTRACTIVE:
            return self.SUBTRACTIVE[number]

        if number < 100:
            tens, unit = divmod(number, 10)

            if tens == 2:
                base = "ogún"
            elif tens == 3:
                base = "ọgbọ̀n"
            elif tens == 4:
                base = "ogójì"
            elif tens == 5:
                base = "àádọ́ta"
            elif tens == 6:
                base = "ọgọ́ta"
            elif tens == 7:
                base = "àádọ́rin"
            elif tens == 8:
                base = "ọgọ́rin"
            elif tens == 9:
                base = "àádọ́rùn-ún"
            else:
                base = ""

            if unit == 0:
                return base

            # Additive forms: 20+1..4, 30+1..4, 40+1..4, etc.
            return f"{base} {self.DIGITS[unit]}"

        raise ValueError("cardinal2 only handles numbers below 100")

    def cardinal3(self, number):
        if number < 100:
            return self.cardinal2(number)

        hundreds, rest = divmod(number, 100)

        if rest == 0:
            return self.HUNDREDS[hundreds]

        # Keep the hundred word explicit, then recurse on the remainder.
        return self.HUNDREDS[hundreds] + " " + self.cardinal2(rest)

    def cardinalPos(self, number):
        if number == 0:
            return self.DIGITS[0]

        parts = []
        x = number
        scale_idx = 0

        while x > 0:
            x, group = divmod(x, 1000)

            if group:
                if scale_idx == 0:
                    part = self.cardinal3(group)
                else:
                    scale = self.BIG[scale_idx]
                    if group == 1 and scale_idx == 1:
                        part = scale
                    elif group == 1:
                        part = scale
                    else:
                        part = self.cardinal3(group) + " " + scale

                parts.append(part)

            scale_idx += 1

        return " ".join(reversed(parts))

    def to_cardinal(self, number):
        if number < 0:
            return "kò " + self.to_cardinal(-number)

        if number == 0:
            return "odo"

        x, y, level = self.float2tuple(number)

        if y == 0:
            return self.cardinalPos(x)

        right = str(y).zfill(level)
        return self.cardinalPos(x) + " àti " + " ".join(
            self.DIGITS[int(d)] for d in right
        )

    def to_currency(self, value):
        return self.to_cardinal(value) + " naira"