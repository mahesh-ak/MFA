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

from decimal import Decimal
from unittest import TestCase

from num2words import num2words
from num2words.lang_GL import Num2Word_GL


class Num2WordsGLTest(TestCase):
    def setUp(self):
        super(Num2WordsGLTest, self).setUp()
        self.n2w = Num2Word_GL()

    def test_cardinal_integer(self):
        self.assertEqual(num2words(1, lang='gl'), 'un')
        self.assertEqual(num2words(2, lang='gl'), 'dous')
        self.assertEqual(num2words(3, lang='gl'), 'três')
        self.assertEqual(num2words(4, lang='gl'), 'quatro')
        self.assertEqual(num2words(5, lang='gl'), 'cinco')
        self.assertEqual(num2words(6, lang='gl'), 'seis')
        self.assertEqual(num2words(7, lang='gl'), 'sete')
        self.assertEqual(num2words(8, lang='gl'), 'oito')
        self.assertEqual(num2words(9, lang='gl'), 'nove')
        self.assertEqual(num2words(10, lang='gl'), 'dez')
        self.assertEqual(num2words(11, lang='gl'), 'onze')
        self.assertEqual(num2words(12, lang='gl'), 'doze')
        self.assertEqual(num2words(13, lang='gl'), 'treze')
        self.assertEqual(num2words(14, lang='gl'), 'catorce')
        self.assertEqual(num2words(15, lang='gl'), 'quinze')
        self.assertEqual(num2words(16, lang='gl'), 'dezaseis')
        self.assertEqual(num2words(17, lang='gl'), 'dezasete')
        self.assertEqual(num2words(18, lang='gl'), 'dezoito')
        self.assertEqual(num2words(19, lang='gl'), 'dezanove')
        self.assertEqual(num2words(20, lang='gl'), 'vinte')

        self.assertEqual(num2words(21, lang='gl'), 'vinte e un')
        self.assertEqual(num2words(22, lang='gl'), 'vinte e dous')
        self.assertEqual(num2words(35, lang='gl'), 'trinta e cinco')
        self.assertEqual(num2words(99, lang='gl'), 'noventa e nove')

        self.assertEqual(num2words(100, lang='gl'), 'cem')
        self.assertEqual(num2words(101, lang='gl'), 'cento e un')
        self.assertEqual(num2words(128, lang='gl'), 'cento e vinte e oito')
        self.assertEqual(num2words(713, lang='gl'), 'setecentos e treze')

        self.assertEqual(num2words(1000, lang='gl'), 'mil')
        self.assertEqual(num2words(1001, lang='gl'), 'mil e un')
        self.assertEqual(num2words(1111, lang='gl'), 'mil cento e onze')
        self.assertEqual(
            num2words(2114, lang='gl'), 'dous mil cento e catorce'
        )
        self.assertEqual(
            num2words(2200, lang='gl'),
            'dous mil e douscentos'
        )
        self.assertEqual(
            num2words(2230, lang='gl'),
            'dous mil douscentos e trinta'
        )
        self.assertEqual(
            num2words(73400, lang='gl'),
            'setenta e três mil e catrocentos'
        )
        self.assertEqual(
            num2words(73421, lang='gl'),
            'setenta e três mil catrocentos e vinte e un'
        )
        self.assertEqual(num2words(100000, lang='gl'), 'cem mil')
        self.assertEqual(
            num2words(250050, lang='gl'),
            'douscentos e cinquenta mil e cinquenta'
        )
        self.assertEqual(
            num2words(6000000, lang='gl'), 'seis millóns'
        )
        self.assertEqual(
            num2words(100000000, lang='gl'), 'cem millóns'
        )
        self.assertEqual(
            num2words(19000000000, lang='gl'), 'dezanove mil millóns'
        )
        self.assertEqual(
            num2words(145000000002, lang='gl'),
            'cento e quarenta e cinco mil millóns e dous'
        )
        self.assertEqual(
            num2words(4635102, lang='gl'),
            'quatro millóns seiscentos e trinta e cinco mil cento e dous'
        )
        self.assertEqual(
            num2words(145254635102, lang='gl'),
            'cento e quarenta e cinco mil douscentos e cinquenta e quatro '
            'millóns seiscentos e trinta e cinco mil cento e dous'
        )
        self.assertEqual(
            num2words(1000000000000, lang='gl'),
            'un billón'
        )
        self.assertEqual(
            num2words(2000000000000, lang='gl'),
            'dous billóns'
        )
        self.assertEqual(
            num2words(1000000000000000, lang='gl'),
            'mil billóns'
        )
        self.assertEqual(
            num2words(2000000000000000, lang='gl'),
            'dous mil billóns'
        )
        self.assertEqual(
            num2words(1000000000000000000, lang='gl'),
            'un trillón'
        )
        self.assertEqual(
            num2words(2000000000000000000, lang='gl'),
            'dous trillóns'
        )

    def test_cardinal_integer_negative(self):
        self.assertEqual(num2words(-1, lang='gl'), 'menos un')
        self.assertEqual(
            num2words(-256, lang='gl'), 'menos douscentos e cinquenta e seis'
        )
        self.assertEqual(num2words(-1000, lang='gl'), 'menos mil')
        self.assertEqual(num2words(-1000000, lang='gl'), 'menos un millón')
        self.assertEqual(
            num2words(-1234567, lang='gl'),
            'menos un millón douscentos e trinta e quatro mil quinhentos e '
            'sessenta e sete'
        )

    def test_cardinal_float(self):
        self.assertEqual(num2words(Decimal('1.00'), lang='gl'), 'un')
        self.assertEqual(num2words(
            Decimal('1.01'), lang='gl'), 'un coma zero un')
        self.assertEqual(num2words(
            Decimal('1.035'), lang='gl'), 'un coma zero três cinco'
        )
        self.assertEqual(num2words(
            Decimal('1.35'), lang='gl'), 'un coma três cinco'
        )
        self.assertEqual(
            num2words(Decimal('3.14159'), lang='gl'),
            'três coma un quatro un cinco nove'
        )
        self.assertEqual(
            num2words(Decimal('101.22'), lang='gl'),
            'cento e un coma dous dous'
        )
        self.assertEqual(
            num2words(Decimal('2345.75'), lang='gl'),
            'dous mil trescentos e quarenta e cinco coma sete cinco')

    def test_cardinal_float_negative(self):
        self.assertEqual(
            num2words(Decimal('-2.34'), lang='gl'),
            'menos dous coma três quatro'
        )
        self.assertEqual(
            num2words(Decimal('-9.99'), lang='gl'),
            'menos nove coma nove nove'
        )
        self.assertEqual(
            num2words(Decimal('-7.01'), lang='gl'),
            'menos sete coma zero un'
        )
        self.assertEqual(
            num2words(Decimal('-222.22'), lang='gl'),
            'menos douscentos e vinte e dous coma dous dous'
        )

    def test_ordinal(self):
        self.assertEqual(num2words(1, lang='gl', ordinal=True), 'primeiro')
        self.assertEqual(num2words(2, lang='gl', ordinal=True), 'segundo')
        self.assertEqual(num2words(3, lang='gl', ordinal=True), 'terceiro')
        self.assertEqual(num2words(4, lang='gl', ordinal=True), 'cuarto')
        self.assertEqual(num2words(5, lang='gl', ordinal=True), 'quinto')
        self.assertEqual(num2words(6, lang='gl', ordinal=True), 'sexto')
        self.assertEqual(num2words(7, lang='gl', ordinal=True), 'sétimo')
        self.assertEqual(num2words(8, lang='gl', ordinal=True), 'oitavo')
        self.assertEqual(num2words(9, lang='gl', ordinal=True), 'noveno')
        self.assertEqual(num2words(10, lang='gl', ordinal=True), 'décimo')
        self.assertEqual(
            num2words(11, lang='gl', ordinal=True), 'décimo primeiro'
        )
        self.assertEqual(
            num2words(12, lang='gl', ordinal=True), 'décimo segundo'
        )
        self.assertEqual(
            num2words(13, lang='gl', ordinal=True), 'décimo terceiro'
        )
        self.assertEqual(
            num2words(14, lang='gl', ordinal=True), 'décimo cuarto'
        )
        self.assertEqual(
            num2words(15, lang='gl', ordinal=True), 'décimo quinto'
        )
        self.assertEqual(
            num2words(16, lang='gl', ordinal=True), 'décimo sexto'
        )
        self.assertEqual(
            num2words(17, lang='gl', ordinal=True), 'décimo sétimo'
        )
        self.assertEqual(
            num2words(18, lang='gl', ordinal=True), 'décimo oitavo'
        )
        self.assertEqual(
            num2words(19, lang='gl', ordinal=True), 'décimo noveno'
        )
        self.assertEqual(
            num2words(20, lang='gl', ordinal=True), 'vixésimo'
        )

        self.assertEqual(
            num2words(21, lang='gl', ordinal=True), 'vixésimo primeiro'
        )
        self.assertEqual(
            num2words(22, lang='gl', ordinal=True), 'vixésimo segundo'
        )
        self.assertEqual(
            num2words(35, lang='gl', ordinal=True), 'trixésimo quinto'
        )
        self.assertEqual(
            num2words(99, lang='gl', ordinal=True), 'nonaxésimo noveno'
        )

        self.assertEqual(
            num2words(100, lang='gl', ordinal=True), 'centésimo'
        )
        self.assertEqual(
            num2words(101, lang='gl', ordinal=True), 'centésimo primeiro'
        )
        self.assertEqual(
            num2words(128, lang='gl', ordinal=True),
            'centésimo vixésimo oitavo'
        )
        self.assertEqual(
            num2words(713, lang='gl', ordinal=True),
            'setecentésimo décimo terceiro'
        )

        self.assertEqual(
            num2words(1000, lang='gl', ordinal=True), 'milésimo'
        )
        self.assertEqual(
            num2words(1001, lang='gl', ordinal=True), 'milésimo primeiro'
        )
        self.assertEqual(
            num2words(1111, lang='gl', ordinal=True),
            'milésimo centésimo décimo primeiro'
        )
        self.assertEqual(
            num2words(2114, lang='gl', ordinal=True),
            'segundo milésimo centésimo décimo cuarto'
        )
        self.assertEqual(
            num2words(73421, lang='gl', ordinal=True),
            'septuaxésimo terceiro milésimo catrocentésimo vixésimo primeiro'
        )

        self.assertEqual(
            num2words(100000, lang='gl', ordinal=True),
            'centésimo milésimo'
        )
        self.assertEqual(
            num2words(250050, lang='gl', ordinal=True),
            'douscentésimo quincuaxésimo milésimo quincuaxésimo'
        )
        self.assertEqual(
            num2words(6000000, lang='gl', ordinal=True), 'sexto milionésimo'
        )
        self.assertEqual(
            num2words(19000000000, lang='gl', ordinal=True),
            'décimo noveno milésimo milionésimo'
        )
        self.assertEqual(
            num2words(145000000002, lang='gl', ordinal=True),
            'centésimo quadraxésimo quinto milésimo milionésimo segundo'
        )

    def test_currency_integer(self):
        self.assertEqual(self.n2w.to_currency(1.00), 'un euro')
        self.assertEqual(self.n2w.to_currency(2.00), 'dous euros')
        self.assertEqual(self.n2w.to_currency(3.00), 'três euros')
        self.assertEqual(self.n2w.to_currency(4.00), 'quatro euros')
        self.assertEqual(self.n2w.to_currency(5.00), 'cinco euros')
        self.assertEqual(self.n2w.to_currency(6.00), 'seis euros')
        self.assertEqual(self.n2w.to_currency(7.00), 'sete euros')
        self.assertEqual(self.n2w.to_currency(8.00), 'oito euros')
        self.assertEqual(self.n2w.to_currency(9.00), 'nove euros')
        self.assertEqual(self.n2w.to_currency(10.00), 'dez euros')
        self.assertEqual(self.n2w.to_currency(11.00), 'onze euros')
        self.assertEqual(self.n2w.to_currency(12.00), 'doze euros')
        self.assertEqual(self.n2w.to_currency(13.00), 'treze euros')
        self.assertEqual(self.n2w.to_currency(14.00), 'catorce euros')
        self.assertEqual(self.n2w.to_currency(15.00), 'quinze euros')
        self.assertEqual(self.n2w.to_currency(16.00), 'dezaseis euros')
        self.assertEqual(self.n2w.to_currency(17.00), 'dezasete euros')
        self.assertEqual(self.n2w.to_currency(18.00), 'dezoito euros')
        self.assertEqual(self.n2w.to_currency(19.00), 'dezanove euros')
        self.assertEqual(self.n2w.to_currency(20.00), 'vinte euros')

        self.assertEqual(self.n2w.to_currency(21.00), 'vinte e un euros')
        self.assertEqual(self.n2w.to_currency(22.00), 'vinte e dous euros')
        self.assertEqual(self.n2w.to_currency(35.00), 'trinta e cinco euros')
        self.assertEqual(self.n2w.to_currency(99.00), 'noventa e nove euros')

        self.assertEqual(self.n2w.to_currency(100.00), 'cem euros')
        self.assertEqual(self.n2w.to_currency(101.00), 'cento e un euros')
        self.assertEqual(
            self.n2w.to_currency(128.00), 'cento e vinte e oito euros'
        )
        self.assertEqual(
            self.n2w.to_currency(713.00), 'setecentos e treze euros')

        self.assertEqual(self.n2w.to_currency(1000.00), 'mil euros')
        self.assertEqual(self.n2w.to_currency(1001.00), 'mil e un euros')
        self.assertEqual(
            self.n2w.to_currency(1111.00), 'mil cento e onze euros')
        self.assertEqual(
            self.n2w.to_currency(2114.00), 'dous mil cento e catorce euros'
        )
        self.assertEqual(
            self.n2w.to_currency(73421.00),
            'setenta e três mil catrocentos e vinte e un euros'
        )

        self.assertEqual(self.n2w.to_currency(100000.00), 'cem mil euros')
        self.assertEqual(
            self.n2w.to_currency(250050.00),
            'douscentos e cinquenta mil e cinquenta euros'
        )
        self.assertEqual(
            self.n2w.to_currency(6000000.00), 'seis millóns de euros'
        )
        self.assertEqual(
            self.n2w.to_currency(19000000000.00),
            'dezanove mil millóns de euros'
        )
        self.assertEqual(
            self.n2w.to_currency(145000000002.00),
            'cento e quarenta e cinco mil millóns e dous euros'
        )
        self.assertEqual(self.n2w.to_currency(1.00, currency='USD'),
                         'un dólar')
        self.assertEqual(self.n2w.to_currency(1.50, currency='USD'),
                         'un dólar e cinquenta cêntimos')
        with self.assertRaises(NotImplementedError):
            self.n2w.to_currency(1.00, currency='CHF')

    def test_currency_integer_negative(self):
        self.assertEqual(self.n2w.to_currency(-1.00), 'menos un euro')
        self.assertEqual(
            self.n2w.to_currency(-256.00),
            'menos douscentos e cinquenta e seis euros'
        )
        self.assertEqual(self.n2w.to_currency(-1000.00), 'menos mil euros')
        self.assertEqual(
            self.n2w.to_currency(-1000000.00), 'menos un millón de euros'
        )
        self.assertEqual(
            self.n2w.to_currency(-1234567.00),
            'menos un millón douscentos e trinta e quatro mil quinhentos e '
            'sessenta e sete euros'
        )

    def test_currency_float(self):
        self.assertEqual(self.n2w.to_currency(Decimal('1.00')), 'un euro')
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.01')), 'un euro e un cêntimo'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.03')), 'un euro e três cêntimos'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.35')),
            'un euro e trinta e cinco cêntimos'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('3.14')),
            'três euros e catorce cêntimos'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('101.22')),
            'cento e un euros e vinte e dous cêntimos'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('2345.75')),
            'dous mil trescentos e quarenta e cinco euros e setenta e cinco '
            'cêntimos'
        )

    def test_currency_float_negative(self):
        self.assertEqual(
            self.n2w.to_currency(Decimal('-2.34')),
            'menos dous euros e trinta e quatro cêntimos'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-9.99')),
            'menos nove euros e noventa e nove cêntimos'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-7.01')),
            'menos sete euros e un cêntimo'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-222.22')),
            'menos douscentos e vinte e dous euros e vinte e dous cêntimos'
        )

    def test_year(self):
        self.assertEqual(self.n2w.to_year(1001), 'mil e un')
        self.assertEqual(
            self.n2w.to_year(1789), 'mil setecentos e oitenta e nove'
        )
        self.assertEqual(
            self.n2w.to_year(1942), 'mil novecentos e quarenta e dous'
        )
        self.assertEqual(
            self.n2w.to_year(1984), 'mil novecentos e oitenta e quatro'
        )
        self.assertEqual(self.n2w.to_year(2000), 'dous mil')
        self.assertEqual(self.n2w.to_year(2001), 'dous mil e un')
        self.assertEqual(self.n2w.to_year(2016), 'dous mil e dezaseis')

    def test_year_negative(self):
        self.assertEqual(self.n2w.to_year(-30), 'trinta antes de Cristo')
        self.assertEqual(
            self.n2w.to_year(-744),
            'setecentos e quarenta e quatro antes de Cristo'
        )
        self.assertEqual(self.n2w.to_year(-10000), 'dez mil antes de Cristo')

    def test_to_ordinal_num(self):
        self.assertEqual(self.n2w.to_ordinal_num(1), '1º')
        self.assertEqual(self.n2w.to_ordinal_num(100), '100º')