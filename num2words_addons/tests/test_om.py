# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.
# Copyright (c) 2020, Hamidreza Kalbasi.  All Rights Reserved.

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



from unittest import TestCase

from num2words import num2words


class Num2WordsOMTest(TestCase):

    def test_and_join_199(self):
        self.assertEqual(num2words(199, lang='om'),
                         "dhibba fi sagalatama fi sagal")

    def test_ordinal(self):
        self.assertEqual(
            num2words(0, lang='om', to='ordinal'),
            'zeeroffaa'
        )
        self.assertEqual(
            num2words(1, lang='om', to='ordinal'),
            'tokkoffaa'
        )
        self.assertEqual(
            num2words(13, lang='om', to='ordinal'),
            'kudhan sadiiffaa'
        )
        self.assertEqual(
            num2words(23, lang='om', to='ordinal'),
            'digdamii fi sadiiffaa'
        )
        self.assertEqual(
            num2words(12, lang='om', to='ordinal'),
            'kudhan lamaffaa'
        )
        self.assertEqual(
            num2words(113, lang='om', to='ordinal'),
            'dhibba fi kudhan sadiiffaa'
        )
        self.assertEqual(
            num2words(103, lang='om', to='ordinal'),
            'dhibba fi sadiiffaa'
        )

    def test_cardinal(self):
        self.assertEqual(num2words(130000, lang='om'),
                         "dhibba fi soddoma kuma")
        self.assertEqual(num2words(242, lang='om'),
                         "lama dhibba fi afurtama fi lama")
        self.assertEqual(num2words(800, lang='om'),
                         "saddeet dhibba")
        self.assertEqual(num2words(-203, lang='om'),
                         "minus lama dhibba fi sadii")
        self.assertEqual(
            num2words(1234567890, lang='om'),
            "tokko biliyoona fi lama dhibba fi soddoma fi afur miliyoona "
            "fi shan dhibba fi jahaatama fi torba kuma "
            "fi saddeet dhibba fi sagalatama"
        )

    def test_year(self):
        self.assertEqual(num2words(1398, lang='om', to='year'),
                         "kuma fi sadii dhibba fi sagalatama fi saddeet")
        self.assertEqual(num2words(1399, lang='om', to='year'),
                         "kuma fi sadii dhibba fi sagalatama fi sagal")
        self.assertEqual(
            num2words(1400, lang='om', to='year'),
            "kuma fi afur dhibba"
        )

    def test_ordinal_num(self):
        self.assertEqual(num2words(10, lang='om', to='ordinal_num'), '10')
        self.assertEqual(num2words(21, lang='om', to='ordinal_num'), '21')
        self.assertEqual(num2words(102, lang='om', to='ordinal_num'), '102')
        self.assertEqual(num2words(73, lang='om', to='ordinal_num'), '73')

    def test_currency(self):
        self.assertEqual(
            num2words(1000, lang='om', to='currency'),
            'kuma qarshii'
        )
        self.assertEqual(
            num2words(1500000, lang='om', to='currency'),
            'tokko miliyoona fi shan dhibba kuma qarshii'
        )
        
#    def test_cardinal_for_float_number(self):
#        self.assertEqual(num2words(12.5, lang='om'),
#                         "goma sha biyu da biyar")
#        self.assertEqual(num2words(0.75, lang='om'),
#                         "saba'in da biyar")
#        self.assertEqual(num2words(12.51, lang='om'),
#                         "goma sha biyu da hamsin da ɗaya")
#        self.assertEqual(num2words(12.53, lang='om'),
#                         "goma sha biyu da hamsin da uku")
#        self.assertEqual(num2words(12.59, lang='om'),
#                         "goma sha biyu da hamsin da tara")
#        self.assertEqual(num2words(0.000001, lang='om'),
#                         "ɗaya")

    def test_overflow(self):
        with self.assertRaises(OverflowError):
            num2words("1000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "00000000000000000000000000000000")
