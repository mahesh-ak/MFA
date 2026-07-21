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

class Num2WordsZUTest(TestCase):

    def test_and_join_199(self):
        self.assertEqual(
            num2words(199, lang='zu'),
            "ikhulu elinye namashumi ayisishiyagalolunye nesishiyagalolunye"
        )

    def test_ordinal(self):
        self.assertEqual(
            num2words(0, lang='zu', to='ordinal'),
            'ye zero'
        )
        self.assertEqual(
            num2words(1, lang='zu', to='ordinal'),
            'ye nye'
        )
        self.assertEqual(
            num2words(13, lang='zu', to='ordinal'),
            'ye lishumi nantathu'
        )
        self.assertEqual(
            num2words(23, lang='zu', to='ordinal'),
            'ye amashumi amabili nantathu'
        )
        self.assertEqual(
            num2words(12, lang='zu', to='ordinal'),
            'ye lishumi nambili'
        )
        self.assertEqual(
            num2words(113, lang='zu', to='ordinal'),
            'ye ikhulu elinye neshumi nantathu'
        )
        self.assertEqual(
            num2words(103, lang='zu', to='ordinal'),
            'ye ikhulu elinye nantathu'
        )

    def test_cardinal(self):
        self.assertEqual(
            num2words(130000, lang='zu'),
            "amawaka ikhulu elinye namashumi amathathu"
        )
        self.assertEqual(
            num2words(242, lang='zu'),
            "amakhulu amabili namashumi amane nambili"
        )
        self.assertEqual(
            num2words(800, lang='zu'),
            "amakhulu ayisishiyagalombili"
        )
        self.assertEqual(
            num2words(-203, lang='zu'),
            "minus amakhulu amabili nantathu"
        )
        self.assertEqual(
            num2words(1234567890, lang='zu'),
            "ibhiliyoni esinye nezigidi amakhulu amabili namashumi amathathu nane "
            "namawaka amakhulu amahlanu namashumi ayisithupha nesikhombisa "
            "namakhulu ayisishiyagalombili namashumi ayisishiyagalolunye"
        )

    def test_year(self):
        self.assertEqual(
            num2words(1398, lang='zu', to='year'),
            "inkulungwane eyodwa namakhulu amathathu namashumi ayisishiyagalolunye nesishiyagalombili"
        )
        self.assertEqual(
            num2words(1399, lang='zu', to='year'),
            "inkulungwane eyodwa namakhulu amathathu namashumi ayisishiyagalolunye nesishiyagalolunye"
        )
        self.assertEqual(
            num2words(1400, lang='zu', to='year'),
            "inkulungwane eyodwa namakhulu amane"
        )

    def test_ordinal_num(self):
        self.assertEqual(num2words(10, lang='zu', to='ordinal_num'), '10')
        self.assertEqual(num2words(21, lang='zu', to='ordinal_num'), '21')
        self.assertEqual(num2words(102, lang='zu', to='ordinal_num'), '102')
        self.assertEqual(num2words(73, lang='zu', to='ordinal_num'), '73')

    def test_currency(self):
        self.assertEqual(
            num2words(1000, lang='zu', to='currency'),
            'inkulungwane eyodwa imali'
        )
        self.assertEqual(
            num2words(1500000, lang='zu', to='currency'),
            'isigidi esinye namawaka amakhulu amahlanu imali'
        )