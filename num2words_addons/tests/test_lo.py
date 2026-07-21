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
from num2words.lang_LO import Num2Word_LO


class TestNumWord(TestCase):

    def test_0(self):
        self.assertEqual(num2words(0, lang='lo'), "ສູນ")

    def test_end_with_1(self):
        self.assertEqual(num2words(21, lang='lo'), "ຊາວເອັດ")
        self.assertEqual(num2words(11, lang='lo'), "ສິບເອັດ")
        self.assertEqual(num2words(101, lang='lo'), "ໜຶ່ງຮ້ອຍເອັດ")
        self.assertEqual(num2words(1201, lang='lo'), "ໜຶ່ງພັນສອງຮ້ອຍເອັດ")

    def test_start_20(self):
        self.assertEqual(num2words(22, lang='lo'), "ຊາວສອງ")
        self.assertEqual(num2words(27, lang='lo'), "ຊາວເຈັດ")

    def test_start_10(self):
        self.assertEqual(num2words(10, lang='lo'), "ສິບ")
        self.assertEqual(num2words(18, lang='lo'), "ສິບແປດ")

    def test_1_to_9(self):
        self.assertEqual(num2words(1, lang='lo'), "ໜຶ່ງ")
        self.assertEqual(num2words(5, lang='lo'), "ຫ້າ")
        self.assertEqual(num2words(9, lang='lo'), "ເກົ້າ")

    def test_31_to_99(self):
        self.assertEqual(num2words(31, lang='lo'), "ສາມສິບເອັດ")
        self.assertEqual(num2words(48, lang='lo'), "ສີ່ສິບແປດ")
        self.assertEqual(num2words(76, lang='lo'), "ເຈັດສິບຫົກ")

    def test_100_to_999(self):
        self.assertEqual(num2words(100, lang='lo'), "ໜຶ່ງຮ້ອຍ")
        self.assertEqual(num2words(123, lang='lo'), "ໜຶ່ງຮ້ອຍຊາວສາມ")
        self.assertEqual(num2words(456, lang='lo'), "ສີ່ຮ້ອຍຫ້າສິບຫົກ")
        self.assertEqual(num2words(721, lang='lo'), "ເຈັດຮ້ອຍຊາວເອັດ")

    def test_1000_to_9999(self):
        self.assertEqual(num2words(1000, lang='lo'), "ໜຶ່ງພັນ")
        self.assertEqual(
            num2words(2175, lang='lo'),
            "ສອງພັນໜຶ່ງຮ້ອຍເຈັດສິບຫ້າ"
        )
        self.assertEqual(num2words(4582, lang='lo'), "ສີ່ພັນຫ້າຮ້ອຍແປດສິບສອງ")
        self.assertEqual(num2words(9346, lang='lo'), "ເກົ້າພັນສາມຮ້ອຍສີ່ສິບຫົກ")

    def test_10000_to_99999(self):
        self.assertEqual(
            num2words(11111, lang='lo'),
            "ໜຶ່ງໝື່ນໜຶ່ງພັນໜຶ່ງຮ້ອຍສິບເອັດ"
        )
        self.assertEqual(
            num2words(22222, lang='lo'),
            "ສອງໝື່ນສອງພັນສອງຮ້ອຍຊາວສອງ"
        )
        self.assertEqual(
            num2words(84573, lang='lo'),
            "ແປດໝື່ນສີ່ພັນຫ້າຮ້ອຍເຈັດສິບສາມ"
        )

    def test_100000_to_999999(self):
        self.assertEqual(
            num2words(153247, lang='lo'),
            "ໜຶ່ງແສນຫ້າໝື່ນສາມພັນສອງຮ້ອຍສີ່ສິບເຈັດ"
        )
        self.assertEqual(
            num2words(562442, lang='lo'),
            "ຫ້າແສນຫົກໝື່ນສອງພັນສີ່ຮ້ອຍສີ່ສິບສອງ"
        )
        self.assertEqual(
            num2words(999999, lang='lo'),
            "ເກົ້າແສນເກົ້າໝື່ນເກົ້າພັນເກົ້າຮ້ອຍເກົ້າສິບເກົ້າ"
        )

    def test_more_than_million(self):
        self.assertEqual(num2words(1000000, lang='lo'), "ໜຶ່ງລ້ານ")
        self.assertEqual(num2words(1000001, lang='lo'), "ໜຶ່ງລ້ານເອັດ")
        self.assertEqual(
            num2words(42478941, lang='lo'),
            "ສີ່ສິບສອງລ້ານສີ່ແສນເຈັດໝື່ນແປດພັນເກົ້າຮ້ອຍສີ່ສິບເອັດ"
        )
        self.assertEqual(
            num2words(712696969, lang='lo'),
            "ເຈັດຮ້ອຍສິບສອງລ້ານຫົກແສນເກົ້າໝື່ນຫົກພັນເກົ້າຮ້ອຍຫົກສິບເກົ້າ"
        )
        self.assertEqual(
            num2words(1000000000000000001, lang='lo'),
            "ໜຶ່ງລ້ານລ້ານລ້ານເອັດ"
        )

    def test_decimal(self):
        self.assertEqual(num2words(0.0, lang='lo'), "ສູນ")
        self.assertEqual(num2words(0.0038, lang='lo'), "ສູນຈຸດສູນສູນສາມແປດ")
        self.assertEqual(num2words(0.01, lang='lo'), "ສູນຈຸດສູນໜຶ່ງ")
        self.assertEqual(num2words(1.123, lang='lo'), "ໜຶ່ງຈຸດໜຶ່ງສອງສາມ")
        self.assertEqual(num2words(35.37, lang='lo'), "ສາມສິບຫ້າຈຸດສາມເຈັດ")
        self.assertEqual(num2words(1000000.01, lang='lo'), "ໜຶ່ງລ້ານຈຸດສູນໜຶ່ງ")

    def test_negative(self):
        self.assertEqual(num2words(-10, lang='lo'), "ລົບສິບ")
        self.assertEqual(num2words(-10.50, lang='lo'), "ລົບສິບຈຸດຫ້າ")