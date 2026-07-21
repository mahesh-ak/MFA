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


class Num2Word_UR(Num2Word_Base):
    """
    Urdu (UR) Num2Word class
    """

    _irregular_ordinals = {
        0: "صفر",
        1: "پہلا",
        2: "دوسرا",
        3: "تیسرا",
        4: "چوتھا",
        6: "چھٹا",
    }

    _irregular_ordinals_nums = {
        0: "۰",
        1: "۱لا",
        2: "۲را",
        3: "۳را",
        4: "۴ھا",
        6: "۶ٹا",
    }

    _urdu_digits = "۰۱۲۳۴۵۶۷۸۹"
    _digits_to_urdu_digits = dict(zip(string.digits, _urdu_digits))

    _regular_ordinal_suffix = "واں"

    def setup(self):
        self.low_numwords = [
            "ننانوے",
            "اٹھانوے",
            "ستانوے",
            "چھیانوے",
            "پچانوے",
            "چورانوے",
            "ترانوے",
            "بانوے",
            "اکیانوے",
            "نوے",
            "نواسی",
            "اٹھاسی",
            "ستاسی",
            "چھیاسی",
            "پچاسی",
            "چوراسی",
            "تراسی",
            "بیاسی",
            "اکیاسی",
            "اسی",
            "اناسی",
            "اٹھہتر",
            "ستتر",
            "چھہتر",
            "پچھتر",
            "چہتر",
            "تہتر",
            "بہتر",
            "اکہتر",
            "ستر",
            "انہتر",
            "اڑسٹھ",
            "سڑسٹھ",
            "چھیاسٹھ",
            "پینسٹھ",
            "چونسٹھ",
            "تریسٹھ",
            "باسٹھ",
            "اکسٹھ",
            "ساٹھ",
            "انسٹھ",
            "اٹھاون",
            "ستاون",
            "چھپن",
            "پچپن",
            "چون",
            "تریپن",
            "باون",
            "اکیاون",
            "پچاس",
            "انچاس",
            "اڑتالیس",
            "سینتالیس",
            "چھیالیس",
            "پینتالیس",
            "چوالیس",
            "تینتالیس",
            "بیالیس",
            "اکتالیس",
            "چالیس",
            "انتالیس",
            "اڑتیس",
            "سینتیس",
            "چھتیس",
            "پینتیس",
            "چونتیس",
            "تینتیس",
            "بتیس",
            "اکتیس",
            "تیس",
            "انتیس",
            "اٹھائیس",
            "ستائیس",
            "چھبیس",
            "پچیس",
            "چوبیس",
            "تیئیس",
            "بائیس",
            "اکیس",
            "بیس",
            "انیس",
            "اٹھارہ",
            "سترہ",
            "سولہ",
            "پندرہ",
            "چودہ",
            "تیرہ",
            "بارہ",
            "گیارہ",
            "دس",
            "نو",
            "آٹھ",
            "سات",
            "چھ",
            "پانچ",
            "چار",
            "تین",
            "دو",
            "ایک",
            "صفر",
        ]

        self.mid_numwords = [(100, "سو")]

        self.high_numwords = [
            (11, "کھرب"),
            (9, "ارب"),
            (7, "کروڑ"),
            (5, "لاکھ"),
            (3, "ہزار"),
        ]

        self.pointword = "اعشاریہ"
        self.negword = "منفی "

    def set_high_numwords(self, high):
        for n, word in self.high_numwords:
            self.cards[10**n] = word

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

    def _convert_to_urdu_numerals(self, value):
        return "".join(
            map(self._digits_to_urdu_digits.__getitem__, str(value))
        )

    def to_ordinal_num(self, value):
        if value in self._irregular_ordinals_nums:
            return self._irregular_ordinals_nums[value]

        return self._convert_to_urdu_numerals(value) + self._regular_ordinal_suffix