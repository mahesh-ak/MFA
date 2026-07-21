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


class Num2Word_OR(Num2Word_Base):
    """
    Odia (OR) Num2Word class
    """

    _irregular_ordinals = {
        0: "ଶୂନ୍ୟ",
        1: "ପ୍ରଥମ",
        2: "ଦ୍ୱିତୀୟ",
        3: "ତୃତୀୟ",
        4: "ଚତୁର୍ଥ",
        6: "ଷଷ୍ଠ",
    }

    _irregular_ordinals_nums = {
        0: "୦",
        1: "୧ମ",
        2: "୨ୟ",
        3: "୩ୟ",
        4: "୪ର୍ଥ",
        6: "୬ଷ୍ଠ",
    }

    _odia_digits = "୦୧୨୩୪୫୬୭୮୯"
    _digits_to_odia_digits = dict(zip(string.digits, _odia_digits))

    _regular_ordinal_suffix = "ତମ"

    def setup(self):
        self.low_numwords = [
            'ନିନାନବେ',
            'ଅଠାନବେ',
            'ସତାନବେ',
            'ଛଅନବେ',
            'ପଞ୍ଚାନବେ',
            'ଚଉରାନବେ',
            'ତେରାନବେ',
            'ବାନବେ',
            'ଏକାନବେ',
            'ନବେ',
            'ନବାଶୀ',
            'ଅଠାଶୀ',
            'ସତାଶୀ',
            'ଛଅଶୀ',
            'ପଞ୍ଚାଶୀ',
            'ଚଉରାଶୀ',
            'ତେଆଶୀ',
            'ବୟାଶୀ',
            'ଏକାଶୀ',
            'ଅଶୀ',
            'ଊଣଅଶୀ',
            'ଅଠହତର',
            'ସତହତର',
            'ଛହତର',
            'ପଞ୍ଚହତର',
            'ଚଉହତର',
            'ତେହତର',
            'ବାହତର',
            'ଏକସତର',
            'ସତର',
            'ଊଣସତର',
            'ଅଠଷାଠି',
            'ସତଷାଠି',
            'ଛଷାଠି',
            'ପଞ୍ଚଷାଠି',
            'ଚଉଷାଠି',
            'ତେଷାଠି',
            'ବାଷାଠି',
            'ଏକଷାଠି',
            'ଷାଠି',
            'ଊଣଷାଠି',
            'ଅଠାବନ',
            'ସତାବନ',
            'ଛପ୍ପନ',
            'ପଚାବନ',
            'ଚଉବନ',
            'ତେବନ',
            'ବାବନ',
            'ଏକାବନ',
            'ପଚାଶ',
            'ଊଣପଚାଶ',
            'ଅଠଚାଳିଶ',
            'ସତଚାଳିଶ',
            'ଛଅଚାଳିଶ',
            'ପଞ୍ଚଚାଳିଶ',
            'ଚଉଚାଳିଶ',
            'ତେତାଳିଶ',
            'ବୟାଳିଶ',
            'ଏକଚାଳିଶ',
            'ଚାଳିଶ',
            'ଊଣଚାଳିଶ',
            'ଅଠତିରିଶ',
            'ସତତିରିଶ',
            'ଛତିରିଶ',
            'ପଞ୍ଚତିରିଶ',
            'ଚଉତିରିଶ',
            'ତେତିରିଶ',
            'ବତିରିଶ',
            'ଏକତିରିଶ',
            'ତିରିଶ',
            'ଉଣତିରିଶ',
            'ଅଠାଇଶ',
            'ସତାଇଶି',
            'ଛବିଶ',
            'ପଚିଶ',
            'ଚଉବିଶ',
            'ତେଇଶ',
            'ବାଇଶ',
            'ଏକୋଇଶ',
            'କୋଡ଼ିଏ',
            'ଊଣେଇଶ',
            'ଅଠାର',
            'ସତର',
            'ଷୋଳ',
            'ପନ୍ଦର',
            'ଚଉଦ',
            'ତେର',
            'ବାର',
            'ଏଗାର',
            'ଦଶ',
            'ନଅ',
            'ଆଠ',
            'ସାତ',
            'ଛଅ',
            'ପାଞ୍ଚ',
            'ଚାରି',
            'ତିନି',
            'ଦୁଇ',
            'ଏକ',
            'ଶୂନ୍ୟ'
        ]


        self.mid_numwords = [(100, "ଶତ")]

        self.high_numwords = [
            (11, "ଖରବ"),
            (9, "ଅରବ"),
            (7, "କୋଟି"),
            (5, "ଲକ୍ଷ"),
            (3, "ହଜାର"),
        ]

        self.pointword = "ଦଶମିକ"
        self.negword = "ମାଇନସ "

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

    def _convert_to_odia_numerals(self, value):
        return "".join(
            map(self._digits_to_odia_digits.__getitem__, str(value))
        )

    def to_ordinal_num(self, value):
        if value in self._irregular_ordinals_nums:
            return self._irregular_ordinals_nums[value]

        return self._convert_to_odia_numerals(value) + self._regular_ordinal_suffix