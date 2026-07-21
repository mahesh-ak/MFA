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


shonaOnes = [
    "", "imwe", "mbiri", "nhatu", "ina", "shanu", "nhanhatu",
    "nomwe", "sere", "pfumbamwe",
    "gumi",
    "gumi ne imwe",
    "gumi nemaviri",
    "gumi nematatu",
    "gumi nemana",
    "gumi nemashanu",
    "gumi nematanhatu",
    "gumi nemanomwe",
    "gumi nemasere",
    "gumi nemapfumbamwe",
]

shonaTens = [
    "",
    "gumi",
    "makumi maviri",
    "makumi matatu",
    "makumi mana",
    "makumi mashanu",
    "makumi matanhatu",
    "makumi manomwe",
    "makumi masere",
    "makumi mapfumbamwe",
]

shonaHundreds = [
    "",
    "zana rimwe",
    "mazana maviri",
    "mazana matatu",
    "mazana mana",
    "mazana mashanu",
    "mazana matanhatu",
    "mazana manomwe",
    "mazana masere",
    "mazana mapfumbamwe",
]

shonaBig = [
    '',
    'chiuru',
    'miriyoni',
    'bhiriyoni',
    'tiririyoni',
]



class Num2Word_SN(object):

    errmsg_toobig = "Too large"
    MAXNUM = 10 ** 36

    def __init__(self):
        self.number = 0
        
    def assimilate(self, word):
        mapping = {
            "mbiri": "maviri", 
            "ina": "mana", 
            "nhanhatu": "matatu",
            "nomwe": "manomwe", 
            "pfumbamwe": "mapfumbamwe",
            "nhatu": "matatu",
            "shanu": "mashanu",
            "nhatu": "matatu",
            "sere": "masere",
        }
        return mapping.get(word, word)

    # --- phonological join ---
    def join_ne(self, a, b):
        b = b.split()
        b2 = [self.assimilate(b[0])] + (b[1:] if len(b) > 1 else [])
        b2 = ' '.join(b2)

        if b2.startswith(("a", "e", "i", "o", "u")):
            return a + " nem" + b2
        elif b2.startswith("m"):
            return a + " ne" + b2
        return a + " ne" + b2

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
            if number == 1:
                return "rimwe"
            return shonaOnes[number]

        if number < 100:
            x, y = divmod(number, 10)
            if y == 0:
                return shonaTens[x]
            return self.join_ne(shonaTens[x], shonaOnes[y])

        x, y = divmod(number, 100)
        if y == 0:
            return shonaHundreds[x]

        return self.join_ne(shonaHundreds[x], self.cardinal3(y))

    def cardinalPos(self, number):
        x = number
        res = ''

        for i, b in enumerate(shonaBig):
            x, y = divmod(x, 1000)
            if y == 0:
                continue

            # --- base number ---
            if y == 1:
                if b == 'chiuru':
                    num = "chimwe"
                elif b in ['miriyoni', 'bhiriyoni', 'tiririyoni']:
                    num = "rimwe"
                else:
                    num = "rimwe"
            else:
                num = self.cardinal3(y)

            # --- group handling ---
            if b == '':
                yx = num

            elif b == 'chiuru':
                if y == 1:
                    yx = "chiuru chimwe"
                else:
                    yx = "zviuru " + num

            else:
                # miliyoni / bhiriyoni
                if y != 1:
                    b = 'ma' + b
                yx = b + " " + num

            if res == '':
                res = yx
            else:
                res = self.join_ne(yx, res)

        return res

    def fractional(self, number, level):
        return self.cardinalPos(number)

    def to_currency(self, value):
        return self.to_cardinal(value) + " mari"

    def to_ordinal(self, number):
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

        return self.join_ne(
            self.cardinalPos(x),
            + " ".join(shonaOnes[int(d)] for d in str(y))
        )