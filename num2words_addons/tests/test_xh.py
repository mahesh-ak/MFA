# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.
# Copyright (c) 2020, Hamidreza Kalbasi.  All Rights Reserved.

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

from unittest import TestCase

from num2words import num2words

class Num2WordsXHTest(TestCase):

    def test_and_join_199(self):
        self.assertEqual(
            num2words(199, lang='xh'),
            "ikhulu elinye namashumi asithoba anesithoba"
        )

    def test_ordinal(self):
        self.assertEqual(
            num2words(0, lang='xh', to='ordinal'),
            'ye zero'
        )
        self.assertEqual(
            num2words(1, lang='xh', to='ordinal'),
            'ye nye'
        )
        self.assertEqual(
            num2words(13, lang='xh', to='ordinal'),
            'ye lishumi elinesithathu'
        )
        self.assertEqual(
            num2words(23, lang='xh', to='ordinal'),
            'ye amashumi amabini anentathu'
        )
        self.assertEqual(
            num2words(12, lang='xh', to='ordinal'),
            'ye lishumi elinesibini'
        )
        self.assertEqual(
            num2words(113, lang='xh', to='ordinal'),
            'ye ikhulu elinye neshumi elinesithathu'
        )
        self.assertEqual(
            num2words(103, lang='xh', to='ordinal'),
            'ye ikhulu elinye nantathu'
        )

    def test_cardinal(self):
        self.assertEqual(
            num2words(130000, lang='xh'),
            "amawaka ikhulu elinye namashumi amathathu"
        )
        self.assertEqual(
            num2words(242, lang='xh'),
            "amakhulu amabini namashumi amane anembini"
        )
        self.assertEqual(
            num2words(800, lang='xh'),
            "amakhulu asibhozo"
        )
        self.assertEqual(
            num2words(-203, lang='xh'),
            "minus amakhulu amabini nantathu"
        )
        self.assertEqual(
            num2words(1234567890, lang='xh'),
            "ibhiliyoni esinye naizigidi amakhulu amabini namashumi amathathu anene "
            "namawaka amakhulu amahlanu namashumi amathandathu anesixhenxe "
            "namakhulu asibhozo namashumi asithoba"
        )

    def test_year(self):
        self.assertEqual(
            num2words(1398, lang='xh', to='year'),
            "iwaka elinye namakhulu amathathu namashumi asithoba anesibhozo"
        )
        self.assertEqual(
            num2words(1399, lang='xh', to='year'),
            "iwaka elinye namakhulu amathathu namashumi asithoba anesithoba"
        )
        self.assertEqual(
            num2words(1400, lang='xh', to='year'),
            "iwaka elinye namakhulu amane"
        )

    def test_ordinal_num(self):
        self.assertEqual(num2words(10, lang='xh', to='ordinal_num'), '10')
        self.assertEqual(num2words(21, lang='xh', to='ordinal_num'), '21')
        self.assertEqual(num2words(102, lang='xh', to='ordinal_num'), '102')
        self.assertEqual(num2words(73, lang='xh', to='ordinal_num'), '73')

    def test_currency(self):
        self.assertEqual(
            num2words(1000, lang='xh', to='currency'),
            'iwaka elinye imali'
        )
        self.assertEqual(
            num2words(1500000, lang='xh', to='currency'),
            'isigidi esinye namawaka amakhulu amahlanu imali'
        )