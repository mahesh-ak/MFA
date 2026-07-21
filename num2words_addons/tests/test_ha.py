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



class Num2WordsHATest(TestCase):

    def test_and_join_199(self):
        self.assertEqual(num2words(199, lang='ha'),
                         "ɗari da casa'in da tara")

    def test_ordinal(self):
        self.assertEqual(
            num2words(0, lang='ha', to='ordinal'),
            'na sifili'
        )
        self.assertEqual(
            num2words(1, lang='ha', to='ordinal'),
            'na ɗaya'
        )
        self.assertEqual(
            num2words(13, lang='ha', to='ordinal'),
            'na goma sha uku'
        )
        self.assertEqual(
            num2words(23, lang='ha', to='ordinal'),
            'na ashirin da uku'
        )
        self.assertEqual(
            num2words(12, lang='ha', to='ordinal'),
            'na goma sha biyu'
        )
        self.assertEqual(
            num2words(113, lang='ha', to='ordinal'),
            'na ɗari da goma sha uku'
        )
        self.assertEqual(
            num2words(103, lang='ha', to='ordinal'),
            'na ɗari da uku'
        )

    def test_cardinal(self):
        self.assertEqual(num2words(130000, lang='ha'),
                         "dubu ɗari da talatin")
        self.assertEqual(num2words(242, lang='ha'),
                         "ɗari biyu da arba'in da biyu")
        self.assertEqual(num2words(800, lang='ha'),
                         "ɗari takwas")
        self.assertEqual(num2words(-203, lang='ha'),
                         "minus ɗari biyu da uku")
        self.assertEqual(
            num2words(1234567890, lang='ha'),
            "biliyan ɗaya da miliyan ɗari biyu da talatin da huɗu "
            "da dubu ɗari biyar da sittin da bakwai "
            "da ɗari takwas da casa'in"
        )

    def test_year(self):
        self.assertEqual(num2words(1398, lang='ha', to='year'),
                         "dubu da ɗari uku da casa'in da takwas")
        self.assertEqual(num2words(1399, lang='ha', to='year'),
                         "dubu da ɗari uku da casa'in da tara")
        self.assertEqual(
            num2words(1400, lang='ha', to='year'),
            "dubu da ɗari huɗu"
        )


    def test_ordinal_num(self):
        self.assertEqual(num2words(10, lang='ha', to='ordinal_num'), '10')
        self.assertEqual(num2words(21, lang='ha', to='ordinal_num'), '21')
        self.assertEqual(num2words(102, lang='ha', to='ordinal_num'), '102')
        self.assertEqual(num2words(73, lang='ha', to='ordinal_num'), '73')

    def test_currency(self):
        self.assertEqual(
            num2words(1000, lang='ha', to='currency'),
            'dubu kuɗi'
        )
        self.assertEqual(
            num2words(1500000, lang='ha', to='currency'),
            'miliyan ɗaya da dubu ɗari biyar kuɗi'
        )


#    def test_cardinal_for_float_number(self):
#        self.assertEqual(num2words(12.5, lang='ha'),
#                         "goma sha biyu da biyar")
#        self.assertEqual(num2words(0.75, lang='ha'),
#                         "saba'in da biyar")
#        self.assertEqual(num2words(12.51, lang='ha'),
#                         "goma sha biyu da hamsin da ɗaya")
#        self.assertEqual(num2words(12.53, lang='ha'),
#                         "goma sha biyu da hamsin da uku")
#        self.assertEqual(num2words(12.59, lang='ha'),
#                         "goma sha biyu da hamsin da tara")
#        self.assertEqual(num2words(0.000001, lang='ha'),
#                         "ɗaya")

    def test_overflow(self):
        with self.assertRaises(OverflowError):
            num2words("1000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "00000000000000000000000000000000")
