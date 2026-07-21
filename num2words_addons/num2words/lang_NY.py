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


nyanjaOnes = [
    "", "chimodzi", "ziwiri", "zitatu", "zinayi", "zisanu", "zisanu ndi chimodzi",
    "zisanu ndi ziwiri", "zisanu ndi zitatu", "zisanu ndi zinayi",
    "khumi",
    "khumi ndi chimodzi",
    "khumi ndi ziwiri",
    "khumi ndi zitatu",
    "khumi ndi zinayi",
    "khumi ndi zisanu",
    "khumi ndi zisanu ndi chimodzi",
    "khumi ndi zisanu ndi ziwiri",
    "khumi ndi zisanu ndi zitatu",
    "khumi ndi zisanu ndi zinayi",
]

nyanjaTens = [
    "",
    "khumi",
    "makumi awiri",
    "makumi atatu",
    "makumi anayi",
    "makumi asanu",
    "makumi asanu ndi limodzi",
    "makumi asanu ndi awiri",
    "makumi asanu ndi atatu",
    "makumi asanu ndi anayi",
]

nyanjaHundreds = [
    "",
    "zana limodzi",
    "zana ziwiri",
    "zana zitatu",
    "zana zinayi",
    "zana zisanu",
    "zana zisanu ndi chimodzi",
    "zana zisanu ndi ziwiri",
    "zana zisanu ndi zitatu",
    "zana zisanu ndi zinayi",
]

nyanjaBig = [
    '',
    'zikwi',
    'miliyoni',
    'biliyoni',
    'tiriliyoni',
]

nyanjaSeparator = ' ndi '


class Num2Word_NY(object):

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
            return nyanjaOnes[number]

        if number < 100:
            x, y = divmod(number, 10)
            if y == 0:
                return nyanjaTens[x]
            return nyanjaTens[x] + nyanjaSeparator + nyanjaOnes[y]

        x, y = divmod(number, 100)
        if y == 0:
            return nyanjaHundreds[x]

        return nyanjaHundreds[x] + nyanjaSeparator + self.cardinal3(y)

    def cardinalPos(self, number):
        x = number
        res = ''

        for b in nyanjaBig:
            x, y = divmod(x, 1000)
            if y == 0:
                continue
            
            # Chichewa: number + group
            if b == 'zikwi' and y == 1:
                yx = 'zikwi chimodzi'
            elif b != '':
                yx = self.cardinal3(y) + ' ' + b
                if y == 1:
                    yx = b + ' imodzi'
            else:
                yx = self.cardinal3(y)

            if res == '':
                res = yx
            else:
                res = yx + nyanjaSeparator + res

        return res

    def fractional(self, number, level):
        return self.cardinalPos(number)

    def to_currency(self, value):
        return self.to_cardinal(value) + " ndalama"

    def to_ordinal(self, number):
        if number == 1:
            return "ya imodzi"
        return "ya " + self.to_cardinal(number)

    def to_year(self, value):
        return self.to_cardinal(value)

    @staticmethod
    def to_ordinal_num(value):
        return str(value)

    def to_cardinal(self, number):
        if number < 0:
            return "minus " + self.to_cardinal(-number)

        if number == 0:
            return "ziro"

        x, y, level = self.float2tuple(number)

        if y == 0:
            return self.cardinalPos(x)

        return (
            self.cardinalPos(x)
            + " ndi "
            + " ".join(nyanjaOnes[int(d)] for d in str(y))
        )