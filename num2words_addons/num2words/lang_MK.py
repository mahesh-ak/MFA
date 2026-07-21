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

from .base import Num2Word_Base
from .currency import parse_currency_parts, prefix_currency
from .utils import get_digits, splitbyx


ZERO = ('нула',)

ONES = {
    1: ('еден',),
    2: ('два',),
    3: ('три',),
    4: ('четири',),
    5: ('пет',),
    6: ('шест',),
    7: ('седум',),
    8: ('осум',),
    9: ('девет',),
}

TENS = {
    0: ('десет',),
    1: ('единаесет',),
    2: ('дванаесет',),
    3: ('тринаесет',),
    4: ('четиринаесет',),
    5: ('петнаесет',),
    6: ('шеснаесет',),
    7: ('седумнаесет',),
    8: ('осумнаесет',),
    9: ('деветнаесет',),
}

TWENTIES = {
    2: ('дваесет',),
    3: ('триесет',),
    4: ('четириесет',),
    5: ('педесет',),
    6: ('шеесет',),
    7: ('седумдесет',),
    8: ('осумдесет',),
    9: ('деведесет',),
}

HUNDREDS = {
    1: ('сто',),
    2: ('двесте',),
    3: ('триста',),
    4: ('четиристотини',),
    5: ('петстотини',),
    6: ('шестстотини',),
    7: ('седумстотини',),
    8: ('осумстотини',),
    9: ('деветстотини',),
}

SCALE = {
    0: ('', '', '', False),
    1: ('илјада', 'илјади', 'илјади', True),
    2: ('милион', 'милиони', 'милиони', False),
    3: ('милијарда', 'милијарди', 'милијарди', False),
    4: ('трилион', 'трилиони', 'трилиони', False),
    5: ('квадрилион', 'квадрилиони', 'квадрилиони', False),
}


class Num2Word_MK(Num2Word_Base):

    def setup(self):
        self.negword = "минус"
        self.pointword = "запирка"

    def to_cardinal(self, number, feminine=False):
        n = str(number).replace(',', '.')
        if '.' in n:
            left, right = n.split('.')
            leading_zero_count = len(right) - len(right.lstrip('0'))

            decimal_part = (
                (ZERO[0] + ' ') * leading_zero_count +
                self._int2word(int(right))
            )

            return '%s %s %s' % (
                self._int2word(int(left)),
                self.pointword,
                decimal_part
            )
        else:
            return self._int2word(int(n))

    def pluralize(self, number, forms):
        if number == 1:
            return forms[0]
        return forms[1]

    def to_ordinal(self, number):
        raise NotImplementedError()

    def _int2word(self, number):
        if number < 0:
            return ' '.join([self.negword, self._int2word(abs(number))])

        if number == 0:
            return ZERO[0]

        words = []
        chunks = list(splitbyx(str(number), 3))
        chunk_len = len(chunks)

        for chunk in chunks:
            chunk_len -= 1
            digit_right, digit_mid, digit_left = get_digits(chunk)

            if digit_left > 0:
                words.append(HUNDREDS[digit_left][0])

            if digit_mid > 1:
                words.append(TWENTIES[digit_mid][0])

            if digit_mid == 1:
                words.append(TENS[digit_right][0])
            elif digit_right > 0:
                words.append(ONES[digit_right][0])

            if chunk_len > 0 and chunk != 0:
                scale_word = self.pluralize(chunk, SCALE[chunk_len])
                words.append(scale_word)

        return ' '.join(words)

    def to_currency(self, val, currency='EUR', cents=True,
                    separator=',', adjective=False):

        left, right, is_negative = parse_currency_parts(val)

        minus_str = "%s " % self.negword if is_negative else ""

        # Simplified Macedonian currency handling
        currency_main = {
            'EUR': ('евро', 'евра'),
            'MKD': ('денар', 'денари'),
        }

        currency_sub = {
            'EUR': ('цент', 'центи'),
            'MKD': ('денар', 'денари'),
        }

        cr1 = currency_main.get(currency, ('', ''))
        cr2 = currency_sub.get(currency, ('', ''))

        return '%s%s %s%s %s %s' % (
            minus_str,
            self.to_cardinal(left),
            cr1[0] if left == 1 else cr1[1],
            separator,
            self.to_cardinal(right),
            cr2[0] if right == 1 else cr2[1],
        )