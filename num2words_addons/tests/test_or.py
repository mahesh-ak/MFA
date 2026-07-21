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

# number, odia number, pronounced form
TEST_CASES_CARDINAL = (
    (0, u"୦", u"ଶୂନ୍ୟ"),
    (1, u"୧", u"ଏକ"),
    (2, u"୨", u"ଦୁଇ"),
    (3, u"୩", u"ତିନି"),
    (4, u"୪", u"ଚାରି"),
    (5, u"୫", u"ପାଞ୍ଚ"),
    (6, u"୬", u"ଛଅ"),
    (7, u"୭", u"ସାତ"),
    (8, u"୮", u"ଆଠ"),
    (9, u"୯", u"ନଅ"),
    (10, u"୧୦", u"ଦଶ"),
    (11, u"୧୧", u"ଏଗାର"),
    (12, u"୧୨", u"ବାର"),
    (13, u"୧୩", u"ତେର"),
    (14, u"୧୪", u"ଚଉଦ"),
    (15, u"୧୫", u"ପନ୍ଦର"),
    (16, u"୧୬", u"ଷୋଳ"),
    (17, u"୧୭", u"ସତର"),
    (18, u"୧୮", u"ଅଠାର"),
    (19, u"୧୯", u"ଊଣେଇଶ"),
    (20, u"୨୦", u"କୋଡ଼ିଏ"),
    (21, u"୨୧", u"ଏକୋଇଶ"),
    (22, u"୨୨", u"ବାଇଶ"),
    (23, u"୨୩", u"ତେଇଶ"),
    (24, u"୨୪", u"ଚଉବିଶ"),
    (25, u"୨୫", u"ପଚିଶ"),
    (26, u"୨୬", u"ଛବିଶ"),
    (27, u"୨୭", u"ସତାଇଶି"),
    (28, u"୨୮", u"ଅଠାଇଶ"),
    (29, u"୨୯", u"ଉଣତିରିଶ"),
    (30, u"୩୦", u"ତିରିଶ"),
    (31, u"୩୧", u"ଏକତିରିଶ"),
    (32, u"୩୨", u"ବତିରିଶ"),
    (33, u"୩୩", u"ତେତିରିଶ"),
    (34, u"୩୪", u"ଚଉତିରିଶ"),
    (35, u"୩୫", u"ପଞ୍ଚତିରିଶ"),
    (36, u"୩୬", u"ଛତିରିଶ"),
    (37, u"୩୭", u"ସତତିରିଶ"),
    (38, u"୩୮", u"ଅଠତିରିଶ"),
    (39, u"୩୯", u"ଊଣଚାଳିଶ"),
    (40, u"୪୦", u"ଚାଳିଶ"),
    (41, u"୪୧", u"ଏକଚାଳିଶ"),
    (42, u"୪୨", u"ବୟାଳିଶ"),
    (43, u"୪୩", u"ତେତାଳିଶ"),
    (44, u"୪୪", u"ଚଉଚାଳିଶ"),
    (45, u"୪୫", u"ପଞ୍ଚଚାଳିଶ"),
    (46, u"୪୬", u"ଛଅଚାଳିଶ"),
    (47, u"୪୭", u"ସତଚାଳିଶ"),
    (48, u"୪୮", u"ଅଠଚାଳିଶ"),
    (49, u"୪୯", u"ଊଣପଚାଶ"),
    (50, u"୫୦", u"ପଚାଶ"),
    (51, u"୫୧", u"ଏକାବନ"),
    (52, u"୫୨", u"ବାବନ"),
    (53, u"୫୩", u"ତେବନ"),
    (54, u"୫୪", u"ଚଉବନ"),
    (55, u"୫୫", u"ପଚାବନ"),
    (56, u"୫୬", u"ଛପ୍ପନ"),
    (57, u"୫୭", u"ସତାବନ"),
    (58, u"୫୮", u"ଅଠାବନ"),
    (59, u"୫୯", u"ଊଣଷାଠି"),
    (60, u"୬୦", u"ଷାଠି"),
    (61, u"୬୧", u"ଏକଷାଠି"),
    (62, u"୬୨", u"ବାଷାଠି"),
    (63, u"୬୩", u"ତେଷାଠି"),
    (64, u"୬୪", u"ଚଉଷାଠି"),
    (65, u"୬୫", u"ପଞ୍ଚଷାଠି"),
    (66, u"୬୬", u"ଛଷାଠି"),
    (67, u"୬୭", u"ସତଷାଠି"),
    (68, u"୬୮", u"ଅଠଷାଠି"),
    (69, u"୬୯", u"ଊଣସତର"),
    (70, u"୭୦", u"ସତର"),
    (71, u"୭୧", u"ଏକସତର"),
    (72, u"୭୨", u"ବାହତର"),
    (73, u"୭୩", u"ତେହତର"),
    (74, u"୭୪", u"ଚଉହତର"),
    (75, u"୭୫", u"ପଞ୍ଚହତର"),
    (76, u"୭୬", u"ଛହତର"),
    (77, u"୭୭", u"ସତହତର"),
    (78, u"୭୮", u"ଅଠହତର"),
    (79, u"୭୯", u"ଊଣଅଶୀ"),
    (80, u"୮୦", u"ଅଶୀ"),
    (81, u"୮୧", u"ଏକାଶୀ"),
    (82, u"୮୨", u"ବୟାଶୀ"),
    (83, u"୮୩", u"ତେଆଶୀ"),
    (84, u"୮୪", u"ଚଉରାଶୀ"),
    (85, u"୮୫", u"ପଞ୍ଚାଶୀ"),
    (86, u"୮୬", u"ଛଅଶୀ"),
    (87, u"୮୭", u"ସତାଶୀ"),
    (88, u"୮୮", u"ଅଠାଶୀ"),
    (89, u"୮୯", u"ନବାଶୀ"),
    (90, u"୯୦", u"ନବେ"),
    (91, u"୯୧", u"ଏକାନବେ"),
    (92, u"୯୨", u"ବାନବେ"),
    (93, u"୯୩", u"ତେରାନବେ"),
    (94, u"୯୪", u"ଚଉରାନବେ"),
    (95, u"୯୫", u"ପଞ୍ଚାନବେ"),
    (96, u"୯୬", u"ଛଅନବେ"),
    (97, u"୯୭", u"ସତାନବେ"),
    (98, u"୯୮", u"ଅଠାନବେ"),
    (99, u"୯୯", u"ନିନାନବେ"),

    (100, u"୧୦୦", u"ଏକ ଶତ"),
    (1000, u"୧୦୦୦", u"ଏକ ହଜାର"),
    (10000, u"୧୦୦୦୦", u"ଦଶ ହଜାର"),
    (100000, u"୧୦୦୦୦୦", u"ଏକ ଲକ୍ଷ"),
    (1000000, u"୧୦୦୦୦୦୦", u"ଦଶ ଲକ୍ଷ"),
    (10000000, u"୧୦୦୦୦୦୦୦", u"ଏକ କୋଟି"),
    (100000000, u"୧୦୦୦୦୦୦୦୦", u"ଦଶ କୋଟି"),
    (1000000000, u"୧୦୦୦୦୦୦୦୦୦", u"ଏକ ଅରବ"),
    (10000000000, u"୧୦୦୦୦୦୦୦୦୦୦", u"ଦଶ ଅରବ"),
    (100000000000, u"୧୦୦୦୦୦୦୦୦୦୦୦", u"ଏକ ଖରବ"),
    (1000000000000, u"୧୦୦୦୦୦୦୦୦୦୦୦୦", u"ଦଶ ଖରବ"),

    (1234, u"୧୨୩୪", u"ଏକ ହଜାର ଦୁଇ ଶତ ଚଉତିରିଶ"),
    (8901234, u"୮୯୦୧୨୩୪", u"ନବାଶୀ ଲକ୍ଷ ଏକ ହଜାର ଦୁଇ ଶତ ଚଉତିରିଶ"),
    (567890123, u"୫୬୭୮୯୦୧୨୩",
        u"ଛପ୍ପନ କୋଟି ଅଠହତର ଲକ୍ଷ ନବେ ହଜାର ଏକ ଶତ ତେଇଶ"),
    (113345, u"୧୧୩୩୪୫", u"ଏକ ଲକ୍ଷ ତେର ହଜାର ତିନି ଶତ ପଞ୍ଚଚାଳିଶ"),
)

class Num2WordsORTest(TestCase):
    def test_cardinal(self):
        for number, _, words in TEST_CASES_CARDINAL:
            self.assertEqual(
                num2words(number, lang="or"),
                words,
                msg="failing number %s" % number,
            )

   # In python3, Hindi numbers are implicitly converted into number
    # as `assert int('४२') == 42`.
    # Thus it's possible to pass Hindi numbers string directly
    # to the num2words as `num2words('४२', lang='hi')`.
    # This will work for any language,
    # but is relevant to test for Hindi particularly.
    def test_odia_numeric_input(self):
        for number, hindi_number, words in TEST_CASES_CARDINAL:
            self.assertEqual(
                num2words(hindi_number, lang="or"),
                words,
                msg="failing number %s" % number,
            )
