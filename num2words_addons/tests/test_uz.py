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

class Num2WordsUZTest(TestCase):
    def test_to_cardinal(self):
        self.maxDiff = None
        self.assertEqual(num2words(7, lang='uz'), "yetti")
        self.assertEqual(num2words(23, lang='uz'), "yigirma uch")
        self.assertEqual(num2words(145, lang='uz'), "yuz qirq besh")
        self.assertEqual(
            num2words(2869, lang='uz'),
            "ikki ming sakkiz yuz oltmish to‘qqiz"
        )
        self.assertEqual(
            num2words(-789000125, lang='uz'),
            "minus yetti yuz sakson to‘qqiz million yuz yigirma besh",
        )
        self.assertEqual(
            num2words(84932, lang='uz'),
            "sakson to‘rt ming to‘qqiz yuz o‘ttiz ikki"
        )

    def test_to_cardinal_floats(self):
        self.assertEqual(num2words(100.67, lang='uz'), "yuz butun oltmish yetti")
        self.assertEqual(num2words(0.7, lang='uz'), "nol butun yetti")
        self.assertEqual(num2words(1.73, lang='uz'), "bir butun yetmish uch")
        self.assertEqual(
            num2words(10.02, lang='uz'),
            "o‘n butun nol ikki"
        )
        self.assertEqual(
            num2words(15.007, lang='uz'),
            "o‘n besh butun nol nol yetti"
        )

    def test_to_ordinal(self):
        with self.assertRaises(NotImplementedError):
            num2words(1, lang='uz', to="ordinal")

    def test_to_currency(self):
        self.assertEqual(
            num2words(25.24, lang='uz', to="currency", currency="UZS"),
            "yigirma besh so‘m, yigirma to‘rt tiyin",
        )
        self.assertEqual(
            num2words(1996.4, lang='uz', to="currency", currency="UZS"),
            "bir ming to‘qqiz yuz to‘qson olti so‘m, qirq tiyin",
        )
        self.assertEqual(
            num2words(632924.51, lang='uz', to="currency", currency="UZS"),
            "olti yuz o‘ttiz ikki ming to‘qqiz yuz yigirma to‘rt so‘m, ellik bir tiyin",
        )
        self.assertEqual(
            num2words(632924.513, lang='uz', to="currency", currency="UZS"),
            "olti yuz o‘ttiz ikki ming to‘qqiz yuz yigirma to‘rt so‘m, ellik bir tiyin",
        )
        self.assertEqual(
            num2words(987654321.123, lang='uz', to="currency", currency="UZS"),
            "to‘qqiz yuz sakson yetti million olti yuz ellik to‘rt ming "
            "uch yuz yigirma bir so‘m, o‘n ikki tiyin",
        )