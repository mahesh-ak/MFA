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


from unittest import TestCase
from num2words import num2words


class Num2WordsKMTest(TestCase):

    def test_0(self):
        self.assertEqual(num2words(0, lang='km'), "សូន្យ")

    def test_1_to_10(self):
        self.assertEqual(num2words(1, lang='km'), "មួយ")
        self.assertEqual(num2words(2, lang='km'), "ពីរ")
        self.assertEqual(num2words(7, lang='km'), "ប្រាំពីរ")
        self.assertEqual(num2words(10, lang='km'), "ដប់")

    def test_11_to_19(self):
        self.assertEqual(num2words(11, lang='km'), "ដប់ មួយ")
        self.assertEqual(num2words(13, lang='km'), "ដប់ បី")
        self.assertEqual(num2words(14, lang='km'), "ដប់ បួន")
        self.assertEqual(num2words(15, lang='km'), "ដប់ ប្រាំ")
        self.assertEqual(num2words(16, lang='km'), "ដប់ ប្រាំមួយ")
        self.assertEqual(num2words(19, lang='km'), "ដប់ ប្រាំបួន")

    def test_20_to_99(self):
        self.assertEqual(num2words(20, lang='km'), "ម្ភៃ")
        self.assertEqual(num2words(23, lang='km'), "ម្ភៃ បី")
        self.assertEqual(num2words(28, lang='km'), "ម្ភៃ ប្រាំបី")
        self.assertEqual(num2words(31, lang='km'), "សាមសិប មួយ")
        self.assertEqual(num2words(40, lang='km'), "សែសិប")
        self.assertEqual(num2words(66, lang='km'), "ហុកសិប ប្រាំមួយ")
        self.assertEqual(num2words(92, lang='km'), "កៅសិប ពីរ")

    def test_100_to_999(self):
        self.assertEqual(num2words(100, lang='km'), "មួយ រយ")
        self.assertEqual(num2words(150, lang='km'), "មួយ រយ ហាសិប")
        self.assertEqual(
            num2words(196, lang='km'), "មួយ រយ កៅសិប ប្រាំមួយ"
        )
        self.assertEqual(num2words(200, lang='km'), "ពីរ រយ")
        self.assertEqual(num2words(210, lang='km'), "ពីរ រយ ដប់")

    def test_1000_to_9999(self):
        self.assertEqual(num2words(1000, lang='km'), "មួយ ពាន់")
        self.assertEqual(num2words(1500, lang='km'), "មួយ ពាន់ ប្រាំ រយ")
        self.assertEqual(
            num2words(7378, lang='km'),
            "ប្រាំពីរ ពាន់ បី រយ ចិតសិប ប្រាំបី"
        )
        self.assertEqual(num2words(2000, lang='km'), "ពីរ ពាន់")
        self.assertEqual(num2words(2100, lang='km'), "ពីរ ពាន់ មួយ រយ")
        self.assertEqual(
            num2words(6870, lang='km'),
            "ប្រាំមួយ ពាន់ ប្រាំបី រយ ចិតសិប"
        )
        self.assertEqual(num2words(10000, lang='km'), "ដប់ ពាន់")
        self.assertEqual(num2words(100000, lang='km'), "មួយ រយ ពាន់")
        self.assertEqual(
            num2words(523456, lang='km'),
            "ប្រាំ រយ ម្ភៃ បី ពាន់ បួន រយ ហាសិប ប្រាំមួយ"
        )

    def test_big(self):
        self.assertEqual(num2words(1000000, lang='km'), "មួយ លាន")
        self.assertEqual(
            num2words(1200000, lang='km'), "មួយ លាន ពីរ រយ ពាន់"
        )
        self.assertEqual(num2words(3000000, lang='km'), "បី លាន")
        self.assertEqual(
            num2words(3800000, lang='km'), "បី លាន ប្រាំបី រយ ពាន់"
        )
        self.assertEqual(num2words(1000000000, lang='km'), "មួយ ប៊ីលាន")
        self.assertEqual(num2words(2000000000, lang='km'), "ពីរ ប៊ីលាន")
        self.assertEqual(
            num2words(2000001000, lang='km'), "ពីរ ប៊ីលាន មួយ ពាន់"
        )
        self.assertEqual(
            num2words(1234567890, lang='km'),
            "មួយ ប៊ីលាន ពីរ រយ សាមសិប បួន លាន ប្រាំ រយ ហុកសិប ប្រាំពីរ ពាន់ "
            "ប្រាំបី រយ កៅសិប"
        )

    def test_decimal_number(self):
        self.assertEqual(
            num2words(1000.11, lang='km'), "មួយ ពាន់ ចំណុច មួយ មួយ"
        )
        self.assertEqual(
            num2words(1000.21, lang='km'), "មួយ ពាន់ ចំណុច ពីរ មួយ"
        )

    def test_special_number(self):
        self.assertEqual(num2words(21, lang='km'), "ម្ភៃ មួយ")
        self.assertEqual(num2words(25, lang='km'), "ម្ភៃ ប្រាំ")

        # >100
        self.assertEqual(num2words(101, lang='km'), "មួយ រយ មួយ")
        self.assertEqual(num2words(105, lang='km'), "មួយ រយ ប្រាំ")
        self.assertEqual(num2words(701, lang='km'), "ប្រាំពីរ រយ មួយ")
        self.assertEqual(num2words(705, lang='km'), "ប្រាំពីរ រយ ប្រាំ")

        # >1000
        self.assertEqual(num2words(1001, lang='km'), "មួយ ពាន់ មួយ")
        self.assertEqual(num2words(1005, lang='km'), "មួយ ពាន់ ប្រាំ")
        self.assertEqual(
            num2words(98765, lang='km'),
            "កៅសិប ប្រាំបី ពាន់ ប្រាំពីរ រយ ហុកសិប ប្រាំ"
        )

        # > 1000000
        self.assertEqual(num2words(3000005, lang='km'), "បី លាន ប្រាំ")
        self.assertEqual(num2words(1000007, lang='km'), "មួយ លាន ប្រាំពីរ")

        # > 1000000000
        self.assertEqual(
            num2words(1000000017, lang='km'), "មួយ ប៊ីលាន ដប់ ប្រាំពីរ"
        )
        self.assertEqual(
            num2words(1000101017, lang='km'),
            "មួយ ប៊ីលាន មួយ រយ មួយ ពាន់ ដប់ ប្រាំពីរ"
        )