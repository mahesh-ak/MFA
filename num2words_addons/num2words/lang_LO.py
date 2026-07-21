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

class Num2Word_LO(Num2Word_Base):

    def setup(self):
        self.negword = 'ລົບ'
        self.pointword = 'ຈຸດ'

        self.CURRENCY_FORMS = {
            'LAK': (('ກີບ', 'ກີບ'), ('ສະຕາງ', 'ສະຕາງ')),
            'USD': (('ໂດລາ', 'ໂດລາ'), ('ເຊັນ', 'ເຊັນ')),
            'EUR': (('ຢູໂຣ', 'ຢູໂຣ'), ('ເຊັນ', 'ເຊັນ')),
        }

        self.high_numwords = []

        self.mid_numwords = ['', 'ສິບ', 'ຮ້ອຍ', 'ພັນ', 'ໝື່ນ', 'ແສນ', 'ລ້ານ']

        self.low_numwords = [
            'ສູນ', 'ໜຶ່ງ', 'ສອງ', 'ສາມ', 'ສີ່',
            'ຫ້າ', 'ຫົກ', 'ເຈັດ', 'ແປດ', 'ເກົ້າ'
        ]

    def set_high_numwords(self, high_numwords):
        pass

    def set_mid_numwords(self, mid_numwords):
        pass

    def splitnum(self, six_num):
        length = len(six_num) > 1
        word_num = ''

        for index, num in enumerate(map(int, six_num)):
            if num == 0:
                continue

            # --- units (index 0) ---
            if index == 0:
                if length and num == 1:
                    word_num += 'ເອັດ'
                else:
                    word_num += self.low_numwords[num]

            # --- tens (index 1) ---
            elif index == 1:
                if num == 1:
                    word_num = 'ສິບ' + word_num
                elif num == 2:
                    word_num = 'ຊາວ' + word_num
                else:
                    word_num = self.low_numwords[num] + 'ສິບ' + word_num

            # --- hundreds and above ---
            else:
                word_num = (
                    self.low_numwords[num]
                    + self.mid_numwords[index]
                    + word_num
                )

        # handle zero
        if not word_num:
            return '' #self.low_numwords[0]

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
                result = result + 'ລ້ານ' + t

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
            add_zero = precision - len(post)
            post = ('0' * add_zero) + post

        if int(pre) == 0: 
            result = self.low_numwords[0] 
        else: 
            result = self.left_num_to_text(pre)

        right_text = ''
        if not post == '0':
            for i in map(int, post):
                right_text = right_text + self.low_numwords[i]
            result = result + self.pointword + right_text
        
        if int(pre) == 0 and not post.strip('0'):
            return self.low_numwords[0]

        if negative:
            result = self.negword + result

        return result

    def to_ordinal(self, number):
        return self.to_cardinal(number)

    def to_currency(self, number, currency='LAK'):

        number, negative = self.round_2_decimal(number)

        split_num = number.split('.')

        left_num = split_num[0]
        left_text = self.left_num_to_text(left_num)

        right_num = split_num[1]
        right_text = self.splitnum(right_num[::-1].rstrip('0'))

        try:
            cr1, cr2 = self.CURRENCY_FORMS[currency]

        except KeyError:
            raise NotImplementedError(
                'Currency code "%s" not implemented for "%s"' %
                (currency, self.__class__.__name__))

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