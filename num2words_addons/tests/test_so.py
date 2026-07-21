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



class Num2WordsSOTest(TestCase):

    def test_and_join_199(self):
        self.assertEqual(num2words(199, lang='so'),
                         "boqol iyo sagaashan iyo sagaal")

    def test_ordinal(self):
        self.assertEqual(
            num2words(0, lang='so', to='ordinal'),
            'ka eber'
        )
        self.assertEqual(
            num2words(1, lang='so', to='ordinal'),
            'ka kow'
        )
        self.assertEqual(
            num2words(13, lang='so', to='ordinal'),
            'ka toban iyo saddex'
        )
        self.assertEqual(
            num2words(23, lang='so', to='ordinal'),
            'ka labaatan iyo saddex'
        )
        self.assertEqual(
            num2words(12, lang='so', to='ordinal'),
            'ka toban iyo laba'
        )
        self.assertEqual(
            num2words(113, lang='so', to='ordinal'),
            'ka boqol iyo toban iyo saddex'
        )
        self.assertEqual(
            num2words(103, lang='so', to='ordinal'),
            'ka boqol iyo saddex'
        )

    def test_cardinal(self):
        self.assertEqual(num2words(130000, lang='so'),
                         "boqol iyo soddon kun")
        self.assertEqual(num2words(242, lang='so'),
                         "laba boqol iyo afartan iyo laba")
        self.assertEqual(num2words(800, lang='so'),
                         "siddeed boqol")
        self.assertEqual(num2words(-203, lang='so'),
                         "minus laba boqol iyo saddex")
        self.assertEqual(
            num2words(1234567890, lang='so'),
            "kow bilyan iyo laba boqol iyo soddon iyo afar milyan "
            "iyo shan boqol iyo lixdan iyo toddoba kun "
            "iyo siddeed boqol iyo sagaashan"
        )

    def test_year(self):
        self.assertEqual(num2words(1398, lang='so', to='year'),
                         "kun iyo saddex boqol iyo sagaashan iyo siddeed")
        self.assertEqual(num2words(1399, lang='so', to='year'),
                         "kun iyo saddex boqol iyo sagaashan iyo sagaal")
        self.assertEqual(
            num2words(1400, lang='so', to='year'),
            "kun iyo afar boqol"
        )

    def test_ordinal_num(self):
        self.assertEqual(num2words(10, lang='so', to='ordinal_num'), '10')
        self.assertEqual(num2words(21, lang='so', to='ordinal_num'), '21')
        self.assertEqual(num2words(102, lang='so', to='ordinal_num'), '102')
        self.assertEqual(num2words(73, lang='so', to='ordinal_num'), '73')

    def test_currency(self):
        self.assertEqual(
            num2words(1000, lang='so', to='currency'),
            'kun lacag'
        )
        self.assertEqual(
            num2words(1500000, lang='so', to='currency'),
            'kow milyan iyo shan boqol kun lacag'
        )

#    def test_cardinal_for_float_number(self):
#        self.assertEqual(num2words(12.5, lang='so'),
#                         "goma sha biyu da biyar")
#        self.assertEqual(num2words(0.75, lang='so'),
#                         "saba'in da biyar")
#        self.assertEqual(num2words(12.51, lang='so'),
#                         "goma sha biyu da hamsin da ɗaya")
#        self.assertEqual(num2words(12.53, lang='so'),
#                         "goma sha biyu da hamsin da uku")
#        self.assertEqual(num2words(12.59, lang='so'),
#                         "goma sha biyu da hamsin da tara")
#        self.assertEqual(num2words(0.000001, lang='so'),
#                         "ɗaya")

    def test_overflow(self):
        with self.assertRaises(OverflowError):
            num2words("1000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "00000000000000000000000000000000")
