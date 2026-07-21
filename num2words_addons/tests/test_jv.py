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

from unittest import TestCase

from num2words import num2words

class Num2WordsJVTest(TestCase):

    def test_cardinal_for_natural_number(self):
        self.assertEqual(num2words(10, lang='jv'), "sepuluh")
        self.assertEqual(num2words(11, lang='jv'), "sewelas")
        self.assertEqual(num2words(108, lang='jv'), "satus wolu")
        self.assertEqual(num2words(1075, lang='jv'), "sewu pitu puluh lima")
        self.assertEqual(
            num2words(1087231, lang='jv'),
            "siji yuta wolung puluh pitu ewu loro atus telu puluh siji"
        )
        self.assertEqual(
            num2words(1000000408, lang='jv'),
            "siji milyar papat atus wolu"
        )

    def test_cardinal_for_decimal_number(self):
        self.assertEqual(
            num2words(12.234, lang='jv'),
            "loro welas koma loro telu papat"
        )
        self.assertEqual(
            num2words(9.076, lang='jv'),
            "sanga koma nol pitu enem"
        )

    def test_cardinal_for_negative_number(self):
        self.assertEqual(
            num2words(-923, lang='jv'),
            "minus sanga atus loro puluh telu"
        )
        self.assertEqual(
            num2words(-0.234, lang='jv'),
            "minus nol koma loro telu papat"
        )

    def test_ordinal_for_natural_number(self):
        self.assertEqual(num2words(1, ordinal=True, lang='jv'), "pisanan")
        self.assertEqual(num2words(10, ordinal=True, lang='jv'), "ke-sepuluh")

    def test_ordinal_for_negative_number(self):
        self.assertRaises(TypeError, num2words, -12, ordinal=True, lang='jv')

    def test_ordinal_for_floating_number(self):
        self.assertRaises(TypeError, num2words, 3.243, ordinal=True, lang='jv')