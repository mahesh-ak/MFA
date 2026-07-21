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


class Num2WordsSWTest(TestCase):

    def test_and_join_199(self):
        self.assertEqual(
            num2words(199, lang='sw'),
            "mia moja na tisini na tisa"
        )

    def test_ordinal(self):
        self.assertEqual(
            num2words(0, lang='sw', to='ordinal'),
            'ya sifuri'
        )
        self.assertEqual(
            num2words(1, lang='sw', to='ordinal'),
            'ya moja'
        )
        self.assertEqual(
            num2words(13, lang='sw', to='ordinal'),
            'ya kumi na tatu'
        )
        self.assertEqual(
            num2words(23, lang='sw', to='ordinal'),
            'ya ishirini na tatu'
        )
        self.assertEqual(
            num2words(12, lang='sw', to='ordinal'),
            'ya kumi na mbili'
        )
        self.assertEqual(
            num2words(113, lang='sw', to='ordinal'),
            'ya mia moja na kumi na tatu'
        )
        self.assertEqual(
            num2words(103, lang='sw', to='ordinal'),
            'ya mia moja na tatu'
        )

    def test_cardinal(self):
        self.assertEqual(
            num2words(130000, lang='sw'),
            "elfu mia moja na thelathini"
        )
        self.assertEqual(
            num2words(242, lang='sw'),
            "mia mbili na arobaini na mbili"
        )
        self.assertEqual(
            num2words(800, lang='sw'),
            "mia nane"
        )
        self.assertEqual(
            num2words(-203, lang='sw'),
            "minus mia mbili na tatu"
        )
        self.assertEqual(
            num2words(1234567890, lang='sw'),
            "bilioni moja na milioni mia mbili na thelathini na nne "
            "na elfu mia tano na sitini na saba "
            "na mia nane na tisini"
        )

    def test_year(self):
        self.assertEqual(
            num2words(1398, lang='sw', to='year'),
            "elfu moja na mia tatu na tisini na nane"
        )
        self.assertEqual(
            num2words(1399, lang='sw', to='year'),
            "elfu moja na mia tatu na tisini na tisa"
        )
        self.assertEqual(
            num2words(1400, lang='sw', to='year'),
            "elfu moja na mia nne"
        )

    def test_ordinal_num(self):
        self.assertEqual(num2words(10, lang='sw', to='ordinal_num'), '10')
        self.assertEqual(num2words(21, lang='sw', to='ordinal_num'), '21')
        self.assertEqual(num2words(102, lang='sw', to='ordinal_num'), '102')
        self.assertEqual(num2words(73, lang='sw', to='ordinal_num'), '73')

    def test_currency(self):
        self.assertEqual(
            num2words(1000, lang='sw', to='currency'),
            'elfu moja pesa'
        )
        self.assertEqual(
            num2words(1500000, lang='sw', to='currency'),
            'milioni moja na elfu mia tano pesa'
        )
        
#    def test_cardinal_for_float_number(self):
#        self.assertEqual(num2words(12.5, lang='sw'),
#                         "goma sha biyu da biyar")
#        self.assertEqual(num2words(0.75, lang='sw'),
#                         "saba'in da biyar")
#        self.assertEqual(num2words(12.51, lang='sw'),
#                         "goma sha biyu da hamsin da ɗaya")
#        self.assertEqual(num2words(12.53, lang='sw'),
#                         "goma sha biyu da hamsin da uku")
#        self.assertEqual(num2words(12.59, lang='sw'),
#                         "goma sha biyu da hamsin da tara")
#        self.assertEqual(num2words(0.000001, lang='sw'),
#                         "ɗaya")

    def test_overflow(self):
        with self.assertRaises(OverflowError):
            num2words("1000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "00000000000000000000000000000000")
