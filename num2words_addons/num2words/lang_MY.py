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

from num2words.base import Num2Word_Base
from num2words.currency import parse_currency_parts
from num2words.utils import splitbyx

class Num2Word_MY(Num2Word_Base):

    
    def setup(self):
        self.negword = 'အနုတ်'
        self.pointword = 'ဒသမ'

        self.CURRENCY_FORMS = {
            'MMK': (('ကျပ်', 'ကျပ်'), ('ပြား', 'ပြား')),
            'USD': (('ဒေါ်လာ', 'ဒေါ်လာ'), ('ဆင့်', 'ဆင့်')),
        }

        self.high_numwords = []

        self.mid_numwords = ['', 'ဆယ်', 'ရာ', 'ထောင်', 'သောင်း', 'သိန်း', 'သန်း']

        self.low_numwords = [
            'သုည', 'တစ်', 'နှစ်', 'သုံး', 'လေး',
            'ငါး', 'ခြောက်', 'ခုနစ်', 'ရှစ်', 'ကိုး'
        ]

    def set_high_numwords(self, high_numwords):
        pass

    def set_mid_numwords(self, mid_numwords):
        pass

    def splitnum(self, six_num):
        word_num = ''

        for index, num in enumerate(map(int, six_num)):
            if num == 0:
                continue

            # units
            if index == 0:
                word_num += self.low_numwords[num]

            # tens
            elif index == 1:
                if num == 1:
                    word_num = 'ဆယ်' + word_num
                else:
                    word_num = self.low_numwords[num] + 'ဆယ်' + word_num

            # hundreds+
            else:
                word_num = (
                    self.low_numwords[num]
                    + self.mid_numwords[index]
                    + word_num
                )

        return word_num 

    def split_six(self, num_txt):
        result = splitbyx(num_txt, 6, format_int=False)
        result = list(result)[::-1]
        number_list = []
        for i in result:
            number_list.append(i[::-1])
        return number_list

    def add_text_million(self, word_num):
        result = ''

        for index, t in enumerate(reversed(word_num)):
            if index == 0:
                result = t
            else:
                result = result + 'သန်း' + t

        return result

    def round_2_decimal(self, number):
        integer, cents, negative = parse_currency_parts(
            number, is_int_with_cents=False
        )
        integer = '{}'.format(integer)
        cents = '{}'.format(cents)

        if len(cents) < 2:
            add_zero = 2 - len(cents)
            cents = ('0' * add_zero) + cents

        text_num = integer + '.' + cents

        return text_num, negative

    def left_num_to_text(self, number):

        left_num_list = self.split_six(number)

        left_text_list = []
        for i in left_num_list:
            left_text_list.append(self.splitnum(i))

        left_text = self.add_text_million(left_text_list)
        return left_text

    def to_cardinal(self, number):
        negative = number < 0

        pre, post = self.float2tuple(number)
        precision = self.precision
        pre = '{}'.format(pre)
        post = '{}'.format(post)

        if negative:
            pre = pre.lstrip('-')

        if len(post) < precision:
            post = ('0' * (precision - len(post))) + post

        # integer part
        if int(pre) == 0:
            result = self.low_numwords[0]
        else:
            result = self.left_num_to_text(pre)

        # decimal part
        if post.strip('0'):
            right_text = ''.join(self.low_numwords[int(i)] for i in post)
            result += self.pointword + right_text

        # pure zero
        if int(pre) == 0 and not post.strip('0'):
            return self.low_numwords[0]

        if negative:
            result = self.negword + result

        return result

    def to_ordinal(self, number):
        return self.to_cardinal(number)
    
    def to_currency(self, number, currency='MMK'):
        number, negative = self.round_2_decimal(number)

        left_num, right_num = number.split('.')

        left_text = self.left_num_to_text(left_num)
        right_text = self.splitnum(right_num[::-1].rstrip('0'))

        cr1, cr2 = self.CURRENCY_FORMS[currency]

        if right_num == '00':
            result = left_text + cr1[0]
        else:
            if left_num == '0':
                result = right_text + cr2[0]
            else:
                result = left_text + cr1[0] + right_text + cr2[0]

        if negative:
            result = self.negword + result

        return result