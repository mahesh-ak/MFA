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


class Num2WordsCEBTest(TestCase):

    def test_and_join_199(self):
        self.assertEqual(
            num2words(199, lang='ceb'),
            "usa ka gatos ug nubenta ug siyam"
        )

    def test_ordinal(self):
        self.assertEqual(
            num2words(0, lang='ceb', to='ordinal'),
            'ika-sero'
        )
        self.assertEqual(
            num2words(1, lang='ceb', to='ordinal'),
            'ika-usa'
        )
        self.assertEqual(
            num2words(13, lang='ceb', to='ordinal'),
            'ika-trese'
        )
        self.assertEqual(
            num2words(23, lang='ceb', to='ordinal'),
            'ika-baynte ug tulo'
        )
        self.assertEqual(
            num2words(12, lang='ceb', to='ordinal'),
            'ika-dose'
        )
        self.assertEqual(
            num2words(113, lang='ceb', to='ordinal'),
            'ika-usa ka gatos ug trese'
        )
        self.assertEqual(
            num2words(103, lang='ceb', to='ordinal'),
            'ika-usa ka gatos ug tulo'
        )

    def test_cardinal(self):
        self.assertEqual(
            num2words(130000, lang='ceb'),
            "usa ka gatos ug traynta ka libo"
        )
        self.assertEqual(
            num2words(242, lang='ceb'),
            "duha ka gatos ug kwarenta ug duha"
        )
        self.assertEqual(
            num2words(800, lang='ceb'),
            "walo ka gatos"
        )
        self.assertEqual(
            num2words(-203, lang='ceb'),
            "minus duha ka gatos ug tulo"
        )
        self.assertEqual(
            num2words(1234567890, lang='ceb'),
            "usa ka bilyon ug duha ka gatos ug traynta ug upat ka milyon ug "
            "lima ka gatos ug sesenta ug pito ka libo ug "
            "walo ka gatos ug nubenta"
        )

    def test_year(self):
        self.assertEqual(
            num2words(1398, lang='ceb', to='year'),
            "usa ka libo ug tulo ka gatos ug nubenta ug walo"
        )
        self.assertEqual(
            num2words(1399, lang='ceb', to='year'),
            "usa ka libo ug tulo ka gatos ug nubenta ug siyam"
        )
        self.assertEqual(
            num2words(1400, lang='ceb', to='year'),
            "usa ka libo ug upat ka gatos"
        )

    def test_currency(self):
        self.assertEqual(
            num2words(1000, lang='ceb', to='currency'),
            'usa ka libo pesos'
        )
        self.assertEqual(
            num2words(1500000, lang='ceb', to='currency'),
            'usa ka milyon ug lima ka gatos ka libo pesos'
        )

    def test_ordinal_num(self):
        self.assertEqual(num2words(10, lang='ceb', to='ordinal_num'), '10')
        self.assertEqual(num2words(21, lang='ceb', to='ordinal_num'), '21')
        self.assertEqual(num2words(102, lang='ceb', to='ordinal_num'), '102')
        self.assertEqual(num2words(73, lang='ceb', to='ordinal_num'), '73')
        
#    def test_cardinal_for_float_number(self):
#        self.assertEqual(num2words(12.5, lang='ceb'), "دوازده و نیم")
#        self.assertEqual(num2words(0.75, lang='ceb'), "هفتاد و پنج صدم")
#        self.assertEqual(num2words(12.51, lang='ceb'),
#                         "دوازده و پنجاه و یک صدم")
#        self.assertEqual(num2words(12.53, lang='ceb'),
#                         "دوازده و پنجاه و سه صدم")
#        self.assertEqual(num2words(12.59, lang='ceb'),
#                         "دوازده و پنجاه و نه صدم")
#        self.assertEqual(num2words(0.000001, lang='ceb'), "یک میلیونیم")

#    def test_overflow(self):
#        with self.assertRaises(OverflowError):
#            num2words("1000000000000000000000000000000000000000000000000000000"
#                      "0000000000000000000000000000000000000000000000000000000"
#                      "0000000000000000000000000000000000000000000000000000000"
#                      "0000000000000000000000000000000000000000000000000000000"
#                      "0000000000000000000000000000000000000000000000000000000"
#                      "00000000000000000000000000000000")
