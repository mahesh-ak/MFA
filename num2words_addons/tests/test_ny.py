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


class Num2WordsNYTest(TestCase):

    def test_and_join_199(self):
        self.assertEqual(
            num2words(199, lang='ny'),
            "zana limodzi ndi makumi asanu ndi anayi ndi zisanu ndi zinayi"
        )

    def test_ordinal(self):
        self.assertEqual(
            num2words(0, lang='ny', to='ordinal'),
            'ya ziro'
        )
        self.assertEqual(
            num2words(1, lang='ny', to='ordinal'),
            'ya imodzi'
        )
        self.assertEqual(
            num2words(13, lang='ny', to='ordinal'),
            'ya khumi ndi zitatu'
        )
        self.assertEqual(
            num2words(23, lang='ny', to='ordinal'),
            'ya makumi awiri ndi zitatu'
        )
        self.assertEqual(
            num2words(12, lang='ny', to='ordinal'),
            'ya khumi ndi ziwiri'
        )
        self.assertEqual(
            num2words(113, lang='ny', to='ordinal'),
            'ya zana limodzi ndi khumi ndi zitatu'
        )
        self.assertEqual(
            num2words(103, lang='ny', to='ordinal'),
            'ya zana limodzi ndi zitatu'
        )

    def test_cardinal(self):
        self.maxDiff=None
        self.assertEqual(
            num2words(130000, lang='ny'),
            "zana limodzi ndi makumi atatu zikwi"
        )
        self.assertEqual(
            num2words(242, lang='ny'),
            "zana ziwiri ndi makumi anayi ndi ziwiri"
        )
        self.assertEqual(
            num2words(800, lang='ny'),
            "zana zisanu ndi zitatu"
        )
        self.assertEqual(
            num2words(-203, lang='ny'),
            "minus zana ziwiri ndi zitatu"
        )
        self.assertEqual(
            num2words(1234567890, lang='ny'),
            "biliyoni imodzi ndi zana ziwiri ndi makumi atatu ndi zinayi miliyoni "
            "ndi zana zisanu ndi makumi asanu ndi limodzi ndi zisanu ndi ziwiri zikwi "
            "ndi zana zisanu ndi zitatu ndi makumi asanu ndi anayi"
        )
        
    def test_year(self):
        self.assertEqual(
            num2words(1398, lang='ny', to='year'),
            "zikwi chimodzi ndi zana zitatu ndi makumi asanu ndi anayi ndi zisanu ndi zitatu"
        )
        self.assertEqual(
            num2words(1399, lang='ny', to='year'),
            "zikwi chimodzi ndi zana zitatu ndi makumi asanu ndi anayi ndi zisanu ndi zinayi"
        )
        self.assertEqual(
            num2words(1400, lang='ny', to='year'),
            "zikwi chimodzi ndi zana zinayi"
        )

    def test_ordinal_num(self):
        self.assertEqual(num2words(10, lang='ny', to='ordinal_num'), '10')
        self.assertEqual(num2words(21, lang='ny', to='ordinal_num'), '21')
        self.assertEqual(num2words(102, lang='ny', to='ordinal_num'), '102')
        self.assertEqual(num2words(73, lang='ny', to='ordinal_num'), '73')

    def test_currency(self):
        self.assertEqual(
            num2words(1000, lang='ny', to='currency'),
            'zikwi chimodzi ndalama'
        )
        self.assertEqual(
            num2words(1500000, lang='ny', to='currency'),
            'miliyoni imodzi ndi zana zisanu zikwi ndalama'
        )
        
#    def test_cardinal_for_float_number(self):
#        self.assertEqual(num2words(12.5, lang='ny'),
#                         "goma sha biyu da biyar")
#        self.assertEqual(num2words(0.75, lang='ny'),
#                         "saba'in da biyar")
#        self.assertEqual(num2words(12.51, lang='ny'),
#                         "goma sha biyu da hamsin da ɗaya")
#        self.assertEqual(num2words(12.53, lang='ny'),
#                         "goma sha biyu da hamsin da uku")
#        self.assertEqual(num2words(12.59, lang='ny'),
#                         "goma sha biyu da hamsin da tara")
#        self.assertEqual(num2words(0.000001, lang='ny'),
#                         "ɗaya")

    def test_overflow(self):
        with self.assertRaises(OverflowError):
            num2words("1000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "00000000000000000000000000000000")
