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


class Num2WordsSNTest(TestCase):

    def test_and_join_199(self):
        self.assertEqual(
            num2words(199, lang='sn'),
            "zana rimwe nemakumi mapfumbamwe nemapfumbamwe"
        )

    def test_ordinal(self):
        self.assertEqual(
            num2words(0, lang='sn', to='ordinal'),
            'ye zero'
        )
        self.assertEqual(
            num2words(1, lang='sn', to='ordinal'),
            'ye rimwe'
        )
        self.assertEqual(
            num2words(13, lang='sn', to='ordinal'),
            'ye gumi nematatu'
        )
        self.assertEqual(
            num2words(23, lang='sn', to='ordinal'),
            'ye makumi maviri nematatu'
        )
        self.assertEqual(
            num2words(12, lang='sn', to='ordinal'),
            'ye gumi nemaviri'
        )
        self.assertEqual(
            num2words(113, lang='sn', to='ordinal'),
            'ye zana rimwe negumi nematatu'
        )
        self.assertEqual(
            num2words(103, lang='sn', to='ordinal'),
            'ye zana rimwe nematatu'
        )

    def test_cardinal(self):
        self.assertEqual(
            num2words(130000, lang='sn'),
            "zviuru zana rimwe nemakumi matatu"
        )
        self.assertEqual(
            num2words(242, lang='sn'),
            "mazana maviri nemakumi mana nemaviri"
        )
        self.assertEqual(
            num2words(800, lang='sn'),
            "mazana masere"
        )
        self.assertEqual(
            num2words(-203, lang='sn'),
            "minus mazana maviri nematatu"
        )
        self.assertEqual(
            num2words(1234567890, lang='sn'),
            "bhiriyoni rimwe nemamiriyoni mazana maviri nemakumi matatu nemana "
            "nezviuru mazana mashanu nemakumi matanhatu nemanomwe "
            "nemazana masere nemakumi mapfumbamwe"
        )

    def test_year(self):
        self.assertEqual(
            num2words(1398, lang='sn', to='year'),
            "chiuru chimwe nemazana matatu nemakumi mapfumbamwe nemasere"
        )
        self.assertEqual(
            num2words(1399, lang='sn', to='year'),
            "chiuru chimwe nemazana matatu nemakumi mapfumbamwe nemapfumbamwe"
        )
        self.assertEqual(
            num2words(1400, lang='sn', to='year'),
            "chiuru chimwe nemazana mana"
        )

    def test_ordinal_num(self):
        self.assertEqual(num2words(10, lang='sn', to='ordinal_num'), '10')
        self.assertEqual(num2words(21, lang='sn', to='ordinal_num'), '21')
        self.assertEqual(num2words(102, lang='sn', to='ordinal_num'), '102')
        self.assertEqual(num2words(73, lang='sn', to='ordinal_num'), '73')

    def test_currency(self):
        self.assertEqual(
            num2words(1000, lang='sn', to='currency'),
            'chiuru chimwe mari'
        )
        self.assertEqual(
            num2words(1500000, lang='sn', to='currency'),
            'miriyoni rimwe nezviuru mazana mashanu mari'
        )
        
#    def test_cardinal_for_float_number(self):
#        self.assertEqual(num2words(12.5, lang='sn'),
#                         "goma sha biyu da biyar")
#        self.assertEqual(num2words(0.75, lang='sn'),
#                         "saba'in da biyar")
#        self.assertEqual(num2words(12.51, lang='sn'),
#                         "goma sha biyu da hamsin da ɗaya")
#        self.assertEqual(num2words(12.53, lang='sn'),
#                         "goma sha biyu da hamsin da uku")
#        self.assertEqual(num2words(12.59, lang='sn'),
#                         "goma sha biyu da hamsin da tara")
#        self.assertEqual(num2words(0.000001, lang='sn'),
#                         "ɗaya")

    def test_overflow(self):
        with self.assertRaises(OverflowError):
            num2words("1000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "00000000000000000000000000000000")
