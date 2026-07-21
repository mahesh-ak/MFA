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

from __future__ import unicode_literals

from unittest import TestCase

from num2words import num2words


from unittest import TestCase
from num2words import num2words


class Num2WordsELTest(TestCase):

    def test_cardinal(self):
        self.assertEqual(num2words(100, lang='el'), "εκατό")
        self.assertEqual(num2words(101, lang='el'), "εκατόν ένα")
        self.assertEqual(num2words(110, lang='el'), "εκατόν δέκα")
        self.assertEqual(num2words(115, lang='el'), "εκατόν δεκαπέντε")
        self.assertEqual(num2words(123, lang='el'), "εκατόν είκοσι τρία")

        self.assertEqual(num2words(1000, lang='el'), "χίλια")
        self.assertEqual(num2words(1001, lang='el'), "χίλια ένα")
        self.assertEqual(num2words(2012, lang='el'), "δύο χιλιάδες δώδεκα")

        self.assertEqual(
            num2words(10.02, lang='el'),
            "δέκα κόμμα μηδέν δύο"
        )
        self.assertEqual(
            num2words(15.007, lang='el'),
            "δεκαπέντε κόμμα μηδέν μηδέν επτά"
        )

        self.assertEqual(
            num2words(12519.85, lang='el'),
            "δώδεκα χιλιάδες πεντακόσια δεκαεννέα κόμμα ογδόντα πέντε"
        )

        self.assertEqual(
            num2words(123.50, lang='el'),
            "εκατόν είκοσι τρία κόμμα πέντε"
        )

        self.assertEqual(
            num2words(1234567890, lang='el'),
            "ένα δισεκατομμύριο διακόσια τριάντα τέσσερα εκατομμύρια "
            "πεντακόσια εξήντα επτά χιλιάδες οκτακόσια ενενήντα"
        )

#        self.assertEqual(
#            num2words(215461407892039002157189883901676, lang='el'),
#            "διακόσια δεκαπέντε κουιντισεκατομμύρια τετρακόσια εξήντα ένα "
#            "τετρακισεκατομμύρια τετρακόσια επτά τετρακις εκατομμύρια "
#            "οκτακόσια ενενήντα δύο τρισεκατομμύρια τριάντα εννέα δισεκατομμύρια "
#            "δύο δισεκατομμύρια εκατόν πενήντα επτά δισεκατομμύρια "
#            "εκατόν ογδόντα εννέα εκατομμύρια οκτακόσια ογδόντα τρία "
#            "εκατομμύρια εννιακόσιες μία χιλιάδες εξακόσια εβδομήντα έξι"
#        )

#        self.assertEqual(
#            num2words(719094234693663034822824384220291, lang='el'),
#            "επτακόσια δεκαεννέα κουιντισεκατομμύρια ενενήντα τέσσερα "
#            "τετρακισεκατομμύρια διακόσια τριάντα τέσσερα τετρακις εκατομμύρια "
#            "εξακόσια ενενήντα τρία τρισεκατομμύρια εξακόσια εξήντα τρία "
#            "δισεκατομμύρια τριάντα τέσσερα δισεκατομμύρια οκτακόσια είκοσι δύο "
#            "δισεκατομμύρια οκτακόσια είκοσι τέσσερα εκατομμύρια "
#            "τριακόσια ογδόντα τέσσερα εκατομμύρια διακόσιες είκοσι χιλιάδες "
#            "διακόσια ενενήντα ένα"
#        )