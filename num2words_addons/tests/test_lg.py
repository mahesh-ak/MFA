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


class Num2WordsLGTest(TestCase):

    def test_and_join_199(self):
        self.assertEqual(
            num2words(199, lang='lg'),
            "kikumi mu amakumi mwenda mu mwenda"
        )

    def test_ordinal(self):
        self.assertEqual(
            num2words(0, lang='lg', to='ordinal'),
            'eya zeero'
        )
        self.assertEqual(
            num2words(1, lang='lg', to='ordinal'),
            'eya emu'
        )
        self.assertEqual(
            num2words(13, lang='lg', to='ordinal'),
            'eya kkumi na ssatu'
        )
        self.assertEqual(
            num2words(23, lang='lg', to='ordinal'),
            'eya amakumi abiri mu ssatu'
        )
        self.assertEqual(
            num2words(12, lang='lg', to='ordinal'),
            'eya kkumi na bbiri'
        )
        self.assertEqual(
            num2words(113, lang='lg', to='ordinal'),
            'eya kikumi mu kkumi na ssatu'
        )
        self.assertEqual(
            num2words(103, lang='lg', to='ordinal'),
            'eya kikumi mu ssatu'
        )

    def test_cardinal(self):
        self.assertEqual(
            num2words(130000, lang='lg'),
            "lukumi kikumi mu amakumi asatu"
        )
        self.assertEqual(
            num2words(242, lang='lg'),
            "bibiri mu amakumi ana mu bbiri"
        )
        self.assertEqual(
            num2words(800, lang='lg'),
            "munaana"
        )
        self.assertEqual(
            num2words(-203, lang='lg'),
            "minus bibiri mu ssatu"
        )
        self.assertEqual(
            num2words(1234567890, lang='lg'),
            "bukadde emu mu kakadde bibiri mu amakumi asatu mu nnya "
            "mu lukumi bitaano mu amakumi mukaaga mu musanvu "
            "mu munaana mu amakumi mwenda"
        )

    def test_year(self):
        self.assertEqual(
            num2words(1398, lang='lg', to='year'),
            "lukumi emu mu bisatu mu amakumi mwenda mu munaana"
        )
        self.assertEqual(
            num2words(1399, lang='lg', to='year'),
            "lukumi emu mu bisatu mu amakumi mwenda mu mwenda"
        )
        self.assertEqual(
            num2words(1400, lang='lg', to='year'),
            "lukumi emu mu bina"
        )

    def test_ordinal_num(self):
        self.assertEqual(num2words(10, lang='lg', to='ordinal_num'), '10')
        self.assertEqual(num2words(21, lang='lg', to='ordinal_num'), '21')
        self.assertEqual(num2words(102, lang='lg', to='ordinal_num'), '102')
        self.assertEqual(num2words(73, lang='lg', to='ordinal_num'), '73')

    def test_currency(self):
        self.assertEqual(
            num2words(1000, lang='lg', to='currency'),
            'lukumi emu ssente'
        )
        self.assertEqual(
            num2words(1500000, lang='lg', to='currency'),
            'kakadde emu mu lukumi bitaano ssente'
        )
        
#    def test_cardinal_for_float_number(self):
#        self.assertEqual(num2words(12.5, lang='lg'),
#                         "goma sha biyu da biyar")
#        self.assertEqual(num2words(0.75, lang='lg'),
#                         "saba'in da biyar")
#        self.assertEqual(num2words(12.51, lang='lg'),
#                         "goma sha biyu da hamsin da ɗaya")
#        self.assertEqual(num2words(12.53, lang='lg'),
#                         "goma sha biyu da hamsin da uku")
#        self.assertEqual(num2words(12.59, lang='lg'),
#                         "goma sha biyu da hamsin da tara")
#        self.assertEqual(num2words(0.000001, lang='lg'),
#                         "ɗaya")

    def test_overflow(self):
        with self.assertRaises(OverflowError):
            num2words("1000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "00000000000000000000000000000000")
