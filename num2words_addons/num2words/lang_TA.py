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


class Num2Word_TA(Num2Word_EU):

    def set_high_numwords(self, high):
        for n, word in self.high_numwords:
            self.cards[10**n] = word

    def setup(self):

        self.low_numwords = [
            "தொண்ணூற்று ஒன்பது",
            "தொண்ணூற்று எட்டு",
            "தொண்ணூற்று ஏழு",
            "தொண்ணூற்று ஆறு",
            "தொண்ணூற்று ஐந்து",
            "தொண்ணூற்று நான்கு",
            "தொண்ணூற்று மூன்று",
            "தொண்ணூற்று இரண்டு",
            "தொண்ணூற்று ஒன்று",
            "தொண்ணூறு",

            "எண்பத்து ஒன்பது",
            "எண்பத்து எட்டு",
            "எண்பத்து ஏழு",
            "எண்பத்து ஆறு",
            "எண்பத்து ஐந்து",
            "எண்பத்து நான்கு",
            "எண்பத்து மூன்று",
            "எண்பத்து இரண்டு",
            "எண்பத்து ஒன்று",
            "எண்பது",

            "எழுபத்து ஒன்பது",
            "எழுபத்து எட்டு",
            "எழுபத்து ஏழு",
            "எழுபத்து ஆறு",
            "எழுபத்து ஐந்து",
            "எழுபத்து நான்கு",
            "எழுபத்து மூன்று",
            "எழுபத்து இரண்டு",
            "எழுபத்து ஒன்று",
            "எழுபது",

            "அறுபத்து ஒன்பது",
            "அறுபத்து எட்டு",
            "அறுபத்து ஏழு",
            "அறுபத்து ஆறு",
            "அறுபத்து ஐந்து",
            "அறுபத்து நான்கு",
            "அறுபத்து மூன்று",
            "அறுபத்து இரண்டு",
            "அறுபத்து ஒன்று",
            "அறுபது",

            "ஐம்பத்து ஒன்பது",
            "ஐம்பத்து எட்டு",
            "ஐம்பத்து ஏழு",
            "ஐம்பத்து ஆறு",
            "ஐம்பத்து ஐந்து",
            "ஐம்பத்து நான்கு",
            "ஐம்பத்து மூன்று",
            "ஐம்பத்து இரண்டு",
            "ஐம்பத்து ஒன்று",
            "ஐம்பது",

            "நாற்பத்து ஒன்பது",
            "நாற்பத்து எட்டு",
            "நாற்பத்து ஏழு",
            "நாற்பத்து ஆறு",
            "நாற்பத்து ஐந்து",
            "நாற்பத்து நான்கு",
            "நாற்பத்து மூன்று",
            "நாற்பத்து இரண்டு",
            "நாற்பத்து ஒன்று",
            "நாற்பது",

            "முப்பத்து ஒன்பது",
            "முப்பத்து எட்டு",
            "முப்பத்து ஏழு",
            "முப்பத்து ஆறு",
            "முப்பத்து ஐந்து",
            "முப்பத்து நான்கு",
            "முப்பத்து மூன்று",
            "முப்பத்து இரண்டு",
            "முப்பத்து ஒன்று",
            "முப்பது",

            "இருபத்து ஒன்பது",
            "இருபத்து எட்டு",
            "இருபத்து ஏழு",
            "இருபத்து ஆறு",
            "இருபத்து ஐந்து",
            "இருபத்து நான்கு",
            "இருபத்து மூன்று",
            "இருபத்து இரண்டு",
            "இருபத்து ஒன்று",
            "இருபது",

            "பத்தொன்பது",
            "பதினெட்டு",
            "பதினேழு",
            "பதினாறு",
            "பதினைந்து",
            "பதினான்கு",
            "பதிமூன்று",
            "பன்னிரண்டு",
            "பதினொன்று",
            "பத்து",

            "ஒன்பது",
            "எட்டு",
            "ஏழு",
            "ஆறு",
            "ஐந்து",
            "நான்கு",
            "மூன்று",
            "இரண்டு",
            "ஒன்று",
            "பூஜ்ஜியம்",
        ]

        self.mid_numwords = [(100, "நூறு")]

        self.high_numwords = [
            (7, "கோடி"),
            (5, "லட்சம்"),
            (3, "ஆயிரம்"),
        ]

        self.pointword = "புள்ளி"
        self.negword = "மைனஸ் "

        self.hundred_map = {
            100: "நூறு",
            200: "இருநூறு",
            300: "முந்நூறு",
            400: "நானூறு",
            500: "ஐந்நூறு",
            600: "அறுநூறு",
            700: "எழுநூறு",
            800: "எண்ணூறு",
            900: "தொள்ளாயிரம்"  # widely accepted modern Tamil for 900
        }

    def _normalize_one(self, text):
        return "ஒரு" if text == "ஒன்று" else text

    def _inflect(self, word):
        if word.endswith("ூறு"):
            return word.replace("ூறு" ,"ூற்று")
        if word.endswith("யிரம்"):
            return word.replace("யிரம்","யிரத்து")
        if word.endswith("லட்சம்"):
            return word.replace("லட்சம்", "லட்சத்து")
        if word.endswith("கோடி"):
            return word
        return word

    def merge(self, lpair, rpair):
        ltext, lnum = lpair
        rtext, rnum = rpair

        # ✅ HANDLE irregular hundreds
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
        return "%s%s" % (value, "வது")

    def to_ordinal(self, value):
        self.verify_ordinal(value)
        if value != 1:
            outwords = self.to_cardinal(value)
        else:
            outwords = 'முதல'

        if outwords.endswith("ு"):
            outwords = outwords[:-1]

        return outwords + "ாவது"