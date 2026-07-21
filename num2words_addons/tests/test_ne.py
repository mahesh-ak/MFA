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

# number, nepali number, pronounced form
TEST_CASES_CARDINAL = (
    (0, u"०", u"शून्य"),
    (1, u"१", u"एक"),
    (2, u"२", u"दुई"),
    (3, u"३", u"तीन"),
    (4, u"४", u"चार"),
    (5, u"५", u"पाँच"),
    (6, u"६", u"छ"),
    (7, u"७", u"सात"),
    (8, u"८", u"आठ"),
    (9, u"९", u"नौ"),
    (10, u"१०", u"दश"),
    (11, u"११", u"एघार"),
    (12, u"१२", u"बाह्र"),
    (13, u"१३", u"तेह्र"),
    (14, u"१४", u"चौध"),
    (15, u"१५", u"पन्ध्र"),
    (16, u"१६", u"सोह्र"),
    (17, u"१७", u"सत्र"),
    (18, u"१८", u"अठार"),
    (19, u"१९", u"उन्नाइस"),
    (20, u"२०", u"बीस"),
    (21, u"२१", u"एक्काइस"),
    (22, u"२२", u"बाइस"),
    (23, u"२३", u"तेइस"),
    (24, u"२४", u"चौबीस"),
    (25, u"२५", u"पच्चीस"),
    (26, u"२६", u"छब्बीस"),
    (27, u"२७", u"सत्ताइस"),
    (28, u"२८", u"अठाइस"),
    (29, u"२९", u"उनन्तीस"),
    (30, u"३०", u"तीस"),
    (31, u"३१", u"एकतीस"),
    (32, u"३२", u"बत्तीस"),
    (33, u"३३", u"तेत्तीस"),
    (34, u"३४", u"चौँतीस"),
    (35, u"३५", u"पैतीस"),
    (36, u"३६", u"छत्तीस"),
    (37, u"३७", u"सैतीस"),
    (38, u"३८", u"अठतीस"),
    (39, u"३९", u"उनन्चालिस"),
    (40, u"४०", u"चालिस"),
    (41, u"४१", u"एकचालिस"),
    (42, u"४२", u"बयालिस"),
    (43, u"४३", u"त्रेचालिस"),
    (44, u"४४", u"चौवालीस"),
    (45, u"४५", u"पैतालिस"),
    (46, u"४६", u"छयालिस"),
    (47, u"४७", u"सन्तालिस"),
    (48, u"४८", u"अठचालिस"),
    (49, u"४९", u"उनन्चास"),
    (50, u"५०", u"पचास"),
    (51, u"५१", u"एकाउन्न"),
    (52, u"५२", u"बाउन्न"),
    (53, u"५३", u"त्रेपन्न"),
    (54, u"५४", u"चौवन्न"),
    (55, u"५५", u"पचपन्न"),
    (56, u"५६", u"छपन्न"),
    (57, u"५७", u"सन्ताउन्न"),
    (58, u"५८", u"अन्ठाउन्न"),
    (59, u"५९", u"उनन्साठी"),
    (60, u"६०", u"साठी"),
    (61, u"६१", u"एकसाठी"),
    (62, u"६२", u"बासाठी"),
    (63, u"६३", u"त्रिसाठी"),
    (64, u"६४", u"चौँसाठी"),
    (65, u"६५", u"पैसाठी"),
    (66, u"६६", u"छयसाठी"),
    (67, u"६७", u"सतसाठी"),
    (68, u"६८", u"अठसाठी"),
    (69, u"६९", u"उनहत्तर"),
    (70, u"७०", u"सत्तरी"),
    (71, u"७१", u"एकहत्तर"),
    (72, u"७२", u"बहत्तर"),
    (73, u"७३", u"त्रिहत्तर"),
    (74, u"७४", u"चौहत्तर"),
    (75, u"७५", u"पचहत्तर"),
    (76, u"७६", u"छयहत्तर"),
    (77, u"७७", u"सतहत्तर"),
    (78, u"७८", u"अठहत्तर"),
    (79, u"७९", u"उनासी"),
    (80, u"८०", u"असी"),
    (81, u"८१", u"एकासी"),
    (82, u"८२", u"बयासी"),
    (83, u"८३", u"त्रियासी"),
    (84, u"८४", u"चौरासी"),
    (85, u"८५", u"पचासी"),
    (86, u"८६", u"छयासी"),
    (87, u"८७", u"सत्तासी"),
    (88, u"८८", u"अठासी"),
    (89, u"८९", u"नवासी"),
    (90, u"९०", u"नब्बे"),
    (91, u"९१", u"एकान्नब्बे"),
    (92, u"९२", u"बयान्नब्बे"),
    (93, u"९३", u"त्रियान्नब्बे"),
    (94, u"९४", u"चौरान्नब्बे"),
    (95, u"९५", u"पन्चान्नब्बे"),
    (96, u"९६", u"छयान्नब्बे"),
    (97, u"९७", u"सन्तान्नब्बे"),
    (98, u"९८", u"अन्ठान्नब्बे"),
    (99, u"९९", u"उनान्नब्बे"),

    (100, u"१००", u"एक सय"),
    (1000, u"१०००", u"एक हजार"),
    (10000, u"१००००", u"दश हजार"),
    (100000, u"१०००००", u"एक लाख"),
    (1000000, u"१००००००", u"दश लाख"),
    (10000000, u"१०००००००", u"एक करोड"),
    (100000000, u"१००००००००", u"दश करोड"),
    (1000000000, u"१०००००००००", u"एक अर्ब"),
    (10000000000, u"१००००००००००", u"दश अर्ब"),
    (100000000000, u"१०००००००००००", u"एक खर्ब"),
    (1000000000000, u"१००००००००००००", u"दश खर्ब"),

    (1234, u"१२३४", u"एक हजार दुई सय चौँतीस"),
    (8901234, u"८९०१२३४", u"नवासी लाख एक हजार दुई सय चौँतीस"),
    (567890123, u"५६७८९०१२३",
        u"छपन्न करोड अठहत्तर लाख नब्बे हजार एक सय तेइस"),
    (113345, u"११३३४५", u"एक लाख तेह्र हजार तीन सय पैतालिस"),
)

class Num2WordsNETest(TestCase):
    def test_cardinal(self):
        for number, _, words in TEST_CASES_CARDINAL:
            self.assertEqual(
                num2words(number, lang="ne"),
                words,
                msg="failing number %s" % number,
            )


    # In python3, Hindi numbers are implicitly converted into number
    # as `assert int('४२') == 42`.
    # Thus it's possible to pass Hindi numbers string directly
    # to the num2words as `num2words('४२', lang='hi')`.
    # This will work for any language,
    # but is relevant to test for Hindi particularly.
    def test_nepali_numeric_input(self):
        for number, hindi_number, words in TEST_CASES_CARDINAL:
            self.assertEqual(
                num2words(hindi_number, lang="ne"),
                words,
                msg="failing number %s" % number,
            )
