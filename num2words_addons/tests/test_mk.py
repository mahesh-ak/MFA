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


class Num2WordsMKTest(TestCase):

    def test_cardinal(self):
        self.assertEqual("сто", num2words(100, lang='mk'))
        self.assertEqual("сто еден", num2words(101, lang='mk'))
        self.assertEqual("сто десет", num2words(110, lang='mk'))
        self.assertEqual("сто петнаесет", num2words(115, lang='mk'))
        self.assertEqual(
            "сто дваесет три", num2words(123, lang='mk')
        )
        self.assertEqual(
            "еден илјада", num2words(1000, lang='mk')
        )
        self.assertEqual(
            "еден илјада еден", num2words(1001, lang='mk')
        )
        self.assertEqual(
            "два илјади дванаесет", num2words(2012, lang='mk')
        )
        self.assertEqual(
            "дванаесет илјади петстотини деветнаесет запирка осумдесет пет",
            num2words(12519.85, lang='mk')
        )
        self.assertEqual(
            "еден милијарда двесте триесет четири милиони петстотини "
            "шеесет седум илјади осумстотини деведесет",
            num2words(1234567890, lang='mk')
        )
#        self.assertEqual(
#            "двесте петнаесет нонилиони четиристотини шеесет еден "
#            "октилиони четиристотини седум септилиони осумстотини деведесет "
#            "два секстилиони триесет девет квинтилиони два квадрилиони "
#            "сто педесет седум трилиони сто осумдесет девет милијарди "
#            "осумстотини осумдесет три милиони деветстотини една илјада "
#            "шестстотини седумдесет шест",
#            num2words(215461407892039002157189883901676, lang='mk')
#        )
#        self.assertEqual(
#            "седумстотини деветнаесет нонилиони деведесет четири октилиони "
#            "двесте триесет четири септилиони шестстотини деведесет три "
#            "секстилиони шестстотини шеесет три квинтилиони триесет "
#            "четири квадрилиони осумстотини дваесет два трилиони осумстотини "
#            "дваесет четири милијарди триста осумдесет четири милиони "
#            "двесте дваесет илјади двесте деведесет еден",
#            num2words(719094234693663034822824384220291, lang='mk')
#        )
        self.assertEqual("пет", num2words(5, lang='mk'))
        self.assertEqual("петнаесет", num2words(15, lang='mk'))
        self.assertEqual("сто педесет четири", num2words(154, lang='mk'))
        self.assertEqual(
            "еден илјада сто триесет пет",
            num2words(1135, lang='mk')
        )
        self.assertEqual(
            "четиристотини осумнаесет илјади петстотини триесет еден",
            num2words(418531, lang='mk'),
        )
        self.assertEqual(
            "еден милион сто триесет девет",
            num2words(1000139, lang='mk')
        )

    def test_floating_point(self):
        self.assertEqual("пет запирка два", num2words(5.2, lang='mk'))
        self.assertEqual(
            num2words(10.02, lang='mk'),
            "десет запирка нула два"
        )
        self.assertEqual(
            num2words(15.007, lang='mk'),
            "петнаесет запирка нула нула седум"
        )
        self.assertEqual(
            "петстотини шеесет еден запирка четириесет два",
            num2words(561.42, lang='mk')
        )

    def test_to_ordinal(self):
        with self.assertRaises(NotImplementedError):
            num2words(1, lang='mk', to='ordinal')

    def test_to_currency(self):
        self.assertEqual(
            'еден евро, нула центи',
            num2words(1.0, lang='mk', to='currency', currency='EUR')
        )
        self.assertEqual(
            'два евра, нула центи',
            num2words(2.0, lang='mk', to='currency', currency='EUR')
        )
        self.assertEqual(
            'пет евра, нула центи',
            num2words(5.0, lang='mk', to='currency', currency='EUR')
        )
        self.assertEqual(
            'два евра, еден цент',
            num2words(2.01, lang='mk', to='currency', currency='EUR')
        )
        self.assertEqual(
            'два евра, два центи',
            num2words(2.02, lang='mk', to='currency', currency='EUR')
        )
        self.assertEqual(
            'два евра, пет центи',
            num2words(2.05, lang='mk', to='currency', currency='EUR')
        )
        self.assertEqual(
            'еден денар, нула денари',
            num2words(1.0, lang='mk', to='currency', currency='MKD')
        )
        self.assertEqual(
            'два денари, два денари',
            num2words(2.02, lang='mk', to='currency', currency='MKD')
        )
        self.assertEqual(
            'пет денари, пет денари',
            num2words(5.05, lang='mk', to='currency', currency='MKD')
        )
        self.assertEqual(
            'единаесет денари, единаесет денари',
            num2words(11.11, lang='mk', to='currency', currency='MKD')
        )
        self.assertEqual(
            'дваесет еден евра, дваесет еден центи',
            num2words(21.21, lang='mk', to='currency', currency='EUR')
        )
        self.assertEqual(
            'еден илјада двесте триесет четири евра, педесет шест центи',
            num2words(1234.56, lang='mk', to='currency', currency='EUR')
        )
        self.assertEqual(
            'сто еден евра и единаесет центи',
            num2words(
                10111,
                lang='mk',
                to='currency',
                currency='EUR',
                separator=' и'
            )
        )
        self.assertEqual(
            'минус дванаесет илјади петстотини деветнаесет евра, осумдесет пет центи',
            num2words(
                -1251985,
                lang='mk',
                to='currency',
                currency='EUR',
                cents=False
            )
        )
        self.assertEqual(
            "триесет осум евра и четириесет центи",
            num2words(
                '38.4',
                lang='mk',
                to='currency',
                separator=' и',
                cents=False,
                currency='EUR'
            )
        )