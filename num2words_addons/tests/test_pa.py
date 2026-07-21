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

# number, punjabi number, pronounced form
TEST_CASES_CARDINAL = (
    (0, u"੦", u"ਸਿਫ਼ਰ"),
    (1, u"੧", u"ਇੱਕ"),
    (2, u"੨", u"ਦੋ"),
    (3, u"੩", u"ਤਿੰਨ"),
    (4, u"੪", u"ਚਾਰ"),
    (5, u"੫", u"ਪੰਜ"),
    (6, u"੬", u"ਛੇ"),
    (7, u"੭", u"ਸੱਤ"),
    (8, u"੮", u"ਅੱਠ"),
    (9, u"੯", u"ਨੌਂ"),
    (10, u"੧੦", u"ਦੱਸ"),
    (11, u"੧੧", u"ਗਿਆਰਾਂ"),
    (12, u"੧੨", u"ਬਾਰਾਂ"),
    (13, u"੧੩", u"ਤੇਰਾਂ"),
    (14, u"੧੪", u"ਚੌਦਾਂ"),
    (15, u"੧੫", u"ਪੰਦਰਾਂ"),
    (16, u"੧੬", u"ਸੋਲ੍ਹਾਂ"),
    (17, u"੧੭", u"ਸਤਾਰਾਂ"),
    (18, u"੧੮", u"ਅਠਾਰਾਂ"),
    (19, u"੧੯", u"ਉੱਨੀ"),
    (20, u"੨੦", u"ਵੀਹ"),
    (21, u"੨੧", u"ਇੱਕੀ"),
    (22, u"੨੨", u"ਬਾਈ"),
    (23, u"੨੩", u"ਤੇਈ"),
    (24, u"੨੪", u"ਚੌਵੀ"),
    (25, u"੨੫", u"ਪੱਚੀ"),
    (26, u"੨੬", u"ਛੱਬੀ"),
    (27, u"੨੭", u"ਸਤਾਈ"),
    (28, u"੨੮", u"ਅਠਾਈ"),
    (29, u"੨੯", u"ਉਣੱਤੀ"),
    (30, u"੩੦", u"ਤੀਹ"),
    (31, u"੩੧", u"ਇਕੱਤੀ"),
    (32, u"੩੨", u"ਬੱਤੀ"),
    (33, u"੩੩", u"ਤੈਂਤੀ"),
    (34, u"੩੪", u"ਚੌਂਤੀ"),
    (35, u"੩੫", u"ਪੈਂਤੀ"),
    (36, u"੩੬", u"ਛੱਤੀ"),
    (37, u"੩੭", u"ਸੈਂਤੀ"),
    (38, u"੩੮", u"ਅਠੱਤੀ"),
    (39, u"੩੯", u"ਉਣਤਾਲੀ"),
    (40, u"੪੦", u"ਚਾਲੀ"),
    (41, u"੪੧", u"ਇਕਤਾਲੀ"),
    (42, u"੪੨", u"ਬਿਆਲੀ"),
    (43, u"੪੩", u"ਤੈਂਤਾਲੀ"),
    (44, u"੪੪", u"ਚੌਂਤਾਲੀ"),
    (45, u"੪੫", u"ਪੈਂਤਾਲੀ"),
    (46, u"੪੬", u"ਛਿਆਲੀ"),
    (47, u"੪੭", u"ਸੈਂਤਾਲੀ"),
    (48, u"੪੮", u"ਅਠਤਾਲੀ"),
    (49, u"੪੯", u"ਉਣੰਜਾ"),
    (50, u"੫੦", u"ਪੰਜਾਹ"),
    (51, u"੫੧", u"ਇਕਵੰਜਾ"),
    (52, u"੫੨", u"ਬਵੰਜਾ"),
    (53, u"੫੩", u"ਤਰਵੰਜਾ"),
    (54, u"੫੪", u"ਚੌਵੰਜਾ"),
    (55, u"੫੫", u"ਪਚਵੰਜਾ"),
    (56, u"੫੬", u"ਛਵੰਜਾ"),
    (57, u"੫੭", u"ਸਤਾਵੰਜਾ"),
    (58, u"੫੮", u"ਅਠਾਵੰਜਾ"),
    (59, u"੫੯", u"ਉਣਸੱਠ"),
    (60, u"੬੦", u"ਸੱਠ"),
    (61, u"੬੧", u"ਇਕਾਹਠ"),
    (62, u"੬੨", u"ਬਾਹਠ"),
    (63, u"੬੩", u"ਤਰਾਹਠ"),
    (64, u"੬੪", u"ਚੌਂਸਠ"),
    (65, u"੬੫", u"ਪੈਂਸਠ"),
    (66, u"੬੬", u"ਛਿਆਸਠ"),
    (67, u"੬੭", u"ਸਤਾਸਠ"),
    (68, u"੬੮", u"ਅਠਾਸਠ"),
    (69, u"੬੯", u"ਉਣੱਤਰ"),
    (70, u"੭੦", u"ਸਤੱਰ"),
    (71, u"੭੧", u"ਇਕੱਤਰ"),
    (72, u"੭੨", u"ਬਹੱਤਰ"),
    (73, u"੭੩", u"ਤਿਹੱਤਰ"),
    (74, u"੭੪", u"ਚੌਹੱਤਰ"),
    (75, u"੭੫", u"ਪਚੱਤਰ"),
    (76, u"੭੬", u"ਛਿਹੱਤਰ"),
    (77, u"੭੭", u"ਸਤੱਤਰ"),
    (78, u"੭੮", u"ਅਠੱਤਰ"),
    (79, u"੭੯", u"ਉਣਾਸੀ"),
    (80, u"੮੦", u"ਅੱਸੀ"),
    (81, u"੮੧", u"ਇਕਿਆਸੀ"),
    (82, u"੮੨", u"ਬਿਆਸੀ"),
    (83, u"੮੩", u"ਤਰਾਸੀ"),
    (84, u"੮੪", u"ਚੌਰਾਸੀ"),
    (85, u"੮੫", u"ਪਚਾਸੀ"),
    (86, u"੮੬", u"ਛਿਆਸੀ"),
    (87, u"੮੭", u"ਸਤਾਸੀ"),
    (88, u"੮੮", u"ਅਠਾਸੀ"),
    (89, u"੮੯", u"ਨਵਾਸੀ"),
    (90, u"੯੦", u"ਨੱਬੇ"),
    (91, u"੯੧", u"ਇਕਿਆਣਵੇ"),
    (92, u"੯੨", u"ਬਾਣਵੇ"),
    (93, u"੯੩", u"ਤਰਾਣਵੇ"),
    (94, u"੯੪", u"ਚੌਰਾਣਵੇ"),
    (95, u"੯੫", u"ਪਚਾਣਵੇ"),
    (96, u"੯੬", u"ਛਿਆਣਵੇ"),
    (97, u"੯੭", u"ਸਤਾਣਵੇ"),
    (98, u"੯੮", u"ਅਠਾਣਵੇ"),
    (99, u"੯੯", u"ਨਿੰਨਾਣਵੇ"),

    (100, u"੧੦੦", u"ਇੱਕ ਸੌ"),
    (1000, u"੧੦੦੦", u"ਇੱਕ ਹਜ਼ਾਰ"),
    (10000, u"੧੦੦੦੦", u"ਦੱਸ ਹਜ਼ਾਰ"),
    (100000, u"੧੦੦੦੦੦", u"ਇੱਕ ਲੱਖ"),
    (1000000, u"੧੦੦੦੦੦੦", u"ਦੱਸ ਲੱਖ"),
    (10000000, u"੧੦੦੦੦੦੦੦", u"ਇੱਕ ਕਰੋੜ"),
    (100000000, u"੧੦੦੦੦੦੦੦੦", u"ਦੱਸ ਕਰੋੜ"),
    (1000000000, u"੧੦੦੦੦੦੦੦੦੦", u"ਇੱਕ ਅਰਬ"),
    (10000000000, u"੧੦੦੦੦੦੦੦੦੦੦", u"ਦੱਸ ਅਰਬ"),
    (100000000000, u"੧੦੦੦੦੦੦੦੦੦੦੦", u"ਇੱਕ ਖਰਬ"),
    (1000000000000, u"੧੦੦੦੦੦੦੦੦੦੦੦੦", u"ਦੱਸ ਖਰਬ"),

    (1234, u"੧੨੩੪", u"ਇੱਕ ਹਜ਼ਾਰ ਦੋ ਸੌ ਚੌਂਤੀ"),
    (8901234, u"੮੯੦੧੨੩੪", u"ਨਵਾਸੀ ਲੱਖ ਇੱਕ ਹਜ਼ਾਰ ਦੋ ਸੌ ਚੌਂਤੀ"),
    (567890123, u"੫੬੭੮੯੦੧੨੩",
        u"ਛਵੰਜਾ ਕਰੋੜ ਅਠੱਤਰ ਲੱਖ ਨੱਬੇ ਹਜ਼ਾਰ ਇੱਕ ਸੌ ਤੇਈ"),
    (113345, u"੧੧੩੩੪੫", u"ਇੱਕ ਲੱਖ ਤੇਰਾਂ ਹਜ਼ਾਰ ਤਿੰਨ ਸੌ ਪੈਂਤਾਲੀ"),
)

class Num2WordsPATest(TestCase):
    def test_cardinal(self):
        for number, _, words in TEST_CASES_CARDINAL:
            self.assertEqual(
                num2words(number, lang="pa"),
                words,
                msg="failing number %s" % number,
            )


    # In python3, Hindi numbers are implicitly converted into number
    # as `assert int('४२') == 42`.
    # Thus it's possible to pass Hindi numbers string directly
    # to the num2words as `num2words('४२', lang='hi')`.
    # This will work for any language,
    # but is relevant to test for Hindi particularly.
    def test_punjabi_numeric_input(self):
        for number, hindi_number, words in TEST_CASES_CARDINAL:
            self.assertEqual(
                num2words(hindi_number, lang="pa"),
                words,
                msg="failing number %s" % number,
            )
