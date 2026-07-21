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

class Num2WordsGATest(TestCase):

    def test_cardinal_basic(self):
        self.assertEqual(num2words(0, lang='ga'), "náid")
        self.assertEqual(num2words(1, lang='ga'), "aon")
        self.assertEqual(num2words(2, lang='ga'), "dó")
        self.assertEqual(num2words(5, lang='ga'), "cúig")
        self.assertEqual(num2words(10, lang='ga'), "deich")

    def test_cardinal_teens(self):
        self.assertEqual(num2words(11, lang='ga'), "aon déag")
        self.assertEqual(num2words(15, lang='ga'), "cúig déag")
        self.assertEqual(num2words(19, lang='ga'), "naoi déag")

    def test_cardinal_tens(self):
        self.assertEqual(num2words(20, lang='ga'), "fiche")
        self.assertEqual(num2words(21, lang='ga'), "fiche a haon")
        self.assertEqual(num2words(22, lang='ga'), "fiche a dó")
        self.assertEqual(num2words(35, lang='ga'), "tríocha a cúig")

    def test_cardinal_hundreds(self):
        self.assertEqual(num2words(100, lang='ga'), "céad")
        self.assertEqual(num2words(101, lang='ga'), "céad aon")  # no "a" yet
        self.assertEqual(num2words(115, lang='ga'), "céad cúig déag")
        self.assertEqual(num2words(123, lang='ga'), "céad fiche a trí")

    def test_cardinal_thousands(self):
        self.assertEqual(num2words(1000, lang='ga'), "míle")
        self.assertEqual(num2words(1001, lang='ga'), "míle aon")  # no "a" yet
        self.assertEqual(num2words(2000, lang='ga'), "dó míle")   # no mutation yet
        self.assertEqual(num2words(2012, lang='ga'), "dó míle dhá déag")

    def test_cardinal_large(self):
        self.assertEqual(num2words(1000000, lang='ga'), "milliún")
        self.assertEqual(num2words(2000000, lang='ga'), "dó milliún")  # no mutation yet
        self.assertEqual(
            num2words(1234567, lang='ga'),
            "milliún dó céad tríocha a ceathair míle cúig céad seasca a seacht"
        )

    def test_negative(self):
        self.assertEqual(num2words(-1, lang='ga'), "lúide aon")
        self.assertEqual(num2words(-15, lang='ga'), "lúide cúig déag")

#    def test_cardinal_float(self):
#        self.assertEqual(num2words(0.12, lang='ga'), "náid ponc a haon a dó")
#        self.assertEqual(num2words(-0.12, lang='ga'), "lúide náid ponc a haon a dó")
#        self.assertEqual(num2words(12.5, lang='ga'), "dhá déag ponc a cúig")  # keep if your code mutates here
#        self.assertEqual(num2words(12.51, lang='ga'), "dhá déag ponc a cúig a haon")

#    def test_ordinal_basic(self):
#        self.assertEqual(num2words(1, lang='ga', to='ordinal'), "céad")
#        self.assertEqual(num2words(2, lang='ga', to='ordinal'), "dara")
#        self.assertEqual(num2words(3, lang='ga', to='ordinal'), "tríú")
#        self.assertEqual(num2words(10, lang='ga', to='ordinal'), "deichiú")

#    def test_ordinal_composed(self):
#        self.assertEqual(num2words(13, lang='ga', to='ordinal'), "trí déagú")
#        self.assertEqual(num2words(22, lang='ga', to='ordinal'), "fiche a dóú")

#    def test_ordinal_num(self):
#        self.assertEqual(num2words(1, lang='ga', to='ordinal_num'), "1ú")
#        self.assertEqual(num2words(2, lang='ga', to='ordinal_num'), "2ú")
#        self.assertEqual(num2words(10, lang='ga', to='ordinal_num'), "10ú")
#        self.assertEqual(num2words(21, lang='ga', to='ordinal_num'), "21ú")