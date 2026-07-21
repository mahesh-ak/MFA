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

class Num2WordsPSTest(TestCase):

    def test_and_join_199(self):
        self.assertEqual(num2words(199, lang='ps'), "سل او نوي او نهه")

    def test_ordinal(self):
        self.assertEqual(
            num2words(0, lang='ps', to='ordinal'),
            'صفرم'
        )
        self.assertEqual(
            num2words(1, lang='ps', to='ordinal'),
            'لومړی'
        )
        self.assertEqual(
            num2words(13, lang='ps', to='ordinal'),
            'دیارلسم'
        )
        self.assertEqual(
            num2words(23, lang='ps', to='ordinal'),
            'درې ویشتم'
        )
        self.assertEqual(
            num2words(12, lang='ps', to='ordinal'),
            'دوولسم'
        )
        self.assertEqual(
            num2words(113, lang='ps', to='ordinal'),
            'سل او دیارلسم'
        )
        self.assertEqual(
            num2words(103, lang='ps', to='ordinal'),
            'سل او درېیم'
        )

    def test_cardinal(self):
        self.assertEqual(num2words(130000, lang='ps'), "سل او دېرش زره")
        self.assertEqual(num2words(242, lang='ps'), "دوه سوه او دوه څلوېښت")
        self.assertEqual(num2words(800, lang='ps'), "اته سوه")
        self.assertEqual(num2words(-203, lang='ps'), "منفي دوه سوه او درې")
        self.assertEqual(
            num2words(1234567890, lang='ps'),
            "یو میلیارد او دوه سوه او څلور دېرش میلیون او "
            "پنځه سوه او اوه شپېته زره او اته سوه او نوي"
        )

    def test_year(self):
        self.assertEqual(
            num2words(1398, lang='ps', to='year'),
            "زر او درې سوه او اته نوي"
        )
        self.assertEqual(
            num2words(1399, lang='ps', to='year'),
            "زر او درې سوه او نهه نوي"
        )
        self.assertEqual(
            num2words(1400, lang='ps', to='year'),
            "زر او څلور سوه"
        )

    def test_currency(self):
        self.assertEqual(
            num2words(1000, lang='ps', to='currency'),
            'زر افغانۍ'
        )
        self.assertEqual(
            num2words(1500000, lang='ps', to='currency'),
            'یو میلیون او پنځه سوه زره افغانۍ'
        )

#    def test_ordinal_num(self):
#        self.assertEqual(num2words(10, lang='ps', to='ordinal_num'), '10م')
#        self.assertEqual(num2words(21, lang='ps', to='ordinal_num'), '21م')
#        self.assertEqual(num2words(102, lang='ps', to='ordinal_num'), '102م')
#        self.assertEqual(num2words(73, lang='ps', to='ordinal_num'), '73م')

    def test_cardinal_for_float_number(self):
        self.assertEqual(num2words(12.5, lang='ps'), "دولس او نیم")
        self.assertEqual(num2words(0.75, lang='ps'), "پنځه اویا صدم")
        self.assertEqual(num2words(12.51, lang='ps'),
                         "دولس او یو پنځوس صدم")
        self.assertEqual(num2words(12.53, lang='ps'),
                         "دولس او درې پنځوس صدم")
        self.assertEqual(num2words(12.59, lang='ps'),
                         "دولس او نهه پنځوس صدم")
        self.assertEqual(num2words(0.000001, lang='ps'),
                         "یو میلیونیم")