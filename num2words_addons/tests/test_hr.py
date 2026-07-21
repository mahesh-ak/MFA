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


class Num2WordsHRTest(TestCase):

    def test_cardinal(self):
        self.assertEqual("sto", num2words(100, lang='hr'))
        self.assertEqual("sto jedan", num2words(101, lang='hr'))
        self.assertEqual("sto deset", num2words(110, lang='hr'))
        self.assertEqual("sto petnaest", num2words(115, lang='hr'))
        self.assertEqual(
            "sto dvadeset tri", num2words(123, lang='hr')
        )
        self.assertEqual(
            "jedna tisuća", num2words(1000, lang='hr')
        )
        self.assertEqual(
            "jedna tisuća jedan", num2words(1001, lang='hr')
        )
        self.assertEqual(
            "dvije tisuće dvanaest", num2words(2012, lang='hr')
        )
        self.assertEqual(
            "dvanaest tisuća petsto devetnaest zapeta osamdeset pet",
            num2words(12519.85, lang='hr')
        )
        self.assertEqual(
            "jedan bilijun dvesta trideset četiri milijuna petsto "
            "šezdeset sedam tisuća osamsto devedeset",
            num2words(1234567890, lang='hr')
        )
        self.assertEqual(
            "dvesta petnaest nonilijuna četristo šezdeset jedan "
            "oktilijun četristo sedam septilijuna osamsto devedeset "
            "dva sekstilijuna trideset devet kvintilijuna dva kvadrilijuna "
            "sto pedeset sedam trilijuna sto osamdeset devet bilijuna "
            "osamsto osamdeset tri milijuna devetsto jedna tisuća "
            "šesto sedamdeset šest",
            num2words(215461407892039002157189883901676, lang='hr')
        )
        self.assertEqual(
            "sedamsto devetnaest nonilijuna devedeset četiri oktilijuna "
            "dvesta trideset četiri septilijuna šesto devedeset tri "
            "sekstilijuna šesto šezdeset tri kvintilijuna trideset "
            "četiri kvadrilijuna osamsto dvadeset dva trilijuna osamsto "
            "dvadeset četiri bilijuna trista osamdeset četiri milijuna "
            "dvesta dvadeset tisuća dvesta devedeset jedan",
            num2words(719094234693663034822824384220291, lang='hr')
        )
        self.assertEqual("pet", num2words(5, lang='hr'))
        self.assertEqual("petnaest", num2words(15, lang='hr'))
        self.assertEqual("sto pedeset četiri", num2words(154, lang='hr'))
        self.assertEqual(
            "jedna tisuća sto trideset pet",
            num2words(1135, lang='hr')
        )
        self.assertEqual(
            "četristo osamnaest tisuća petsto trideset jedan",
            num2words(418531, lang='hr'),
        )
        self.assertEqual(
            "jedan milijun sto trideset devet",
            num2words(1000139, lang='hr')
        )

    def test_floating_point(self):
        self.assertEqual("pet zapeta dva", num2words(5.2, lang='hr'))
        self.assertEqual(
            num2words(10.02, lang='hr'),
            "deset zapeta nula dva"
        )
        self.assertEqual(
            num2words(15.007, lang='hr'),
            "petnaest zapeta nula nula sedam"
        )
        self.assertEqual(
            "petsto šezdeset jedan zapeta četrdeset dva",
            num2words(561.42, lang='hr')
        )

    def test_to_ordinal(self):
        # @TODO: implement to_ordinal
        with self.assertRaises(NotImplementedError):
            num2words(1, lang='hr', to='ordinal')

    def test_to_currency(self):
        self.assertEqual(
            'jedan euro, nula centi',
            num2words(1.0, lang='hr', to='currency', currency='EUR')

        )
        self.assertEqual(
            'dva eura, nula centi',
            num2words(2.0, lang='hr', to='currency', currency='EUR')

        )
        self.assertEqual(
            'pet eura, nula centi',
            num2words(5.0, lang='hr', to='currency', currency='EUR')

        )
        self.assertEqual(
            'dva eura, jedan cent',
            num2words(2.01, lang='hr', to='currency', currency='EUR')

        )

        self.assertEqual(
            'dva eura, dva centa',
            num2words(2.02, lang='hr', to='currency', currency='EUR')

        )
        self.assertEqual(
            'dva eura, pet centi',
            num2words(2.05, lang='hr', to='currency', currency='EUR')

        )
        self.assertEqual(
            'dvije rublje, nula kopejki',
            num2words(2.0, lang='hr', to='currency', currency='RUB')

        )
        self.assertEqual(
            'dvije rublje, jedna kopejka',
            num2words(2.01, lang='hr', to='currency', currency='RUB')

        )
        self.assertEqual(
            'dvije rublje, dvije kopejke',
            num2words(2.02, lang='hr', to='currency', currency='RUB')

        )
        self.assertEqual(
            'dvije rublje, pet kopejki',
            num2words(2.05, lang='hr', to='currency', currency='RUB')

        )
        self.assertEqual(
            'jedan dinar, nula para',
            num2words(1.0, lang='hr', to='currency', currency='RSD')
        )
        self.assertEqual(
            'dva dinara, dvije pare',
            num2words(2.02, lang='hr', to='currency', currency='RSD')

        )
        self.assertEqual(
            'pet dinara, pet para',
            num2words(5.05, lang='hr', to='currency', currency='RSD')

        )
        self.assertEqual(
            'jedanaest dinara, jedanaest para',
            num2words(11.11, lang='hr', to='currency', currency='RSD')

        )
        self.assertEqual(
            'dvadeset jedan dinar, dvadeset jedna para',
            num2words(21.21, lang='hr', to='currency', currency='RSD')

        )
        self.assertEqual(
            'dvadeset jedan euro, dvadeset jedan cent',
            num2words(21.21, lang='hr', to='currency', currency='EUR')

        )
        self.assertEqual(
            'dvadeset jedna rublja, dvadeset jedna kopejka',
            num2words(21.21, lang='hr', to='currency', currency='RUB')

        )
        self.assertEqual(
            'jedna tisuća dvesta trideset četiri eura, '
            'pedeset šest centi',
            num2words(
                1234.56, lang='hr', to='currency', currency='EUR'
            )
        )
        self.assertEqual(
            'jedna tisuća dvesta trideset četiri rublje, '
            'pedeset šest kopejki',
            num2words(
                1234.56, lang='hr', to='currency', currency='RUB'
            )
        )
        self.assertEqual(
            'sto jedan euro i jedanaest centi',
            num2words(
                10111,
                lang='hr',
                to='currency',
                currency='EUR',
                separator=' i'
            )
        )
        self.assertEqual(
            'sto jedna rublja i dvadeset jedna kopejka',
            num2words(
                10121,
                lang='hr',
                to='currency',
                currency='RUB',
                separator=' i'
            )
        )
        self.assertEqual(
            'sto jedna rublja i dvadeset dvije kopejke',
            num2words(10122, lang='hr', to='currency', currency='RUB',
                      separator=' i')
        )
        self.assertEqual(
            'sto jedan euro i dvadeset jedan cent',
            num2words(10121, lang='hr', to='currency', currency='EUR',
                      separator=' i'),
        )
        self.assertEqual(
            'minus dvanaest tisuća petsto devetnaest eura, 85 centi',
            num2words(
                -1251985,
                lang='hr',
                to='currency',
                currency='EUR',
                cents=False
            )
        )
        self.assertEqual(
            "trideset osam eura i 40 centi",
            num2words('38.4', lang='hr', to='currency', separator=' i',
                      cents=False, currency='EUR'),
        )
