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


class Num2WordsTATest(TestCase):
    def test_numbers(self):
        self.assertEqual(num2words(66, lang="ta"), u"அறுபத்து ஆறு")
        self.assertEqual(num2words(1734, lang="ta"),
            u"ஆயிரத்து எழுநூற்று முப்பத்து நான்கு")
        self.assertEqual(num2words(134, lang="ta"),
            u"நூற்று முப்பத்து நான்கு")
        self.assertEqual(num2words(54411, lang="ta"),
            u"ஐம்பத்து நான்கு ஆயிரத்து நானூற்று பதினொன்று")
        self.assertEqual(num2words(42, lang="ta"), u"நாற்பத்து இரண்டு")
        self.assertEqual(num2words(893, lang="ta"),
            u"எண்ணூற்று தொண்ணூற்று மூன்று")
        self.assertEqual(num2words(1729, lang="ta"),
            u"ஆயிரத்து எழுநூற்று இருபத்து ஒன்பது")
        self.assertEqual(num2words(123, lang="ta"),
            u"நூற்று இருபத்து மூன்று")
        self.assertEqual(num2words(32211, lang="ta"),
            u"முப்பத்து இரண்டு ஆயிரத்து இருநூற்று பதினொன்று") 

    def test_cardinal_for_float_number(self):
        self.assertEqual(num2words(1.61803, lang="ta"),
                         u"ஒன்று புள்ளி ஆறு ஒன்று எட்டு பூஜ்ஜியம் மூன்று")
        self.assertEqual(num2words(34.876, lang="ta"),
                         u"முப்பத்து நான்கு புள்ளி எட்டு ஏழு ஆறு")
        self.assertEqual(num2words(3.14, lang="ta"),
                         u"மூன்று புள்ளி ஒன்று நான்கு")

    def test_ordinal(self):
        self.assertEqual(num2words(1, lang='ta', to='ordinal'), u"முதலாவது")
        self.assertEqual(num2words(22, lang='ta', to='ordinal'),
                         u"இருபத்து இரண்டாவது")
        self.assertEqual(num2words(23, lang='ta', to='ordinal'),
                         u"இருபத்து மூன்றாவது")
        self.assertEqual(num2words(12, lang='ta', to='ordinal'), u"பன்னிரண்டாவது")
        self.assertEqual(num2words(130, lang='ta', to='ordinal'),
                         u"நூற்று முப்பதாவது")
        self.assertEqual(num2words(1003, lang='ta', to='ordinal'),
                         u"ஆயிரத்து மூன்றாவது")
        self.assertEqual(num2words(4, lang='ta', to='ordinal'),
                         u"நான்காவது")

    def test_ordinal_num(self):
        self.assertEqual(num2words(2, lang="ta", to='ordinal_num'), u"2வது")
        self.assertEqual(num2words(3, lang="ta", to='ordinal_num'), u"3வது")
        self.assertEqual(num2words(5, lang="ta", to='ordinal_num'), u"5வது")
        self.assertEqual(num2words(16, lang="ta", to='ordinal_num'), u"16வது")
        self.assertEqual(num2words(113, lang="ta", to='ordinal_num'),
                         u"113வது")
