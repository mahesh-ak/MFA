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

class Num2WordsFFTest(TestCase):

    def test_and_join_199(self):
        self.assertEqual(
            num2words(199, lang='ff'),
            "teemedere go'o e cappanɗe jowiɗi e ɗiɗi e jowiɗi e ɗiɗi"
        )

    def test_ordinal(self):
        self.assertEqual(
            num2words(0, lang='ff', to='ordinal'),
            'sifero'
        )
        self.assertEqual(
            num2words(1, lang='ff', to='ordinal'),
            'go\'o'
        )
        self.assertEqual(
            num2words(13, lang='ff', to='ordinal'),
            'sappo e tati'
        )
        self.assertEqual(
            num2words(23, lang='ff', to='ordinal'),
            'cappanɗe ɗiɗi e tati'
        )
        self.assertEqual(
            num2words(12, lang='ff', to='ordinal'),
            'sappo e ɗiɗi'
        )
        self.assertEqual(
            num2words(113, lang='ff', to='ordinal'),
            'teemedere go\'o e sappo e tati'
        )
        self.assertEqual(
            num2words(103, lang='ff', to='ordinal'),
            'teemedere go\'o e tati'
        )

    def test_cardinal(self):
        self.assertEqual(
            num2words(130000, lang='ff'),
            "teemedere go'o e cappanɗe tati dubu"
        )
        self.assertEqual(
            num2words(242, lang='ff'),
            "teemedere ɗiɗi e cappanɗe nay e ɗiɗi"
        )
        self.assertEqual(
            num2words(800, lang='ff'),
            "teemedere jowiɗi e go'o"
        )
        self.assertEqual(
            num2words(-203, lang='ff'),
            "minus teemedere ɗiɗi e tati"
        )
        self.assertEqual(
            num2words(1234567890, lang='ff'),
            "go'o biliyon e teemedere ɗiɗi e cappanɗe tati e nay miliyon e "
            "teemedere joyi e cappanɗe jeego e jowiɗi dubu e "
            "teemedere jowiɗi e go'o e cappanɗe jowiɗi e ɗiɗi"
        )

    def test_year(self):
        self.assertEqual(
            num2words(1398, lang='ff', to='year'),
            "dubu e teemedere tati e cappanɗe jowiɗi e ɗiɗi e jowiɗi e go'o"
        )
        self.assertEqual(
            num2words(1399, lang='ff', to='year'),
            "dubu e teemedere tati e cappanɗe jowiɗi e ɗiɗi e jowiɗi e ɗiɗi"
        )
        self.assertEqual(
            num2words(1400, lang='ff', to='year'),
            "dubu e teemedere nay"
        )

    def test_currency(self):
        self.assertEqual(
            num2words(1000, lang='ff', to='currency'),
            'dubu CFA'
        )
        self.assertEqual(
            num2words(1500000, lang='ff', to='currency'),
            "go'o miliyon e teemedere joyi dubu CFA"
        )