# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.

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

from __future__ import unicode_literals

from unittest import TestCase

from num2words import num2words
from num2words.lang_MY import Num2Word_MY

from unittest import TestCase
from num2words import num2words


class TestNumWord(TestCase):

    def test_0(self):
        self.assertEqual(num2words(0, lang='my'), "သုည")

    def test_end_with_1(self):
        self.assertEqual(num2words(21, lang='my'), "နှစ်ဆယ်တစ်")
        self.assertEqual(num2words(11, lang='my'), "ဆယ်တစ်")
        self.assertEqual(num2words(101, lang='my'), "တစ်ရာတစ်")
        self.assertEqual(num2words(1201, lang='my'), "တစ်ထောင်နှစ်ရာတစ်")

    def test_start_20(self):
        self.assertEqual(num2words(22, lang='my'), "နှစ်ဆယ်နှစ်")
        self.assertEqual(num2words(27, lang='my'), "နှစ်ဆယ်ခုနစ်")

    def test_start_10(self):
        self.assertEqual(num2words(10, lang='my'), "ဆယ်")
        self.assertEqual(num2words(18, lang='my'), "ဆယ်ရှစ်")

    def test_1_to_9(self):
        self.assertEqual(num2words(1, lang='my'), "တစ်")
        self.assertEqual(num2words(5, lang='my'), "ငါး")
        self.assertEqual(num2words(9, lang='my'), "ကိုး")

    def test_31_to_99(self):
        self.assertEqual(num2words(31, lang='my'), "သုံးဆယ်တစ်")
        self.assertEqual(num2words(48, lang='my'), "လေးဆယ်ရှစ်")
        self.assertEqual(num2words(76, lang='my'), "ခုနစ်ဆယ်ခြောက်")

    def test_100_to_999(self):
        self.assertEqual(num2words(100, lang='my'), "တစ်ရာ")
        self.assertEqual(num2words(123, lang='my'), "တစ်ရာနှစ်ဆယ်သုံး")
        self.assertEqual(num2words(456, lang='my'), "လေးရာငါးဆယ်ခြောက်")
        self.assertEqual(num2words(721, lang='my'), "ခုနစ်ရာနှစ်ဆယ်တစ်")

    def test_1000_to_9999(self):
        self.assertEqual(num2words(1000, lang='my'), "တစ်ထောင်")
        self.assertEqual(
            num2words(2175, lang='my'),
            "နှစ်ထောင်တစ်ရာခုနစ်ဆယ်ငါး"
        )
        self.assertEqual(num2words(4582, lang='my'), "လေးထောင်ငါးရာရှစ်ဆယ်နှစ်")
        self.assertEqual(num2words(9346, lang='my'), "ကိုးထောင်သုံးရာလေးဆယ်ခြောက်")

    def test_10000_to_99999(self):
        self.assertEqual(
            num2words(11111, lang='my'),
            "တစ်သောင်းတစ်ထောင်တစ်ရာဆယ်တစ်"
        )
        self.assertEqual(
            num2words(22222, lang='my'),
            "နှစ်သောင်းနှစ်ထောင်နှစ်ရာနှစ်ဆယ်နှစ်"
        )
        self.assertEqual(
            num2words(84573, lang='my'),
            "ရှစ်သောင်းလေးထောင်ငါးရာခုနစ်ဆယ်သုံး"
        )

    def test_100000_to_999999(self):
        self.assertEqual(
            num2words(153247, lang='my'),
            "တစ်သိန်းငါးသောင်းသုံးထောင်နှစ်ရာလေးဆယ်ခုနစ်"
        )
        self.assertEqual(
            num2words(562442, lang='my'),
            "ငါးသိန်းခြောက်သောင်းနှစ်ထောင်လေးရာလေးဆယ်နှစ်"
        )
        self.assertEqual(
            num2words(999999, lang='my'),
            "ကိုးသိန်းကိုးသောင်းကိုးထောင်ကိုးရာကိုးဆယ်ကိုး"
        )

    def test_more_than_million(self):
        self.assertEqual(num2words(1000000, lang='my'), "တစ်သန်း")
        self.assertEqual(num2words(1000001, lang='my'), "တစ်သန်းတစ်")
        self.assertEqual(
            num2words(42478941, lang='my'),
            "လေးဆယ်နှစ်သန်းလေးသိန်းခုနစ်သောင်းရှစ်ထောင်ကိုးရာလေးဆယ်တစ်"
        )
        self.assertEqual(
            num2words(712696969, lang='my'),
            "ခုနစ်ရာဆယ်နှစ်သန်းခြောက်သိန်းကိုးသောင်းခြောက်ထောင်ကိုးရာခြောက်ဆယ်ကိုး"
        )
        self.assertEqual(
            num2words(1000000000000000001, lang='my'),
            "တစ်သန်းသန်းသန်းတစ်"
        )

    def test_decimal(self):
        self.assertEqual(num2words(0.0, lang='my'), "သုည")
        self.assertEqual(num2words(0.0038, lang='my'), "သုညဒသမသုညသုညသုံးရှစ်")
        self.assertEqual(num2words(0.01, lang='my'), "သုညဒသမသုညတစ်")
        self.assertEqual(num2words(1.123, lang='my'), "တစ်ဒသမတစ်နှစ်သုံး")
        self.assertEqual(num2words(35.37, lang='my'), "သုံးဆယ်ငါးဒသမသုံးခုနစ်")
        self.assertEqual(num2words(1000000.01, lang='my'), "တစ်သန်းဒသမသုညတစ်")

    def test_negative(self):
        self.assertEqual(num2words(-10, lang='my'), "အနုတ်ဆယ်")
        self.assertEqual(num2words(-10.50, lang='my'), "အနုတ်ဆယ်ဒသမငါး")