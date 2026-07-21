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




class Num2WordsBGTest(TestCase):

    def test_cardinal(self):
        self.assertEqual("сто", num2words(100, lang='bg'))
        self.assertEqual("сто и един", num2words(101, lang='bg'))
        self.assertEqual("сто десет", num2words(110, lang='bg'))
        self.assertEqual("сто петнадесет", num2words(115, lang='bg'))
        self.assertEqual(
            "сто двадесет и три", num2words(123, lang='bg')
        )

        # thousand (feminine → една / две)
        self.assertEqual(
            "една хиляда", num2words(1000, lang='bg')
        )
        self.assertEqual(
            "една хиляда един", num2words(1001, lang='bg')
        )
        self.assertEqual(
            "две хиляди дванадесет", num2words(2012, lang='bg')
        )

#       self.assertEqual(
#           "дванадесет хиляди петстотин и деветнадесет запетая осем пет",
#           num2words(12519.85, lang='bg')
#       )

        self.assertEqual(
            "един милиард двеста тридесет и четири милиона петстотин "
            "шестдесет и седем хиляди осемстотин деветдесет",
            num2words(1234567890, lang='bg')
        )

        self.assertEqual("пет", num2words(5, lang='bg'))
        self.assertEqual("петнадесет", num2words(15, lang='bg'))
        self.assertEqual("сто петдесет и четири", num2words(154, lang='bg'))

        self.assertEqual(
            "една хиляда сто тридесет и пет",
            num2words(1135, lang='bg')
        )

        self.assertEqual(
            "четиристотин осемнадесет хиляди петстотин тридесет и един",
            num2words(418531, lang='bg'),
        )

        self.assertEqual(
            "един милион сто тридесет и девет",
            num2words(1000139, lang='bg')
        )

#   def test_floating_point(self):
#       self.assertEqual("пет запетая два", num2words(5.2, lang='bg'))
#       self.assertEqual(
#           num2words(10.02, lang='bg'),
#           "десет запетая нула два"
#       )
#       self.assertEqual(
#           num2words(15.007, lang='bg'),
#           "петнадесет запетая нула нула седем"
#       )
#       self.assertEqual(
#           "петстотин шестдесет и един запетая четири два",
#           num2words(561.42, lang='bg')
#       )

    def test_to_ordinal(self):
        # Not implemented yet
        with self.assertRaises(NotImplementedError):
            num2words(1, lang='bg', to='ordinal')
    def test_to_ordinal(self):
        # @TODO: implement to_ordinal
        with self.assertRaises(NotImplementedError):
            num2words(1, lang='bg', to='ordinal')