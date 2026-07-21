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

from unittest import TestCase

from num2words import num2words


# number, urdu number, pronounced form
TEST_CASES_CARDINAL = (
    (0, u"۰", u"صفر"),
    (1, u"۱", u"ایک"),
    (2, u"۲", u"دو"),
    (3, u"۳", u"تین"),
    (4, u"۴", u"چار"),
    (5, u"۵", u"پانچ"),
    (6, u"۶", u"چھ"),
    (7, u"۷", u"سات"),
    (8, u"۸", u"آٹھ"),
    (9, u"۹", u"نو"),
    (10, u"۱۰", u"دس"),
    (11, u"۱۱", u"گیارہ"),
    (12, u"۱۲", u"بارہ"),
    (13, u"۱۳", u"تیرہ"),
    (14, u"۱۴", u"چودہ"),
    (15, u"۱۵", u"پندرہ"),
    (16, u"۱۶", u"سولہ"),
    (17, u"۱۷", u"سترہ"),
    (18, u"۱۸", u"اٹھارہ"),
    (19, u"۱۹", u"انیس"),
    (20, u"۲۰", u"بیس"),
    (21, u"۲۱", u"اکیس"),
    (22, u"۲۲", u"بائیس"),
    (23, u"۲۳", u"تیئیس"),
    (24, u"۲۴", u"چوبیس"),
    (25, u"۲۵", u"پچیس"),
    (26, u"۲۶", u"چھبیس"),
    (27, u"۲۷", u"ستائیس"),
    (28, u"۲۸", u"اٹھائیس"),
    (29, u"۲۹", u"انتیس"),
    (30, u"۳۰", u"تیس"),
    (31, u"۳۱", u"اکتیس"),
    (32, u"۳۲", u"بتیس"),
    (33, u"۳۳", u"تینتیس"),
    (34, u"۳۴", u"چونتیس"),
    (35, u"۳۵", u"پینتیس"),
    (36, u"۳۶", u"چھتیس"),
    (37, u"۳۷", u"سینتیس"),
    (38, u"۳۸", u"اڑتیس"),
    (39, u"۳۹", u"انتالیس"),
    (40, u"۴۰", u"چالیس"),
    (41, u"۴۱", u"اکتالیس"),
    (42, u"۴۲", u"بیالیس"),
    (43, u"۴۳", u"تینتالیس"),
    (44, u"۴۴", u"چوالیس"),
    (45, u"۴۵", u"پینتالیس"),
    (46, u"۴۶", u"چھیالیس"),
    (47, u"۴۷", u"سینتالیس"),
    (48, u"۴۸", u"اڑتالیس"),
    (49, u"۴۹", u"انچاس"),
    (50, u"۵۰", u"پچاس"),
    (51, u"۵۱", u"اکیاون"),
    (52, u"۵۲", u"باون"),
    (53, u"۵۳", u"تریپن"),
    (54, u"۵۴", u"چون"),
    (55, u"۵۵", u"پچپن"),
    (56, u"۵۶", u"چھپن"),
    (57, u"۵۷", u"ستاون"),
    (58, u"۵۸", u"اٹھاون"),
    (59, u"۵۹", u"انسٹھ"),
    (60, u"۶۰", u"ساٹھ"),
    (61, u"۶۱", u"اکسٹھ"),
    (62, u"۶۲", u"باسٹھ"),
    (63, u"۶۳", u"تریسٹھ"),
    (64, u"۶۴", u"چونسٹھ"),
    (65, u"۶۵", u"پینسٹھ"),
    (66, u"۶۶", u"چھیاسٹھ"),
    (67, u"۶۷", u"سڑسٹھ"),
    (68, u"۶۸", u"اڑسٹھ"),
    (69, u"۶۹", u"انہتر"),
    (70, u"۷۰", u"ستر"),
    (71, u"۷۱", u"اکہتر"),
    (72, u"۷۲", u"بہتر"),
    (73, u"۷۳", u"تہتر"),
    (74, u"۷۴", u"چہتر"),
    (75, u"۷۵", u"پچھتر"),
    (76, u"۷۶", u"چھہتر"),
    (77, u"۷۷", u"ستتر"),
    (78, u"۷۸", u"اٹھہتر"),
    (79, u"۷۹", u"اناسی"),
    (80, u"۸۰", u"اسی"),
    (81, u"۸۱", u"اکیاسی"),
    (82, u"۸۲", u"بیاسی"),
    (83, u"۸۳", u"تراسی"),
    (84, u"۸۴", u"چوراسی"),
    (85, u"۸۵", u"پچاسی"),
    (86, u"۸۶", u"چھیاسی"),
    (87, u"۸۷", u"ستاسی"),
    (88, u"۸۸", u"اٹھاسی"),
    (89, u"۸۹", u"نواسی"),
    (90, u"۹۰", u"نوے"),
    (91, u"۹۱", u"اکیانوے"),
    (92, u"۹۲", u"بانوے"),
    (93, u"۹۳", u"ترانوے"),
    (94, u"۹۴", u"چورانوے"),
    (95, u"۹۵", u"پچانوے"),
    (96, u"۹۶", u"چھیانوے"),
    (97, u"۹۷", u"ستانوے"),
    (98, u"۹۸", u"اٹھانوے"),
    (99, u"۹۹", u"ننانوے"),

    (100, u"۱۰۰", u"ایک سو"),
    (1000, u"۱۰۰۰", u"ایک ہزار"),
    (10000, u"۱۰۰۰۰", u"دس ہزار"),
    (100000, u"۱۰۰۰۰۰", u"ایک لاکھ"),
    (1000000, u"۱۰۰۰۰۰۰", u"دس لاکھ"),
    (10000000, u"۱۰۰۰۰۰۰۰", u"ایک کروڑ"),
    (100000000, u"۱۰۰۰۰۰۰۰۰", u"دس کروڑ"),
    (1000000000, u"۱۰۰۰۰۰۰۰۰۰", u"ایک ارب"),
    (10000000000, u"۱۰۰۰۰۰۰۰۰۰۰", u"دس ارب"),
    (100000000000, u"۱۰۰۰۰۰۰۰۰۰۰۰", u"ایک کھرب"),
    (1000000000000, u"۱۰۰۰۰۰۰۰۰۰۰۰۰", u"دس کھرب"),

    (1234, u"۱۲۳۴", u"ایک ہزار دو سو چونتیس"),
    (8901234, u"۸۹۰۱۲۳۴", u"نواسی لاکھ ایک ہزار دو سو چونتیس"),
    (567890123, u"۵۶۷۸۹۰۱۲۳",
        u"چھپن کروڑ اٹھہتر لاکھ نوے ہزار ایک سو تیئیس"),
    (113345, u"۱۱۳۳۴۵", u"ایک لاکھ تیرہ ہزار تین سو پینتالیس"),
)


class Num2WordsURTest(TestCase):
    def test_cardinal(self):
        for number, _, words in TEST_CASES_CARDINAL:
            self.assertEqual(
                num2words(number, lang="ur"),
                words,
                msg="failing number %s" % number,
            )

    # In python3, Hindi numbers are implicitly converted into number
    # as `assert int('४२') == 42`.
    # Thus it's possible to pass Hindi numbers string directly
    # to the num2words as `num2words('४२', lang='hi')`.
    # This will work for any language,
    # but is relevant to test for Hindi particularly.
    def test_urdu_numeric_input(self):
        for number, hindi_number, words in TEST_CASES_CARDINAL:
            self.assertEqual(
                num2words(hindi_number, lang="ur"),
                words,
                msg="failing number %s" % number,
            )
