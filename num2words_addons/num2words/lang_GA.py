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

from . import lang_EU


# --- Irish mutation helpers (minimal, controlled) ---

def lenition(word):
    if not word:
        return word
    if word[0] in "bcdfgmpst":
        return word[0] + "h" + word[1:]
    return word


def mutate_after_a(word, num):
    # Only correct rule needed now: "a haon"
    if num == 1:
        return "h" + word
    return word


class Num2Word_GA(lang_EU.Num2Word_EU):

    def set_high_numwords(self, high):
        max = 3 + 3 * len(high)
        for word, n in zip(high, range(max, 3, -3)):
            self.cards[10 ** n] = word + "illiún"

    def setup(self):
        super(Num2Word_GA, self).setup()

        self.negword = "lúide "
        self.pointword = "ponc"
        self.exclude_title = ["agus", "ponc", "lúide"]

        # --- core numbers (NO mutation inside data!) ---
        self.low_numwords = [
            "fiche", "naoi déag", "ocht déag", "seacht déag",
            "sé déag", "cúig déag", "ceathair déag", "trí déag",
            "dhá déag", "aon déag", "deich",
            "naoi", "ocht", "seacht", "sé",
            "cúig", "ceathair", "trí", "dó",
            "aon", "náid"
        ]

        self.mid_numwords = [
            (1000, "míle"),
            (100, "céad"),
            (90, "nócha"),
            (80, "ochtó"),
            (70, "seachtó"),
            (60, "seasca"),
            (50, "caoga"),
            (40, "daichead"),
            (30, "tríocha"),
        ]

        self.ords = {
            "aon": "céad",
            "dó": "dara",
            "trí": "tríú",
            "ceathair": "ceathrú",
            "cúig": "cúigiú",
            "sé": "séú",
            "seacht": "seachtú",
            "ocht": "ochtú",
            "naoi": "naoú",
            "deich": "deichiú",
        }

    # --- Core logic: ALL grammar happens here ---
    def merge(self, lpair, rpair):
        ltext, lnum = lpair
        rtext, rnum = rpair

        # drop "aon" before smaller numbers
        if lnum == 1 and rnum < 100:
            return (rtext, rnum)

        # 21–99 → "fiche a haon"
        if 100 > lnum > rnum:
            rtext = mutate_after_a(rtext, rnum)
            return ("%s a %s" % (ltext, rtext), lnum + rnum)

        # 100–999 → NO mutation after céad
        elif lnum >= 100 > rnum:
            return ("%s %s" % (ltext, rtext), lnum + rnum)

        # multiplication (míle, milliún…)
        elif rnum > lnum:
            if lnum == 1:
                return (rtext, rnum)
            return ("%s %s" % (ltext, rtext), lnum * rnum)

        return ("%s %s" % (ltext, rtext), lnum + rnum)

    # --- Ordinals ---
    def to_ordinal(self, value):
        self.verify_ordinal(value)
        words = self.to_cardinal(value).split(" ")
        last = words[-1]

        if last in self.ords:
            words[-1] = self.ords[last]
        else:
            words[-1] = last + "ú"

        return " ".join(words)

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return "%dú" % value

    # --- Year (simple for now) ---
    def to_year(self, val, suffix=None, longval=True):
        text = self.to_cardinal(val)
        return "%s %s" % (text, suffix) if suffix else text