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

class Num2WordsMTTest(TestCase):

    def test_ordinal(self):

        self.assertEqual(num2words(1, to='ordinal', lang='mt'), 'ewwel')
        self.assertEqual(num2words(2, to='ordinal', lang='mt'), 'it-tieni')
        self.assertEqual(num2words(3, to='ordinal', lang='mt'), 'it-tielet')
        self.assertEqual(num2words(4, to='ordinal', lang='mt'), 'ir-raba’')
        self.assertEqual(num2words(5, to='ordinal', lang='mt'), 'il-ħames')
        self.assertEqual(num2words(6, to='ordinal', lang='mt'), 'is-sitt')
        self.assertEqual(num2words(9, to='ordinal', lang='mt'), 'id-disa’')
        self.assertEqual(num2words(20, to='ordinal', lang='mt'), 'l-għoxrin')

        self.assertEqual(
            num2words(94, to='ordinal', lang='mt'),
            'erbgħa u disgħin'
        )
        self.assertEqual(
            num2words(102, to='ordinal', lang='mt'),
            'mija u tnejn'
        )

#        self.assertEqual(
#            num2words(923411, to='ordinal_num', lang='mt'),
#            'disa’ mitt u tlieta u għoxrin elf u erba’ mitt u ħdax'
#        )

    def test_cardinal(self):
        self.assertEqual(num2words(0, to='cardinal', lang='mt'), 'żero')
        self.assertEqual(num2words(12, to='cardinal', lang='mt'), 'tnax')
        
#        self.assertEqual(
#            num2words(12.3, to='cardinal', lang='mt'),
#            'tnax virgola tlieta'
#        )
#        self.assertEqual(
#            num2words(12.01, to='cardinal', lang='mt'),
#            'tnax virgola żero wieħed'
#        )
#        self.assertEqual(
#            num2words(12.02, to='cardinal', lang='mt'),
#            'tnax virgola żero tnejn'
#        )
#        self.assertEqual(
#            num2words(12.03, to='cardinal', lang='mt'),
#            'tnax virgola żero tlieta'
#        )
#        self.assertEqual(
#            num2words(12.34, to='cardinal', lang='mt'),
#            'tnax virgola erbgħa u tletin'
#        )


#        self.assertEqual(
#            num2words(-8324, to='cardinal', lang='mt'),
#            'minus tmint elef u tliet mitt u erbgħa u għoxrin'
#        )

        self.assertEqual(num2words(200, to='cardinal', lang='mt'), 'mitejn')
        self.assertEqual(num2words(700, to='cardinal', lang='mt'), 'seba’ mitt')

#        self.assertEqual(
#            num2words(101010, to='cardinal', lang='mt'),
#            'mija u elf u għaxra'
#        )

#        self.assertEqual(
#            num2words(3431.12, to='cardinal', lang='mt'),
#            'tlett elef u erba’ mitt u wieħed u tletin virgola tnax'
#        )

        self.assertEqual(
            num2words(431, to='cardinal', lang='mt'),
            'erba’ mitt u wieħed u tletin'
        )

        self.assertEqual(
            num2words(94231, to='cardinal', lang='mt'),
            'erbgħa u disgħin elf u mitejn u wieħed u tletin'
        )

        self.assertEqual(
            num2words(1431, to='cardinal', lang='mt'),
            'elf u erba’ mitt u wieħed u tletin'
        )

        self.assertEqual(num2words(740, to='cardinal', lang='mt'),
                         'seba’ mitt u erbgħin')

        self.assertEqual(num2words(741, to='cardinal', lang='mt'),
                         'seba’ mitt u wieħed u erbgħin')

        self.assertEqual(num2words(262, to='cardinal', lang='mt'),
                         'mitejn u tnejn u sittin')

        self.assertEqual(num2words(798, to='cardinal', lang='mt'),
                         'seba’ mitt u tmienja u disgħin')

        self.assertEqual(num2words(710, to='cardinal', lang='mt'),
                         'seba’ mitt u għaxra')

        self.assertEqual(num2words(711, to='cardinal', lang='mt'),
                         'seba’ mitt u ħdax')

        self.assertEqual(num2words(700, to='cardinal', lang='mt'),
                         'seba’ mitt')

        self.assertEqual(num2words(701, to='cardinal', lang='mt'),
                         'seba’ mitt u wieħed')

        self.assertEqual(
            num2words(1258888, to='cardinal', lang='mt'),
            'miljun u mitejn u tmienja u ħamsin elf u tmien mitt u tmienja u tmenin'
        )

        self.assertEqual(num2words(1100, to='cardinal', lang='mt'),
                         'elf u mija')

        self.assertEqual(
            num2words(1000000521, to='cardinal', lang='mt'),
            'biljun u ħames mitt u wieħed u għoxrin'
        )

    def test_prefix_and_suffix(self):
        self.assertEqual(
            num2words(645, to='currency', lang='mt',
                      prefix="biss", suffix="biss"),
            'biss sitt mitt u ħamsa u erbgħin ewro biss'
        )

    def test_year(self):
        self.assertEqual(num2words(2000, to='year', lang='mt'), 'elfejn')