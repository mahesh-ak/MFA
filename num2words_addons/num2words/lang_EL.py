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


## TODO: Fix gender, number agreement

from __future__ import unicode_literals

from .base import Num2Word_Base
from .utils import get_digits, splitbyx

ZERO = ('μηδέν',)

ONES = {
    1: ('ένα',),
    2: ('δύο',),
    3: ('τρία',),
    4: ('τέσσερα',),
    5: ('πέντε',),
    6: ('έξι',),
    7: ('επτά',),
    8: ('οκτώ',),
    9: ('εννέα',),
}

TENS = {
    0: ('δέκα',),
    1: ('έντεκα',),
    2: ('δώδεκα',),
    3: ('δεκατρία',),
    4: ('δεκατέσσερα',),
    5: ('δεκαπέντε',),
    6: ('δεκαέξι',),
    7: ('δεκαεπτά',),
    8: ('δεκαοκτώ',),
    9: ('δεκαεννέα',),
}

TWENTIES = {
    2: ('είκοσι',),
    3: ('τριάντα',),
    4: ('σαράντα',),
    5: ('πενήντα',),
    6: ('εξήντα',),
    7: ('εβδομήντα',),
    8: ('ογδόντα',),
    9: ('ενενήντα',),
}

HUNDREDS = {
    1: ('εκατό',),
    2: ('διακόσια',),
    3: ('τριακόσια',),
    4: ('τετρακόσια',),
    5: ('πεντακόσια',),
    6: ('εξακόσια',),
    7: ('επτακόσια',),
    8: ('οκτακόσια',),
    9: ('εννιακόσια',),
}

THOUSANDS = {
    1: ('χίλια', 'χιλιάδες', 'χιλιάδες'),  # 10^3
    2: ('εκατομμύριο', 'εκατομμύρια', 'εκατομμύρια'),  # 10^6
    3: ('δισεκατομμύριο', 'δισεκατομμύρια', 'δισεκατομμύρια'),  # 10^9
    4: ('τρισεκατομμύριο', 'τρισεκατομμύρια', 'τρισεκατομμύρια'),  # 10^12
    5: ('τετρασεκατομμύριο', 'τετρασεκατομμύρια', 'τετρασεκατομμύρια'),
    6: ('πεντασεκατομμύριο', 'πεντασεκατομμύρια', 'πεντασεκατομμύρια'),
    7: ('εξασεκατομμύριο', 'εξασεκατομμύρια', 'εξασεκατομμύρια'),
    8: ('επτασεκατομμύριο', 'επτασεκατομμύρια', 'επτασεκατομμύρια'),
    9: ('οκτασεκατομμύριο', 'οκτασεκατομμύρια', 'οκτασεκατομμύρια'),
    10: ('εννεασεκατομμύριο', 'εννεασεκατομμύρια', 'εννεασεκατομμύρια'),
}


class Num2Word_EL(Num2Word_Base):
    def setup(self):
        self.negword = "μείον"
        self.pointword = "κόμμα"

    def to_cardinal(self, number):
        n = str(number).replace(',', '.')
        if '.' in n:
            left, right = n.split('.')
            leading_zero_count = len(right) - len(right.lstrip('0'))
            decimal_part = ((ZERO[0] + ' ') * leading_zero_count +
                            self._int2word(int(right)))
            return '%s %s %s' % (
                self._int2word(int(left)),
                self.pointword,
                decimal_part
            )
        else:
            return self._int2word(int(n))

    def pluralize(self, n, forms):
        if n == 1:
            return forms[0]
        return forms[1]

    def to_ordinal(self, number):
        raise NotImplementedError()

    def _int2word(self, n):
        if n == 0:
            return ZERO[0]

        words = []
        chunks = list(splitbyx(str(n), 3))
        i = len(chunks)

        for x in chunks:
            i -= 1

            if x == 0:
                continue

            n1, n2, n3 = get_digits(x)

            # hundreds
            if n3 > 0:
                if n3 == 1 and (n2 > 0 or n1 > 0):
                    words.append('εκατόν')
                else:
                    words.append(HUNDREDS[n3][0])

            # tens
            if n2 > 1:
                words.append(TWENTIES[n2][0])

                if n1 > 0:
                    words.append(ONES[n1][0])

            elif n2 == 1:
                words.append(TENS[n1][0])

            elif n1 > 0:
                # 🔴 FIX: skip "ένα" before "χίλια"
                if not (n1 == 1 and n2 == 0 and n3 == 0 and i == 1):
                    words.append(ONES[n1][0])
            # thousands / millions
            if i > 0:
                if x == 1 and i == 1:
                    words.append('χίλια')
                else:
                    words.append(self.pluralize(x, THOUSANDS[i]))

        return ' '.join(words)