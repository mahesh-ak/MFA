# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.
# Copyright (c) 2018, Abdullah Alhazmy, Alhazmy13.  All Rights Reserved.
# Copyright (c) 2020, Hamidreza Kalbasi.  All Rights Reserved.
# Copyright (c) 2023, Nika Soltani Tehrani.  All Rights Reserved.

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

from .lang_EU import Num2Word_EU


class Num2Word_ML(Num2Word_EU):

    def set_high_numwords(self, high):
        for n, word in self.high_numwords:
            self.cards[10**n] = word

    def setup(self):

        self.low_numwords = [
            "തൊണ്ണൂറത്തി ഒമ്പത്",
            "തൊണ്ണൂറത്തി എട്ട്",
            "തൊണ്ണൂറത്തി ഏഴ്",
            "തൊണ്ണൂറത്തി ആറ്",
            "തൊണ്ണൂറത്തി അഞ്ച്",
            "തൊണ്ണൂറത്തി നാല്",
            "തൊണ്ണൂറത്തി മൂന്ന്",
            "തൊണ്ണൂറത്തി രണ്ട്",
            "തൊണ്ണൂറത്തി ഒന്ന്",
            "തൊണ്ണൂറ്",

            "എൺപത്തി ഒമ്പത്",
            "എൺപത്തി എട്ട്",
            "എൺപത്തി ഏഴ്",
            "എൺപത്തി ആറ്",
            "എൺപത്തി അഞ്ച്",
            "എൺപത്തി നാല്",
            "എൺപത്തി മൂന്ന്",
            "എൺപത്തി രണ്ട്",
            "എൺപത്തി ഒന്ന്",
            "എൺപത്",

            "എഴുപത്തി ഒമ്പത്",
            "എഴുപത്തി എട്ട്",
            "എഴുപത്തി ഏഴ്",
            "എഴുപത്തി ആറ്",
            "എഴുപത്തി അഞ്ച്",
            "എഴുപത്തി നാല്",
            "എഴുപത്തി മൂന്ന്",
            "എഴുപത്തി രണ്ട്",
            "എഴുപത്തി ഒന്ന്",
            "എഴുപത്",

            "അറുപത്തി ഒമ്പത്",
            "അറുപത്തി എട്ട്",
            "അറുപത്തി ഏഴ്",
            "അറുപത്തി ആറ്",
            "അറുപത്തി അഞ്ച്",
            "അറുപത്തി നാല്",
            "അറുപത്തി മൂന്ന്",
            "അറുപത്തി രണ്ട്",
            "അറുപത്തി ഒന്ന്",
            "അറുപത്",

            "അമ്പത്തി ഒമ്പത്",
            "അമ്പത്തി എട്ട്",
            "അമ്പത്തി ഏഴ്",
            "അമ്പത്തി ആറ്",
            "അമ്പത്തി അഞ്ച്",
            "അമ്പത്തി നാല്",
            "അമ്പത്തി മൂന്ന്",
            "അമ്പത്തി രണ്ട്",
            "അമ്പത്തി ഒന്ന്",
            "അമ്പത്",

            "നാല്പത്തി ഒമ്പത്",
            "നാല്പത്തി എട്ട്",
            "നാല്പത്തി ഏഴ്",
            "നാല്പത്തി ആറ്",
            "നാല്പത്തി അഞ്ച്",
            "നാല്പത്തി നാല്",
            "നാല്പത്തി മൂന്ന്",
            "നാല്പത്തി രണ്ട്",
            "നാല്പത്തി ഒന്ന്",
            "നാല്പത്",

            "മുപ്പത്തി ഒമ്പത്",
            "മുപ്പത്തി എട്ട്",
            "മുപ്പത്തി ഏഴ്",
            "മുപ്പത്തി ആറ്",
            "മുപ്പത്തി അഞ്ച്",
            "മുപ്പത്തി നാല്",
            "മുപ്പത്തി മൂന്ന്",
            "മുപ്പത്തി രണ്ട്",
            "മുപ്പത്തി ഒന്ന്",
            "മുപ്പത്",

            "ഇരുപത്തി ഒമ്പത്",
            "ഇരുപത്തി എട്ട്",
            "ഇരുപത്തി ഏഴ്",
            "ഇരുപത്തി ആറ്",
            "ഇരുപത്തി അഞ്ച്",
            "ഇരുപത്തി നാല്",
            "ഇരുപത്തി മൂന്ന്",
            "ഇരുപത്തി രണ്ട്",
            "ഇരുപത്തി ഒന്ന്",
            "ഇരുപത്",

            "പത്തൊമ്പത്",
            "പതിനെട്ട്",
            "പതിനേഴ്",
            "പതിനാറ്",
            "പതിനഞ്ച്",
            "പതിനാല്",
            "പതിമൂന്ന്",
            "പന്ത്രണ്ട്",
            "പതിനൊന്ന്",
            "പത്ത്",

            "ഒമ്പത്",
            "എട്ട്",
            "ഏഴ്",
            "ആറ്",
            "അഞ്ച്",
            "നാല്",
            "മൂന്ന്",
            "രണ്ട്",
            "ഒന്ന്",
            "പൂജ്യം",
        ]

        self.mid_numwords = [(100, "നൂറ്")]

        self.high_numwords = [
            (7, "കോടി"),
            (5, "ലക്ഷം"),
            (3, "ആയിരം"),
        ]

        self.pointword = "പുള്ളി"
        self.negword = "മൈനസ് "

        self.hundred_map = {
            100: "നൂറ്",
            200: "ഇരുനൂറ്",
            300: "മുന്നൂറ്",
            400: "നാനൂറ്",
            500: "അഞ്ഞൂറ്",
            600: "അറുനൂറ്",
            700: "എഴുനൂറ്",
            800: "എണ്ണൂറ്",
            900: "തൊള്ളായിരം"
        }

    def _normalize_one(self, text):
        return "ഒരു" if text == "ഒന്ന്" else text

    def _inflect(self, word):
        if word.endswith("നൂറ്"):
            return word.replace("നൂറ്", "നൂറ്റി")
        if word.endswith("ആയിരം"):
            return word.replace("ആയിരം", "ആയിരത്തി")
        if word.endswith("ലക്ഷം"):
            return word.replace("ലക്ഷം", "ലക്ഷത്തി")
        if word.endswith("കോടി"):
            return word
        return word

    def merge(self, lpair, rpair):
        ltext, lnum = lpair
        rtext, rnum = rpair

        # irregular hundreds
        if lnum * rnum in self.hundred_map:
            return (self.hundred_map[lnum * rnum], lnum * rnum)

        if lnum == 1 and rnum < 100:
            return (rtext, rnum)

        elif 100 > lnum > rnum:
            return ("%s %s" % (ltext, rtext), lnum + rnum)

        elif lnum >= 100 and rnum < lnum:
            ltext = self._inflect(ltext)
            return ("%s %s" % (ltext, rtext), lnum + rnum)

        elif rnum > lnum:
            ltext = self._normalize_one(ltext)

            if lnum == 1:
                return (rtext, rnum)

            return ("%s %s" % (ltext, rtext), lnum * rnum)

        return ("%s %s" % (ltext, rtext), lnum + rnum)

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return "%s%s" % (value, "ാം")

    def to_ordinal(self, value):
        self.verify_ordinal(value)

        if value != 1:
            outwords = self.to_cardinal(value)
        else:
            return "ഒന്നാം"

        # Fix virama ending
        if outwords.endswith("്"):
            outwords = outwords[:-1]
        return outwords + "ാം"