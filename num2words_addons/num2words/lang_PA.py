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


class Num2Word_PA(Num2Word_Base):
    """
    Punjabi (PA) Num2Word class (Gurmukhi)
    """

    _irregular_ordinals = {
        0: "ਸਿਫ਼ਰ",
        1: "ਪਹਿਲਾ",
        2: "ਦੂਜਾ",
        3: "ਤੀਜਾ",
        4: "ਚੌਥਾ",
        6: "ਛੇਵਾਂ",
    }

    _irregular_ordinals_nums = {
        0: "੦",
        1: "੧ਲਾ",
        2: "੨ਰਾ",
        3: "੩ਰਾ",
        4: "੪ਥਾ",
        6: "੬ਵਾਂ",
    }

    _punjabi_digits = "੦੧੨੩੪੫੬੭੮੯"
    _digits_to_punjabi_digits = dict(zip(string.digits, _punjabi_digits))

    _regular_ordinal_suffix = "ਵਾਂ"

    def setup(self):
        self.low_numwords = [
            "ਨਿੰਨਾਣਵੇ",
            "ਅਠਾਣਵੇ",
            "ਸਤਾਣਵੇ",
            "ਛਿਆਣਵੇ",
            "ਪਚਾਣਵੇ",
            "ਚੌਰਾਣਵੇ",
            "ਤਰਾਣਵੇ",
            "ਬਾਣਵੇ",
            "ਇਕਿਆਣਵੇ",
            "ਨੱਬੇ",
            "ਨਵਾਸੀ",
            "ਅਠਾਸੀ",
            "ਸਤਾਸੀ",
            "ਛਿਆਸੀ",
            "ਪਚਾਸੀ",
            "ਚੌਰਾਸੀ",
            "ਤਰਾਸੀ",
            "ਬਿਆਸੀ",
            "ਇਕਿਆਸੀ",
            "ਅੱਸੀ",
            "ਉਣਾਸੀ",
            "ਅਠੱਤਰ",
            "ਸਤੱਤਰ",
            "ਛਿਹੱਤਰ",
            "ਪਚੱਤਰ",
            "ਚੌਹੱਤਰ",
            "ਤਿਹੱਤਰ",
            "ਬਹੱਤਰ",
            "ਇਕੱਤਰ",
            "ਸਤੱਰ",
            "ਉਣੱਤਰ",
            "ਅਠਾਸਠ",
            "ਸਤਾਸਠ",
            "ਛਿਆਸਠ",
            "ਪੈਂਸਠ",
            "ਚੌਂਸਠ",
            "ਤਰਾਹਠ",
            "ਬਾਹਠ",
            "ਇਕਾਹਠ",
            "ਸੱਠ",
            "ਉਣਸੱਠ",
            "ਅਠਾਵੰਜਾ",
            "ਸਤਾਵੰਜਾ",
            "ਛਵੰਜਾ",
            "ਪਚਵੰਜਾ",
            "ਚੌਵੰਜਾ",
            "ਤਰਵੰਜਾ",
            "ਬਵੰਜਾ",
            "ਇਕਵੰਜਾ",
            "ਪੰਜਾਹ",
            "ਉਣੰਜਾ",
            "ਅਠਤਾਲੀ",
            "ਸੈਂਤਾਲੀ",
            "ਛਿਆਲੀ",
            "ਪੈਂਤਾਲੀ",
            "ਚੌਂਤਾਲੀ",
            "ਤੈਂਤਾਲੀ",
            "ਬਿਆਲੀ",
            "ਇਕਤਾਲੀ",
            "ਚਾਲੀ",
            "ਉਣਤਾਲੀ",
            "ਅਠੱਤੀ",
            "ਸੈਂਤੀ",
            "ਛੱਤੀ",
            "ਪੈਂਤੀ",
            "ਚੌਂਤੀ",
            "ਤੈਂਤੀ",
            "ਬੱਤੀ",
            "ਇਕੱਤੀ",
            "ਤੀਹ",
            "ਉਣੱਤੀ",
            "ਅਠਾਈ",
            "ਸਤਾਈ",
            "ਛੱਬੀ",
            "ਪੱਚੀ",
            "ਚੌਵੀ",
            "ਤੇਈ",
            "ਬਾਈ",
            "ਇੱਕੀ",
            "ਵੀਹ",
            "ਉੱਨੀ",
            "ਅਠਾਰਾਂ",
            "ਸਤਾਰਾਂ",
            "ਸੋਲ੍ਹਾਂ",
            "ਪੰਦਰਾਂ",
            "ਚੌਦਾਂ",
            "ਤੇਰਾਂ",
            "ਬਾਰਾਂ",
            "ਗਿਆਰਾਂ",
            "ਦੱਸ",
            "ਨੌਂ",
            "ਅੱਠ",
            "ਸੱਤ",
            "ਛੇ",
            "ਪੰਜ",
            "ਚਾਰ",
            "ਤਿੰਨ",
            "ਦੋ",
            "ਇੱਕ",
            "ਸਿਫ਼ਰ",
        ]

        self.mid_numwords = [(100, "ਸੌ")]

        self.high_numwords = [
            (11, "ਖਰਬ"),
            (9, "ਅਰਬ"),
            (7, "ਕਰੋੜ"),
            (5, "ਲੱਖ"),
            (3, "ਹਜ਼ਾਰ"),
        ]

        self.pointword = "ਦਸ਼ਮਲਵ"
        self.negword = "ਮਾਈਨਸ "

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

    def _convert_to_punjabi_numerals(self, value):
        return "".join(
            map(self._digits_to_punjabi_digits.__getitem__, str(value))
        )

    def to_ordinal_num(self, value):
        if value in self._irregular_ordinals_nums:
            return self._irregular_ordinals_nums[value]

        return self._convert_to_punjabi_numerals(value) + self._regular_ordinal_suffix