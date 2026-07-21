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


class Num2WordsMITest(TestCase):

    def test_cardinal_for_natural_number(self):
        self.assertEqual(num2words(10, lang='mi'), "tekau")
        self.assertEqual(num2words(11, lang='mi'), "tekau mā tahi")
        self.assertEqual(num2words(108, lang='mi'), "kotahi rau waru")
        self.assertEqual(num2words(1075, lang='mi'), "kotahi mano whitu tekau mā rima")
        self.assertEqual(
            num2words(1087231, lang='mi'),
            "kotahi miriona waru tekau mā whitu mano rua rau toru tekau mā tahi"
        )
        self.assertEqual(
            num2words(1000000408, lang='mi'),
            "kotahi piriona whā rau waru"
        )

    def test_cardinal_for_decimal_number(self):
        self.assertEqual(
            num2words(12.234, lang='mi'),
            "tekau mā rua ira rua toru whā"
        )
        self.assertEqual(
            num2words(9.076, lang='mi'),
            "iwa ira kore whitu ono"
        )

    def test_cardinal_for_negative_number(self):
        self.assertEqual(
            num2words(-923, lang='mi'),
            "tāpirihanga iwa rau rua tekau mā toru"
        )
        self.assertEqual(
            num2words(-0.234, lang='mi'),
            "tāpirihanga kore ira rua toru whā"
        )

    def test_ordinal_for_natural_number(self):
        self.assertEqual(num2words(1, ordinal=True, lang='mi'), "te tahi")
        self.assertEqual(num2words(10, ordinal=True, lang='mi'), "te tekau")

    def test_ordinal_for_negative_number(self):
        self.assertRaises(TypeError, num2words, -12, ordinal=True, lang='mi')

    def test_ordinal_for_floating_number(self):
        self.assertRaises(TypeError, num2words, 3.243, ordinal=True, lang='mi')