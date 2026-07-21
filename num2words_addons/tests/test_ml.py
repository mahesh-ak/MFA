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


class Num2WordsMLTest(TestCase):
    def test_numbers(self):
        self.assertEqual(num2words(66, lang="ml"), u"അറുപത്തി ആറ്")
        self.assertEqual(num2words(1734, lang="ml"),
            u"ആയിരത്തി എഴുനൂറ്റി മുപ്പത്തി നാല്")
        self.assertEqual(num2words(134, lang="ml"),
            u"നൂറ്റി മുപ്പത്തി നാല്")
        self.assertEqual(num2words(54411, lang="ml"),
            u"അമ്പത്തി നാല് ആയിരത്തി നാനൂറ്റി പതിനൊന്ന്")
        self.assertEqual(num2words(42, lang="ml"), u"നാല്പത്തി രണ്ട്")
        self.assertEqual(num2words(893, lang="ml"),
            u"എണ്ണൂറ് തൊണ്ണൂറത്തി മൂന്ന്")
        self.assertEqual(num2words(1729, lang="ml"),
            u"ആയിരത്തി എഴുനൂറ്റി ഇരുപത്തി ഒമ്പത്")
        self.assertEqual(num2words(123, lang="ml"),
            u"നൂറ്റി ഇരുപത്തി മൂന്ന്")
        self.assertEqual(num2words(32211, lang="ml"),
            u"മുപ്പത്തി രണ്ട് ആയിരത്തി ഇരുനൂറ്റി പതിനൊന്ന്") 

    def test_cardinal_for_float_number(self):
        self.assertEqual(num2words(1.61803, lang="ml"),
                         u"ഒന്ന് പുള്ളി ആറ് ഒന്ന് എട്ട് പൂജ്യം മൂന്ന്")
        self.assertEqual(num2words(34.876, lang="ml"),
                         u"മുപ്പത്തി നാല് പുള്ളി എട്ട് ഏഴ് ആറ്")
        self.assertEqual(num2words(3.14, lang="ml"),
                         u"മൂന്ന് പുള്ളി ഒന്ന് നാല്")

    def test_ordinal(self):
        self.assertEqual(num2words(1, lang='ml', to='ordinal'), u"ഒന്നാം")
        self.assertEqual(num2words(22, lang='ml', to='ordinal'),
                         u"ഇരുപത്തി രണ്ടാം")
        self.assertEqual(num2words(23, lang='ml', to='ordinal'),
                         u"ഇരുപത്തി മൂന്നാം")
        self.assertEqual(num2words(12, lang='ml', to='ordinal'), u"പന്ത്രണ്ടാം")
        self.assertEqual(num2words(130, lang='ml', to='ordinal'),
                         u"നൂറ്റി മുപ്പതാം")
        self.assertEqual(num2words(1003, lang='ml', to='ordinal'),
                         u"ആയിരത്തി മൂന്നാം")
        self.assertEqual(num2words(4, lang='ml', to='ordinal'),
                         u"നാലാം")

    def test_ordinal_num(self):
        self.assertEqual(num2words(2, lang="ml", to='ordinal_num'), u"2ാം")
        self.assertEqual(num2words(3, lang="ml", to='ordinal_num'), u"3ാം")
        self.assertEqual(num2words(5, lang="ml", to='ordinal_num'), u"5ാം")
        self.assertEqual(num2words(16, lang="ml", to='ordinal_num'), u"16ാം")
        self.assertEqual(num2words(113, lang="ml", to='ordinal_num'),
                         u"113ാം")