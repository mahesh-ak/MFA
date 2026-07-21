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
from num2words.lang_AF import Num2Word_AF


class Num2WordsAFTest(TestCase):
    def test_ordinal_less_than_twenty(self):
        self.assertEqual(num2words(7, ordinal=True, lang='af'), "sevende")
        self.assertEqual(num2words(8, ordinal=True, lang='af'), "agtste")
        self.assertEqual(num2words(12, ordinal=True, lang='af'), "twaalfde")
        self.assertEqual(num2words(17, ordinal=True, lang='af'), "seventiende")

    def test_ordinal_more_than_twenty(self):
        self.assertEqual(
            num2words(81, ordinal=True, lang='af'), "een-en-tagtigste"
        )

    def test_ordinal_at_crucial_number(self):
        self.assertEqual(num2words(0, ordinal=True, lang='af'), "nulde")
        self.assertEqual(num2words(100, ordinal=True, lang='af'), "honderdste")
        self.assertEqual(
            num2words(1000, ordinal=True, lang='af'), "duisendste"
        )
        self.assertEqual(
            num2words(4000, ordinal=True, lang='af'), "vier duisendste"
        )
        self.assertEqual(
            num2words(2000000, ordinal=True, lang='af'), "twee miljoenste"
        )
        self.assertEqual(
            num2words(5000000000, ordinal=True, lang='af'), "vyf miljardste"
        )

    def test_cardinal_at_some_numbers(self):
        self.assertEqual(num2words(82, lang='af'), u'twee-en-tagtig')
        self.assertEqual(num2words(1013, lang='af'), "duisend dertien")
        self.assertEqual(num2words(2000000, lang='af'), "twee miljoen")
        self.assertEqual(num2words(4000000000, lang='af'), "vier miljard")

    def test_cardinal_for_decimal_number(self):
        self.assertEqual(
            num2words(3.486, lang='af'), "drie komma vier agt ses"
        )

    def test_ordinal_for_negative_numbers(self):
        self.assertRaises(TypeError, num2words, -12, ordinal=True, lang='af')

    def test_ordinal_for_floating_numbers(self):
        self.assertRaises(TypeError, num2words, 2.453, ordinal=True, lang='af')

    def test_to_currency_eur(self):
        self.assertEqual(
            num2words('38.4', lang='af', to='currency', separator=' en',
                      cents=False, currency='EUR'),
            "agt-en-dertig euro en 40 cent"
        )
        self.assertEqual(
            num2words('0', lang='af', to='currency', separator=' en',
                      cents=False, currency='EUR'),
            "nul euro"
        )

        self.assertEqual(
            num2words('1.01', lang='af', to='currency', separator=' en',
                      cents=True, currency='EUR'),
            "een euro en een cent"
        )

        self.assertEqual(
            num2words('4778.00', lang='af', to='currency', separator=' en',
                      cents=True, currency='EUR'),
            'vier duisend seven honderd agt-en-seventig euro en nul cent')

    def test_to_currency_usd(self):
        self.assertEqual(
            num2words('38.4', lang='af', to='currency', separator=' en',
                      cents=False, currency='USD'),
            "agt-en-dertig dollar en 40 cent"
        )
        self.assertEqual(
            num2words('0', lang='af', to='currency', separator=' en',
                      cents=False, currency='USD'),
            "nul dollar"
        )

        self.assertEqual(
            num2words('1.01', lang='af', to='currency', separator=' en',
                      cents=True, currency='USD'),
            "een dollar en een cent"
        )

        self.assertEqual(
            num2words('4778.00', lang='af', to='currency', separator=' en',
                      cents=True, currency='USD'),
            'vier duisend seven honderd agt-en-seventig dollar en nul cent')

    def test_pluralize(self):
        n = Num2Word_AF()
        # euros always singular
        cr1, cr2 = n.CURRENCY_FORMS['EUR']
        self.assertEqual(n.pluralize(1, cr1), 'euro')
        self.assertEqual(n.pluralize(2, cr1), 'euro')
        self.assertEqual(n.pluralize(1, cr2), 'cent')
        self.assertEqual(n.pluralize(2, cr2), 'cent')

        # @TODO other currency

    def test_to_year(self):
        self.assertEqual(num2words(2018, lang='af', to='year'),
                         'twee duisend agttien')
        self.assertEqual(num2words(2100, lang='af', to='year'),
                         'een-en-twintig honderd')