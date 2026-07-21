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

from __future__ import unicode_literals

ONES = (
    'សូន្យ', 'មួយ', 'ពីរ', 'បី', 'បួន',
    'ប្រាំ', 'ប្រាំមួយ', 'ប្រាំពីរ', 'ប្រាំបី', 'ប្រាំបួន'
)

TENS = {
    1: 'ដប់',
    2: 'ម្ភៃ',
    3: 'សាមសិប',
    4: 'សែសិប',
    5: 'ហាសិប',
    6: 'ហុកសិប',
    7: 'ចិតសិប',
    8: 'ប៉ែតសិប',
    9: 'កៅសិប',
}

THOUSANDS = (
    '', 'ពាន់', 'លាន', 'ប៊ីលាន', 'ទ្រីលាន'
)


class Num2Word_KM(object):

    def _convert_nn(self, val):
        if val < 10:
            return ONES[val]

        if val < 20:
            if val == 10:
                return 'ដប់'
            return 'ដប់ ' + ONES[val % 10]

        tens = val // 10
        unit = val % 10

        if unit == 0:
            return TENS[tens]

        return TENS[tens] + ' ' + ONES[unit]

    def _convert_nnn(self, val):
        word = ''
        hundreds = val // 100
        rest = val % 100

        if hundreds:
            word = ONES[hundreds] + ' រយ'
            if rest:
                word += ' '

        if rest:
            word += self._convert_nn(rest)

        return word

    def khmer_number(self, val):
        if val == 0:
            return ONES[0]

        if val < 100:
            return self._convert_nn(val)

        if val < 1000:
            return self._convert_nnn(val)

        parts = []
        i = 0

        while val > 0:
            chunk = val % 1000
            if chunk:
                text = self._convert_nnn(chunk)
                if THOUSANDS[i]:
                    text += ' ' + THOUSANDS[i]
                parts.append(text)
            val //= 1000
            i += 1

        return ' '.join(reversed(parts))

    def number_to_text(self, number):
        negative = number < 0
        number = abs(number)

        integer = int(number)
        decimal = str(number).split('.')

        result = self.khmer_number(integer)

        # decimal part
        if len(decimal) > 1 and int(decimal[1]) > 0:
            decimal_part = ' '.join(ONES[int(d)] for d in decimal[1])
            result = result + ' ចំណុច ' + decimal_part

        if negative:
            result = 'អវិជ្ជមាន ' + result

        return result

    def to_cardinal(self, number):
        return self.number_to_text(number)

    def to_ordinal(self, number):
        return self.to_cardinal(number)