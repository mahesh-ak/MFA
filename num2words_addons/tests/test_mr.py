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

# number, hindi number, pronounced form

TEST_CASES_CARDINAL = (
    (0, u"०", u"शून्य"),
    (1, u"१", u"एक"),
    (2, u"२", u"दोन"),
    (3, u"३", u"तीन"),
    (4, u"४", u"चार"),
    (5, u"५", u"पाच"),
    (6, u"६", u"सहा"),
    (7, u"७", u"सात"),
    (8, u"८", u"आठ"),
    (9, u"९", u"नऊ"),
    (10, u"१०", u"दहा"),
    (11, u"११", u"अकरा"),
    (12, u"१२", u"बारा"),
    (13, u"१३", u"तेरा"),
    (14, u"१४", u"चौदा"),
    (15, u"१५", u"पंधरा"),
    (16, u"१६", u"सोळा"),
    (17, u"१७", u"सतरा"),
    (18, u"१८", u"अठरा"),
    (19, u"१९", u"एकोणीस"),
    (20, u"२०", u"वीस"),
    (21, u"२१", u"एकवीस"),
    (22, u"२२", u"बावीस"),
    (23, u"२३", u"तेवीस"),
    (24, u"२४", u"चोवीस"),
    (25, u"२५", u"पंचवीस"),
    (26, u"२६", u"सव्वीस"),
    (27, u"२७", u"सत्तावीस"),
    (28, u"२८", u"अठ्ठावीस"),
    (29, u"२९", u"एकोणतीस"),
    (30, u"३०", u"तीस"),
    (31, u"३१", u"एकतीस"),
    (32, u"३२", u"बत्तीस"),
    (33, u"३३", u"तेहतीस"),
    (34, u"३४", u"चौतीस"),
    (35, u"३५", u"पस्तीस"),
    (36, u"३६", u"छत्तीस"),
    (37, u"३७", u"सदतीस"),
    (38, u"३८", u"अडतीस"),
    (39, u"३९", u"एकोणचाळीस"),
    (40, u"४०", u"चाळीस"),
    (41, u"४१", u"एकेचाळीस"),
    (42, u"४२", u"बेचाळीस"),
    (43, u"४३", u"त्रेचाळीस"),
    (44, u"४४", u"चव्वेचाळीस"),
    (45, u"४५", u"पंचेचाळीस"),
    (46, u"४६", u"सेहेचाळीस"),
    (47, u"४७", u"सत्तेचाळीस"),
    (48, u"४८", u"अठ्ठेचाळीस"),
    (49, u"४९", u"एकोणपन्नास"),
    (50, u"५०", u"पन्नास"),
    (51, u"५१", u"एकावन्न"),
    (52, u"५२", u"बावन्न"),
    (53, u"५३", u"त्रेपन्न"),
    (54, u"५४", u"चौवन्न"),
    (55, u"५५", u"पंचावन्न"),
    (56, u"५६", u"छप्पन्न"),
    (57, u"५७", u"सत्तावन्न"),
    (58, u"५८", u"अठ्ठावन्न"),
    (59, u"५९", u"एकोणसाठ"),
    (60, u"६०", u"साठ"),
    (61, u"६१", u"एकसष्ट"),
    (62, u"६२", u"बासष्ट"),
    (63, u"६३", u"त्रेसष्ट"),
    (64, u"६४", u"चौसष्ट"),
    (65, u"६५", u"पासष्ट"),
    (66, u"६६", u"सहासष्ट"),
    (67, u"६७", u"सदुसष्ट"),
    (68, u"६८", u"अडुसष्ट"),
    (69, u"६९", u"एकोणसत्तर"),
    (70, u"७०", u"सत्तर"),
    (71, u"७१", u"एकाहत्तर"),
    (72, u"७२", u"बहात्तर"),
    (73, u"७३", u"त्र्याहत्तर"),
    (74, u"७४", u"चौरेहत्तर"),
    (75, u"७५", u"पंच्याहत्तर"),
    (76, u"७६", u"शहात्तर"),
    (77, u"७७", u"सत्याहत्तर"),
    (78, u"७८", u"अठ्ठ्याहत्तर"),
    (79, u"७९", u"एकोणऐंशी"),
    (80, u"८०", u"ऐंशी"),
    (81, u"८१", u"एक्याऐंशी"),
    (82, u"८२", u"ब्याऐंशी"),
    (83, u"८३", u"त्र्याऐंशी"),
    (84, u"८४", u"चौरेऐंशी"),
    (85, u"८५", u"पंच्याऐंशी"),
    (86, u"८६", u"सह्यांशी"),
    (87, u"८७", u"सत्त्याऐंशी"),
    (88, u"८८", u"अठ्ठ्याऐंशी"),
    (89, u"८९", u"एकोणनव्वद"),
    (90, u"९०", u"नव्वद"),
    (91, u"९१", u"एक्याण्णव"),
    (92, u"९२", u"ब्याण्णव"),
    (93, u"९३", u"त्र्याण्णव"),
    (94, u"९४", u"चौऱ्याण्णव"),
    (95, u"९५", u"पंच्याण्णव"),
    (96, u"९६", u"शह्याण्णव"),
    (97, u"९७", u"सत्त्याण्णव"),
    (98, u"९८", u"अठ्ठ्याण्णव"),
    (99, u"९९", u"नव्व्याण्णव"),

    (100, u"१००", u"एक शंभर"),
    (1000, u"१०००", u"एक हजार"),
    (10000, u"१००००", u"दहा हजार"),
    (100000, u"१०००००", u"एक लाख"),
    (1000000, u"१००००००", u"दहा लाख"),
    (10000000, u"१०००००००", u"एक कोटी"),
    (100000000, u"१००००००००", u"दहा कोटी"),
    (1000000000, u"१०००००००००", u"एक अब्ज"),
    (10000000000, u"१००००००००००", u"दहा अब्ज"),
    (100000000000, u"१०००००००००००", u"एक खर्व"),
    (1000000000000, u"१००००००००००००", u"दहा खर्व"),

    (1234, u"१२३४", u"एक हजार दोन शंभर चौतीस"),
    (8901234, u"८९०१२३४", u"एकोणनव्वद लाख एक हजार दोन शंभर चौतीस"),
    (567890123, u"५६७८९०१२३",
        u"छप्पन्न कोटी अठ्ठ्याहत्तर लाख नव्वद हजार एक शंभर तेवीस"),
    (113345, u"११३३४५", u"एक लाख तेरा हजार तीन शंभर पंचेचाळीस"),
)

class Num2WordsMRTest(TestCase):
    def test_cardinal(self):
        for number, _, words in TEST_CASES_CARDINAL:
            self.assertEqual(
                num2words(number, lang="mr"),
                words,
                msg="failing number %s" % number,
            )

    def test_marathi_numeric_input(self):
        for number, hindi_number, words in TEST_CASES_CARDINAL:
            self.assertEqual(
                num2words(hindi_number, lang="mr"),
                words,
                msg="failing number %s" % number,
            )
