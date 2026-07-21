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


class Num2WordsCKBTest(TestCase):
    def test_and_join_199(self):
        self.assertEqual(num2words(199, lang='ckb'), "سەد و نەوەد و نۆ")

    def test_ordinal(self):
        self.assertEqual(
            num2words(0, lang='ckb', to='ordinal'),
            'سفرەم'
        )
        self.assertEqual(
            num2words(1, lang='ckb', to='ordinal'),
            'یەکەم'
        )
        self.assertEqual(
            num2words(13, lang='ckb', to='ordinal'),
            'سێزدەم'
        )
        self.assertEqual(
            num2words(23, lang='ckb', to='ordinal'),
            'بیست و سێیەم'
        )
        self.assertEqual(
            num2words(12, lang='ckb', to='ordinal'),
            'دوازدەیەم'
        )
        self.assertEqual(
            num2words(113, lang='ckb', to='ordinal'),
            'سەد و سێزدەم'
        )
        self.assertEqual(
            num2words(103, lang='ckb', to='ordinal'),
            'سەد و سێیەم'
        )

    def test_cardinal(self):
        self.assertEqual(num2words(130000, lang='ckb'), "سەد و سی هەزار")
        self.assertEqual(num2words(242, lang='ckb'), "دووسەد و چل و دوو")
        self.assertEqual(num2words(800, lang='ckb'), "هەشتسەد")
        self.assertEqual(num2words(-203, lang='ckb'), "منفی دووسەد و سێ")
        self.assertEqual(
            num2words(1234567890, lang='ckb'),
            "یەک ملیار و دووسەد و سی و چوار ملیۆن و"
            " پێنجسەد و شەست و حەوت هەزار و هەشتسەد و نەوەد"
        )

    def test_year(self):
        self.assertEqual(num2words(1398, lang='ckb', to='year'),
                         "هەزار و سێسەد و نەوەد و هەشت")
        self.assertEqual(num2words(1399, lang='ckb', to='year'),
                         "هەزار و سێسەد و نەوەد و نۆ")
        self.assertEqual(
            num2words(1400, lang='ckb', to='year'), "هەزار و چوارسەد")

    def test_currency(self):
        self.assertEqual(
            num2words(1000, lang='ckb', to='currency'), 'هەزار دینار')
        self.assertEqual(
            num2words(1500000, lang='ckb', to='currency'),
            'یەک ملیۆن و پێنجسەد هەزار دینار'
        )

    def test_ordinal_num(self):
        self.assertEqual(num2words(10, lang='ckb', to='ordinal_num'), '10ەم')
        self.assertEqual(num2words(21, lang='ckb', to='ordinal_num'), '21ەم')
        self.assertEqual(num2words(102, lang='ckb', to='ordinal_num'), '102ەم')
        self.assertEqual(num2words(73, lang='ckb', to='ordinal_num'), '73ەم')

    def test_cardinal_for_float_number(self):
        self.assertEqual(num2words(12.5, lang='ckb'), "دوازدە و نیو")
        self.assertEqual(num2words(0.75, lang='ckb'), "حەفتا و پێنج سەدەم")
        self.assertEqual(num2words(12.51, lang='ckb'),
                         "دوازدە و پەنجا و یەک سەدەم")
        self.assertEqual(num2words(12.53, lang='ckb'),
                         "دوازدە و پەنجا و سێ سەدەم")
        self.assertEqual(num2words(12.59, lang='ckb'),
                         "دوازدە و پەنجا و نۆ سەدەم")
        self.assertEqual(num2words(0.000001, lang='ckb'), "یەک ملیۆنەم")

    def test_overflow(self):
        with self.assertRaises(OverflowError):
            num2words("1000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "00000000000000000000000000000000")