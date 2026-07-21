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


class Num2Word_MR(Num2Word_Base):
    """
    Marathi (MR) Num2Word class
    """

    _irregular_ordinals = {
        0: "शून्यावा",
        1: "पहिला",
        2: "दुसरा",
        3: "तिसरा",
        4: "चौथा",
        5: "पाचवा",
        6: "सहावा",
    }

    _irregular_ordinals_nums = {
        0: "०वा",
        1: "१ला",
        2: "२रा",
        3: "३रा",
        4: "४था",
        5: "५वा",
        6: "६वा",
    }

    _marathi_digits = "०१२३४५६७८९"
    _digits_to_marathi_digits = dict(zip(string.digits, _marathi_digits))

    _regular_ordinal_suffix = "वा"

    def setup(self):
        self.low_numwords = [
            "नव्व्याण्णव",
            "अठ्ठ्याण्णव",
            "सत्त्याण्णव",
            "शह्याण्णव",
            "पंच्याण्णव",
            "चौऱ्याण्णव",
            "त्र्याण्णव",
            "ब्याण्णव",
            "एक्याण्णव",
            "नव्वद",
            "एकोणनव्वद",
            "अठ्ठ्याऐंशी",
            "सत्त्याऐंशी",
            "सह्यांशी",
            "पंच्याऐंशी",
            "चौरेऐंशी",
            "त्र्याऐंशी",
            "ब्याऐंशी",
            "एक्याऐंशी",
            "ऐंशी",
            "एकोणऐंशी",
            "अठ्ठ्याहत्तर",
            "सत्याहत्तर",
            "शहात्तर",
            "पंच्याहत्तर",
            "चौरेहत्तर",
            "त्र्याहत्तर",
            "बहात्तर",
            "एकाहत्तर",
            "सत्तर",
            "एकोणसत्तर",
            "अडुसष्ट",
            "सदुसष्ट",
            "सहासष्ट",
            "पासष्ट",
            "चौसष्ट",
            "त्रेसष्ट",
            "बासष्ट",
            "एकसष्ट",
            "साठ",
            "एकोणसाठ",
            "अठ्ठावन्न",
            "सत्तावन्न",
            "छप्पन्न",
            "पंचावन्न",
            "चौवन्न",
            "त्रेपन्न",
            "बावन्न",
            "एकावन्न",
            "पन्नास",
            "एकोणपन्नास",
            "अठ्ठेचाळीस",
            "सत्तेचाळीस",
            "सेहेचाळीस",
            "पंचेचाळीस",
            "चव्वेचाळीस",
            "त्रेचाळीस",
            "बेचाळीस",
            "एकेचाळीस",
            "चाळीस",
            "एकोणचाळीस",
            "अडतीस",
            "सदतीस",
            "छत्तीस",
            "पस्तीस",
            "चौतीस",
            "तेहतीस",
            "बत्तीस",
            "एकतीस",
            "तीस",
            "एकोणतीस",
            "अठ्ठावीस",
            "सत्तावीस",
            "सव्वीस",
            "पंचवीस",
            "चोवीस",
            "तेवीस",
            "बावीस",
            "एकवीस",
            "वीस",
            "एकोणीस",
            "अठरा",
            "सतरा",
            "सोळा",
            "पंधरा",
            "चौदा",
            "तेरा",
            "बारा",
            "अकरा",
            "दहा",
            "नऊ",
            "आठ",
            "सात",
            "सहा",
            "पाच",
            "चार",
            "तीन",
            "दोन",
            "एक",
            "शून्य",
        ]

        self.mid_numwords = [(100, "शंभर")]

        self.high_numwords = [
            (11, "खर्व"),
            (9, "अब्ज"),
            (7, "कोटी"),
            (5, "लाख"),
            (3, "हजार"),
        ]

        self.pointword = "दशांश"
        self.negword = "मायनस "

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

        return self.to_cardinal(value) + self._regular_ordinal_suffix

    def _convert_to_marathi_numerals(self, value):
        return "".join(map(self._digits_to_marathi_digits.__getitem__,
                           str(value)))

    def to_ordinal_num(self, value):
        if value in self._irregular_ordinals_nums:
            return self._irregular_ordinals_nums[value]

        return self._convert_to_marathi_numerals(value) + self._regular_ordinal_suffix