# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.
# Copyright (c) 2018, Abdullah Alhazmy, Alhazmy13.  All Rights Reserved.


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

import decimal
import math
import re
from decimal import Decimal
from math import floor

from .base import Num2Word_Base

ARABIC_ONES = [
    "", "wieħed", "tnejn", "tlieta", "erbgħa", "ħamsa", "sitta",
    "sebgħa", "tmienja", "disgħa",
    "għaxra", "ħdax", "tnax", "tlettax", "erbatax", "ħmistax",
    "sittax", "sbatax", "tmintax", "dsatax"
]

EUR = ("ewro", "ewro", "ewro", "ewro")
CENT = ("ċenteżmu", "ċenteżmi", "ċenteżmi", "ċenteżmi")


class Num2Word_MT(Num2Word_Base):
    errmsg_toobig = "abs(%s) must be less than %s."
    MAXVAL = 10**51

    def __init__(self):
        super().__init__()

        self.number = 0
        self.arabicPrefixText = ""
        self.arabicSuffixText = ""
        self.integer_value = 0
        self._decimalValue = ""
        self.partPrecision = 2

        # Currency (Maltese)
        self.currency_unit = EUR
        self.currency_subunit = CENT 
        self.isCurrencyPartNameFeminine = False
        self.isCurrencyNameFeminine = False

        # Maltese connector
        self.separator = 'u'

        # Ones
        self.arabicOnes = ARABIC_ONES

        # Feminine forms (approximation; Maltese mostly not gendered like Arabic)
        self.arabicFeminineOnes = [
            "", "waħda", "tnejn", "tlieta", "erbgħa", "ħamsa", "sitta",
            "sebgħa", "tmienja", "disgħa",
            "għaxra", "ħdax", "tnax", "tlettax", "erbatax", "ħmistax",
            "sittax", "sbatax", "tmintax", "dsatax"
        ]

        # Ordinals
        self.arabicOrdinal = [
            "", "ewwel", "it-tieni", "it-tielet", "ir-raba’", "il-ħames",
            "is-sitt", "is-seba’", "it-tmien", "id-disa’",
            "l-għaxar", "il-ħdax", "it-tnax", "it-tlettax", "l-erbatax",
            "il-ħmistax", "is-sittax", "is-sbatax", "it-tmintax", "id-dsatax"
        ]

        # Tens
        self.arabicTens = [
            "għoxrin", "tletin", "erbgħin", "ħamsin",
            "sittin", "sebgħin", "tmenin", "disgħin"
        ]

        # Hundreds
        self.arabicHundreds = [
            "", "mija", "mitejn", "tliet mitt", "erba’ mitt",
            "ħames mitt", "sitt mitt", "seba’ mitt",
            "tmien mitt", "disgħa mitt"
        ]

        # Dual forms (simplified for Maltese)
        self.arabicAppendedTwos = [
            "mitejn", "elfejn", "miljuni", "biljuni", "triljuni",
            "kwadriljuni", "kwintiljuni", "sestiljuni", "settiljuni",
            "oktiljuni", "noniljuni", "deċiljuni"
        ]

        self.arabicTwos = [
            "mitejn", "elfejn", "miljuni", "biljuni", "triljuni",
            "kwadriljuni", "kwintiljuni", "sestiljuni", "settiljuni",
            "oktiljuni", "noniljuni", "deċiljuni"
        ]

        # Groups (scales)
        self.arabicGroup = [
            "mija", "elf", "miljun", "biljun", "triljun",
            "kwadriljun", "kwintiljun", "sestiljun",
            "settiljun", "oktiljun", "noniljun", "deċiljun"
        ]

        # Accusative-like (not really needed in Maltese, kept for compatibility)
        self.arabicAppendedGroup = [
            "", "elf", "miljun", "biljun", "triljun",
            "kwadriljun", "kwintiljun", "sestiljun",
            "settiljun", "oktiljun", "noniljun", "deċiljun"
        ]

        # Plurals
        self.arabicPluralGroups = [
            "", "eluf", "miljuni", "biljuni", "triljuni",
            "kwadriljuni", "kwintiljuni", "sestiljuni",
            "settiljuni", "oktiljuni", "noniljuni", "deċiljuni"
        ]

        assert len(self.arabicAppendedGroup) == len(self.arabicGroup)
        assert len(self.arabicPluralGroups) == len(self.arabicGroup)
        assert len(self.arabicAppendedTwos) == len(self.arabicTwos)

    def number_to_arabic(self, arabic_prefix_text, arabic_suffix_text):
        self.arabicPrefixText = arabic_prefix_text
        self.arabicSuffixText = arabic_suffix_text
        self.extract_integer_and_decimal_parts()

    def extract_integer_and_decimal_parts(self):
        splits = re.split('\\.', str(self.number))

        self.integer_value = int(splits[0])
        if len(splits) > 1:
            self._decimalValue = int(self.decimal_value(splits[1]))
        else:
            self._decimalValue = 0

    def decimal_value(self, decimal_part):

        if self.partPrecision is not len(decimal_part):
            decimal_part_length = len(decimal_part)

            decimal_part_builder = decimal_part
            for i in range(0, self.partPrecision - decimal_part_length):
                decimal_part_builder += '0'
            decimal_part = decimal_part_builder

            if len(decimal_part) <= self.partPrecision:
                dec = len(decimal_part)
            else:
                dec = self.partPrecision
            result = decimal_part[0: dec]
        else:
            result = decimal_part

        # The following is useless (never happens)
        # for i in range(len(result), self.partPrecision):
        #     result += '0'
        return result

    def digit_feminine_status(self, digit, group_level):
        if group_level == -1:
            if self.isCurrencyPartNameFeminine:
                return self.arabicFeminineOnes[int(digit)]
            else:
                # Note: this never happens
                return self.arabicOnes[int(digit)]
        elif group_level == 0:
            if self.isCurrencyNameFeminine:
                return self.arabicFeminineOnes[int(digit)]
            else:
                return self.arabicOnes[int(digit)]
        else:
            return self.arabicOnes[int(digit)]

    def process_arabic_group(self, group_number, group_level,
                             remaining_number):
        tens = Decimal(group_number) % Decimal(100)
        hundreds = Decimal(group_number) / Decimal(100)
        ret_val = ""

        if int(hundreds) > 0:
            if tens == 0 and int(hundreds) == 2:
                ret_val = "{}".format(self.arabicAppendedTwos[0])
            else:
                ret_val = "{}".format(self.arabicHundreds[int(hundreds)])
                if ret_val != "" and tens != 0:
                    ret_val += " u "

        if tens > 0:
            if tens < 20:
                # if int(group_level) >= len(self.arabicTwos):
                #     raise OverflowError(self.errmsg_toobig %
                #                         (self.number, self.MAXVAL))
                assert int(group_level) < len(self.arabicTwos)
                if tens == 2 and int(hundreds) == 0 and group_level > 0:
                    pow = int(math.log10(self.integer_value))
                    if self.integer_value > 10 and pow % 3 == 0 and \
                            self.integer_value == 2 * (10 ** pow):
                        ret_val = "{}".format(
                            self.arabicAppendedTwos[int(group_level)])
                    else:
                        ret_val = "{}".format(
                            self.arabicTwos[int(group_level)])
                else:

                    if tens == 1 and group_level > 0 and hundreds == 0:
                        # Note: this never happens
                        # (hundreds == 0 only if group_number is 0)
                        ret_val += ""
                    elif (tens == 1 or tens == 2) and (
                            group_level == 0 or group_level == -1) and \
                            hundreds == 0 and remaining_number == 0:
                        # Note: this never happens (idem)
                        ret_val += ""
                    elif tens == 1 and group_level > 0:
                        ret_val += self.arabicGroup[int(group_level)]
                    else:
                        ret_val += self.digit_feminine_status(int(tens),
                                                              group_level)
            else:
                ones = tens % 10
                tens = (tens / 10) - 2
                if ones > 0:
                    ret_val += self.digit_feminine_status(ones, group_level)
                if ret_val != "" and ones != 0:
                    ret_val += " u "

                ret_val += self.arabicTens[int(tens)]

        return ret_val

    # We use this instead of built-in `abs` function,
    # because `abs` suffers from loss of precision for big numbers
    def abs(self, number):
        return number if number >= 0 else -number

    # We use this instead of `"{:09d}".format(number)`,
    # because the string conversion suffers from loss of
    # precision for big numbers
    def to_str(self, number):
        integer = int(number)
        if integer == number:
            return str(integer)
        decimal = round((number - integer) * 10**9)
        return str(integer) + "." + "{:09d}".format(decimal).rstrip("0")

    def convert(self, value):
        self.number = self.to_str(value)
        self.number_to_arabic(self.arabicPrefixText, self.arabicSuffixText)
        return self.convert_to_arabic()

    def convert_to_arabic(self):
        temp_number = Decimal(self.number)

        if temp_number == Decimal(0):
            return "żero" 

        decimal_string = self.process_arabic_group(self._decimalValue,
                                                   -1,
                                                   Decimal(0))
        ret_val = ""
        group = 0

        while temp_number > Decimal(0):

            temp_number_dec = Decimal(str(temp_number))
            try:
                number_to_process = int(temp_number_dec % Decimal(str(1000)))
            except decimal.InvalidOperation:
                decimal.getcontext().prec = len(
                    temp_number_dec.as_tuple().digits
                )
                number_to_process = int(temp_number_dec % Decimal(str(1000)))

            temp_number = int(temp_number_dec / Decimal(1000))

            group_description = \
                self.process_arabic_group(number_to_process,
                                          group,
                                          Decimal(floor(temp_number)))
            if group_description != '':
                if group_description.endswith(self.arabicGroup[group]):
                    skip_group_label = True
                    if ret_val != "":
                        ret_val = "{}u {}".format("", ret_val)
                else:
                    skip_group_label = False
                if group > 0 and not skip_group_label:
                    if ret_val != "":
                        ret_val = "{}u {}".format("", ret_val)
                    if number_to_process != 2 and number_to_process != 1:
                        # if group >= len(self.arabicGroup):
                        #     raise OverflowError(self.errmsg_toobig %
                        #                         (self.number, self.MAXVAL)
                        #     )
                        assert group < len(self.arabicGroup)
                        if number_to_process % 100 != 1:
                            if 3 <= number_to_process <= 10:
                                ret_val = "{} {}".format(
                                    self.arabicPluralGroups[group], ret_val)
                            else:
                                if ret_val != "":
                                    ret_val = "{} {}".format(
                                        self.arabicAppendedGroup[group],
                                        ret_val)
                                else:
                                    ret_val = "{} {}".format(
                                        self.arabicGroup[group], ret_val)

                        else:
                            ret_val = "{} {}".format(self.arabicGroup[group],
                                                     ret_val)
                ret_val = "{} {}".format(group_description, ret_val)
            group += 1
        formatted_number = ""
        if self.arabicPrefixText != "":
            formatted_number += "{} ".format(self.arabicPrefixText)
        formatted_number += ret_val
        if self.integer_value != 0:
            remaining100 = int(self.integer_value % 100)

            if remaining100 == 0:
                formatted_number += self.currency_unit[0]
            elif remaining100 == 1:
                formatted_number += self.currency_unit[0]
            elif remaining100 == 2:
                if self.integer_value == 2:
                    formatted_number += self.currency_unit[1]
                else:
                    formatted_number += self.currency_unit[0]
            elif 3 <= remaining100 <= 10:
                formatted_number += self.currency_unit[2]
            elif 11 <= remaining100 <= 99:
                formatted_number += self.currency_unit[3]
        if self._decimalValue != 0:
            formatted_number += " {} ".format(self.separator)
            formatted_number += decimal_string

        if self._decimalValue != 0:
            formatted_number += " "
            remaining100 = int(self._decimalValue % 100)

            if remaining100 == 0:
                formatted_number += self.currency_subunit[0]
            elif remaining100 == 1:
                formatted_number += self.currency_subunit[0]
            elif remaining100 == 2:
                formatted_number += self.currency_subunit[1]
            elif 3 <= remaining100 <= 10:
                formatted_number += self.currency_subunit[2]
            elif 11 <= remaining100 <= 99:
                formatted_number += self.currency_subunit[3]

        if self.arabicSuffixText != "":
            formatted_number += " {}".format(self.arabicSuffixText)

        return formatted_number

    def validate_number(self, number):
        if number >= self.MAXVAL:
            raise OverflowError(self.errmsg_toobig % (number, self.MAXVAL))
        return number

    def set_currency_prefer(self, currency):
        if currency == 'EUR':
            self.currency_unit = EUR
            self.currency_subunit = CENT
            self.partPrecision = 3


    def to_currency(self, value, currency='EUR', prefix='', suffix=''):
        self.set_currency_prefer(currency)
        self.isCurrencyNameFeminine = False
        self.separator = "u"
        self.arabicOnes = ARABIC_ONES
        self.arabicPrefixText = prefix
        self.arabicSuffixText = suffix
        return self.convert(value=value)

    def to_ordinal(self, number, prefix=''):
        if number <= 19:
            return "{}".format(self.arabicOrdinal[number])
        if number < 100:
            self.isCurrencyNameFeminine = True
        else:
            self.isCurrencyNameFeminine = False
        self.currency_subunit = ('', '', '', '')
        self.currency_unit = ('', '', '', '')
        self.arabicPrefixText = prefix
        self.arabicSuffixText = ""
        result = self.convert(self.abs(number)).strip()
        if number >= 20 and ' ' not in result:
            result = 'l-' + result
        return result

    def to_year(self, value):
        value = self.validate_number(value)
        return self.to_cardinal(value)

    def to_ordinal_num(self, value):
        return self.to_ordinal(value).strip()

    def to_cardinal(self, number):
        self.isCurrencyNameFeminine = False
        number = self.validate_number(number)
        minus = ''
        if number < 0:
            minus = 'minus '
        self.separator = 'virgola'
        self.currency_subunit = ('', '', '', '')
        self.currency_unit = ('', '', '', '')
        self.arabicPrefixText = ""
        self.arabicSuffixText = ""
        self.arabicOnes = ARABIC_ONES
        return minus + self.convert(value=self.abs(number)).strip()
