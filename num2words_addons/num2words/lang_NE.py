# -*- encoding: utf-8 -*-
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

import string

from num2words.base import Num2Word_Base


class Num2Word_NE(Num2Word_Base):
    """
    Nepali (NE) Num2Word class
    """

    _irregular_ordinals = {
        0: "शून्य",
        1: "पहिलो",
        2: "दोस्रो",
        3: "तेस्रो",
        4: "चौथो",
        6: "छैटौं",
    }

    _irregular_ordinals_nums = {
        0: "०",
        1: "१औं",
        2: "२औं",
        3: "३औं",
        4: "४औं",
        6: "६औं",
    }

    _nepali_digits = "०१२३४५६७८९"
    _digits_to_nepali_digits = dict(zip(string.digits, _nepali_digits))

    _regular_ordinal_suffix = "औं"

    def setup(self):
        self.low_numwords = ['उनान्नब्बे',
                'अन्ठान्नब्बे',
                'सन्तान्नब्बे',
                'छयान्नब्बे',
                'पन्चान्नब्बे',
                'चौरान्नब्बे',
                'त्रियान्नब्बे',
                'बयान्नब्बे',
                'एकान्नब्बे',
                'नब्बे',
                'नवासी',
                'अठासी',
                'सत्तासी',
                'छयासी',
                'पचासी',
                'चौरासी',
                'त्रियासी',
                'बयासी',
                'एकासी',
                'असी',
                'उनासी',
                'अठहत्तर',
                'सतहत्तर',
                'छयहत्तर',
                'पचहत्तर',
                'चौहत्तर',
                'त्रिहत्तर',
                'बहत्तर',
                'एकहत्तर',
                'सत्तरी',
                'उनहत्तर',
                'अठसाठी',
                'सतसाठी',
                'छयसाठी',
                'पैसाठी',
                'चौँसाठी',
                'त्रिसाठी',
                'बासाठी',
                'एकसाठी',
                'साठी',
                'उनन्साठी',
                'अन्ठाउन्न',
                'सन्ताउन्न',
                'छपन्न',
                'पचपन्न',
                'चौवन्न',
                'त्रेपन्न',
                'बाउन्न',
                'एकाउन्न',
                'पचास',
                'उनन्चास',
                'अठचालिस',
                'सन्तालिस',
                'छयालिस',
                'पैतालिस',
                'चौवालीस',
                'त्रेचालिस',
                'बयालिस',
                'एकचालिस',
                'चालिस',
                'उनन्चालिस',
                'अठतीस',
                'सैतीस',
                'छत्तीस',
                'पैतीस',
                'चौँतीस',
                'तेत्तीस',
                'बत्तीस',
                'एकतीस',
                'तीस',
                'उनन्तीस',
                'अठाइस',
                'सत्ताइस',
                'छब्बीस',
                'पच्चीस',
                'चौबीस',
                'तेइस',
                'बाइस',
                'एक्काइस',
                'बीस',
                'उन्नाइस',
                'अठार',
                'सत्र',
                'सोह्र',
                'पन्ध्र',
                'चौध',
                'तेह्र',
                'बाह्र',
                'एघार',
                'दश',
                'नौ',
                'आठ',
                'सात',
                'छ',
                'पाँच',
                'चार',
                'तीन',
                'दुई',
                'एक',
                'शून्य'
            ]



        self.mid_numwords = [(100, "सय")]

        self.high_numwords = [
            (11, "खर्ब"),
            (9, "अर्ब"),
            (7, "करोड"),
            (5, "लाख"),
            (3, "हजार"),
        ]

        self.pointword = "दशमलव"
        self.negword = "माइनस "

    def set_high_numwords(self, high):
        for n, word in self.high_numwords:
            self.cards[10 ** n] = word

    def merge(self, lpair, rpair):
        ltext, lnum = lpair
        rtext, rnum = rpair

        if lnum == 1 and rnum < 100:
            return rtext, rnum
        elif lnum >= 100 > rnum:
            return "%s %s" % (ltext, rtext), lnum + rnum
        elif rnum > lnum:
            return "%s %s" % (ltext, rtext), lnum * rnum

        return "%s %s" % (ltext, rtext), lnum + rnum

    def to_ordinal(self, value):
        if value in self._irregular_ordinals:
            return self._irregular_ordinals[value]

        cardinal = self.to_cardinal(value)
        return cardinal + self._regular_ordinal_suffix

    def _convert_to_nepali_numerals(self, value):
        return "".join(
            map(self._digits_to_nepali_digits.__getitem__, str(value))
        )

    def to_ordinal_num(self, value):
        if value in self._irregular_ordinals_nums:
            return self._irregular_ordinals_nums[value]

        return (
            self._convert_to_nepali_numerals(value)
            + self._regular_ordinal_suffix
        )
