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

from __future__ import division, print_function, unicode_literals

from unittest import TestCase

from num2words import num2words


class Num2WordsETTest(TestCase):


    def test_cardinal(self):
        self.assertEqual(
            num2words(-1, lang='et'),
            'miinus üks'
        )
        self.assertEqual(
            num2words(0, lang='et'),
            'null'
        )
        self.assertEqual(
            num2words(1, lang='et'),
            'üks'
        )
        self.assertEqual(
            num2words(13, lang='et'),
            'kolmteist'
        )
        self.assertEqual(
            num2words(22, lang='et'),
            'kakskümmendkaks'
        )
        self.assertEqual(
            num2words(75, lang='et'),
            'seitsekümmendviis'
        )
        self.assertEqual(
            num2words(124, lang='et'),
            'sadakakskümmendneli'
        )
        self.assertEqual(
            num2words(651, lang='et'),
            'kuussadaviiskümmendüks'
        )
        self.assertEqual(
            num2words(2232, lang='et'),
            'kakstuhatkakssadakolmkümmendkaks'
        )
        self.assertEqual(
            num2words(16501, lang='et'),
            'kuueteisttuhatviissadaüks'
        )
        self.assertEqual(
            num2words(1900000000000, lang='et'),
            'ükstriljonüheksasadamiljard'
        )
#        self.assertEqual(
#            num2words(24656451324564987566, lang='et'),
#            'kakskümmendnelitriljonkuussadaviiskümmendkuusbilliard'
#            'neli­sadaviiskümmendükstriljonkolmsadakakskümmendnelimiljard'
#            'viissadakuuskümmendnelimiljonüheksasadakaheksakümmendseitsetuhat'
#            'viissadakuuskümmendkuus'
#        )
