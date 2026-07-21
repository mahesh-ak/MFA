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

class Num2WordsKYTest(TestCase):
    def test_to_cardinal(self):
        self.maxDiff = None
        self.assertEqual(num2words(7, lang="ky"), "жети")
        self.assertEqual(num2words(23, lang="ky"), "жыйырма үч")
        self.assertEqual(num2words(145, lang="ky"), "жүз кырк беш")
        self.assertEqual(
            num2words(2869, lang="ky"),
            "эки миң сегиз жүз алтымыш тогуз"
        )
        self.assertEqual(
            num2words(-789000125, lang="ky"),
            "минус жети жүз сексен тогуз миллион жүз жыйырма беш",
        )
        self.assertEqual(
            num2words(84932, lang="ky"),
            "сексен төрт миң тогуз жүз отуз эки"
        )

    def test_to_cardinal_floats(self):
        self.assertEqual(num2words(100.67, lang="ky"), "жүз бүтүн алтымыш жети")
        self.assertEqual(num2words(0.7, lang="ky"), "нөл бүтүн жети")
        self.assertEqual(num2words(1.73, lang="ky"), "бир бүтүн жетимиш үч")
        self.assertEqual(
            num2words(10.02, lang='ky'),
            "он бүтүн нөл эки"
        )
        self.assertEqual(
            num2words(15.007, lang='ky'),
            "он беш бүтүн нөл нөл жети"
        )

    def test_to_ordinal(self):
        with self.assertRaises(NotImplementedError):
            num2words(1, lang="ky", to="ordinal")

    def test_to_currency(self):
        self.assertEqual(
            num2words(25.24, lang="ky", to="currency", currency="KGS"),
            "жыйырма беш сом, жыйырма төрт тыйын",
        )
        self.assertEqual(
            num2words(1996.4, lang="ky", to="currency", currency="KGS"),
            "бир миң тогуз жүз токсон алты сом, кырк тыйын",
        )
        self.assertEqual(
            num2words(632924.51, lang="ky", to="currency", currency="KGS"),
            "алты жүз отуз эки миң тогуз жүз жыйырма төрт сом, элүү бир тыйын",
        )
        self.assertEqual(
            num2words(632924.513, lang="ky", to="currency", currency="KGS"),
            "алты жүз отуз эки миң тогуз жүз жыйырма төрт сом, элүү бир тыйын",
        )
        self.assertEqual(
            num2words(987654321.123, lang="ky", to="currency", currency="KGS"),
            "тогуз жүз сексен жети миллион алты жүз элүү төрт миң "
            "үч жүз жыйырма бир сом, он эки тыйын",
        )