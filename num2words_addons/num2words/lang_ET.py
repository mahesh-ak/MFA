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

from __future__ import division, print_function, unicode_literals

from collections import OrderedDict

from . import lang_EU

GENERIC_CENTS = ('sent', 'senti')
GENERIC_CENTAVOS = ('sent', 'senti')

# grammatical cases (keep same constants)
NOM = 10
GEN = 11
ACC = 12
PTV = 13
INE = 14
ELA = 15
ILL = 16
ADE = 17
ABL = 18
ALL = 19
ESS = 20
TRANSL = 21
INSTRUC = 22
ABE = 23
COM = 24

NAME_TO_CASE = {
    'nominative': NOM,
    'genitive': GEN,
    'accusative': ACC,
    'partitive': PTV,
    'inessive': INE,
    'elative': ELA,
    'illative': ILL,
    'adessive': ADE,
    'ablative': ABL,
    'allative': ALL,
    'essive': ESS,
    'translative': TRANSL,
    'instructive': INSTRUC,
    'abessive': ABE,
    'comitative': COM,
}

# ❌ REMOVE vowel harmony (not used in Estonian)
BACK_TO_FRONT = {}

# ✅ Single simplified Estonian pattern
KOTUS_TYPE = {
    1: {
        # grammatical
        NOM: ('', 'd'),
        GEN: ('i', 'de'),
        PTV: ('i', 'sid'),

        # locative (internal)
        INE: ('is', 'des'),
        ELA: ('ist', 'dest'),
        ILL: ('isse', 'desse'),

        # locative (external)
        ADE: ('il', 'del'),
        ABL: ('ilt', 'delt'),
        ALL: ('ile', 'dele'),

        # essive / translative
        ESS: ('ina', 'dena'),
        TRANSL: ('iks', 'deks'),

        # rare
        INSTRUC: ('', ''),
        ABE: ('ita', 'deta'),
        COM: ('iga', 'dega'),
    }
}

# keep compatibility aliases (minimal hack)
KOTUS_TYPE[5] = KOTUS_TYPE[1]
KOTUS_TYPE[7] = KOTUS_TYPE[1]
KOTUS_TYPE[8] = KOTUS_TYPE[1]
KOTUS_TYPE[9] = KOTUS_TYPE[1]
KOTUS_TYPE[10] = KOTUS_TYPE[1]
KOTUS_TYPE[27] = KOTUS_TYPE[1]
KOTUS_TYPE[31] = KOTUS_TYPE[1]
KOTUS_TYPE[32] = KOTUS_TYPE[1]
KOTUS_TYPE[38] = KOTUS_TYPE[1]
KOTUS_TYPE[45] = KOTUS_TYPE[1]
KOTUS_TYPE[46] = KOTUS_TYPE[1]
KOTUS_TYPE[108] = KOTUS_TYPE[1]
KOTUS_TYPE[110] = KOTUS_TYPE[1]
KOTUS_TYPE[132] = KOTUS_TYPE[1]

def inflect(parts, options):
    if not isinstance(parts, list):
        parts = [parts]

    out = ''
    for part in parts:
        # part is plain text, concat and continue
        if not isinstance(part, tuple):
            out += part
            continue
        # predefined case (kaksikymmentä, ...)
        tmp_case = options.case
        if len(part) == 3:
            # override singular nominative only
            if options.case == NOM and not options.plural:
                tmp_case = part[2]
            part = part[:2]
        # stem and suffix
        stem, kotus_type = part
        suffix = KOTUS_TYPE[kotus_type][tmp_case][options.plural]
        # many choices, choose preferred or first
        if isinstance(suffix, tuple):
            common = set(suffix) & set(options.prefer or set())
            if len(common) == 1:
                suffix = common.pop()
            else:
                suffix = suffix[0]
        # apply vowel harmony
        if not set(BACK_TO_FRONT) & set(stem):
            for back, front in BACK_TO_FRONT.items():
                suffix = suffix.replace(back, front)
        # concat
        out += stem + suffix

    return out


class Options(object):
    def __init__(self, ordinal, case, plural, prefer):
        self.ordinal = ordinal
        self.case = case
        self.plural = plural
        self.prefer = prefer

    def variation(self, ordinal=None, case=None, plural=None, prefer=None):
        return Options(
            ordinal if ordinal is not None else self.ordinal,
            case if case is not None else self.case,
            plural if plural is not None else self.plural,
            prefer if prefer is not None else self.prefer,
        )


class Num2Word_ET(lang_EU.Num2Word_EU):
    CURRENCY_FORMS = {
        'BRL': (('real', 'realia'), GENERIC_CENTAVOS),
        'CHF': (('frangi', 'frangia'), ('rappen', 'rappenia')),
        'CNY': (('juan', 'juania'), ('fen', 'feniä')),
        'EUR': (('euro', 'euroa'), GENERIC_CENTS),
        'FIM': (('markka', 'markkaa'), ('penni', 'penniä')),  # historical
        'INR': (('rupia', 'rupiaa'), ('paisa', 'paisaa')),
        'JPY': (('jeni', 'jeniä'), ('sen', 'seniä')),  # rare subunit
        'KRW': (('won', 'wonia'), ('jeon', 'jeonia')),  # rare subunit
        'KPW': (('won', 'wonia'), ('chon', 'chonia')),  # rare subunit
        'MXN': (('peso', 'pesoa'), GENERIC_CENTAVOS),
        'RUB': (('rupla', 'ruplaa'), ('kopeekka', 'kopeekkaa')),
        'TRY': (('liira', 'liiraa'), ('kuruş', 'kuruşia')),
        'ZAR': (('randi', 'randia'), GENERIC_CENTS),
    }

    # crowns
    for curr_code in 'DKK', 'ISK', 'NOK', 'SEK':
        CURRENCY_FORMS[curr_code] = (('kruunu', 'kruunua'), ('äyri', 'äyriä'))

    # dollars
    for curr_code in 'AUD', 'CAD', 'HKD', 'NZD', 'SGD', 'USD':
        CURRENCY_FORMS[curr_code] = (
            ('dollari', 'dollaria'), GENERIC_CENTS)

    # pounds
    for curr_code in ('GBP',):
        CURRENCY_FORMS[curr_code] = (('punta', 'puntaa'), ('penny', 'pennyä'))

    CURRENCY_ADJECTIVES = {
        'AUD': 'Australian',
        'BRL': 'Brasilian',
        'CAD': 'Kanadan',
        'CHF': 'Sveitsin',
        'DKK': 'Tanskan',
        'FIM': 'Suomen',  # historical
        'GBP': 'Englannin',
        'HKD': 'Hongkongin',
        'INR': 'Intian',
        'ISK': 'Islannin',
        'KRW': 'Etelä-Korean',
        'KPW': 'Pohjois-Korean',
        'MXN': 'Meksikon',
        'NOK': 'Norjan',
        'NZD': 'Uuden-Seelannin',
        'RUB': 'Venäjän',
        'SEK': 'Ruotsin',
        'SGD': 'Singaporen',
        'TRY': 'Turkin',
        'USD': 'Yhdysvaltain',
        'ZAR': 'Etelä-Afrikan',
    }

    def __init__(self):
        self.ords = OrderedDict()
        super(Num2Word_ET, self).__init__()

    def set_numwords(self):
        self.set_high_numwords(self.high_numwords)
        self.set_mid_numwords(self.mid_numwords, self.mid_ords)
        self.set_low_numwords(self.low_numwords, self.low_ords)

    def set_high_numwords(self, high):
        # map Latin sequence → correct Estonian names
        replacements = {
            6: "miljon",
            12: "triljon",
            18: "kvadriljon",
            24: "kvintiljon",
            30: "sekstiljon",
            36: "septiljon",
        } 

        max_power = 6 * len(high)

        for n in range(max_power, 0, -6):
            if n == 6:
                # keep existing special case
                self.cards[10 ** 9] = ("miljard", 1)
                self.ords[10 ** 9] = ("miljardes", 1)

            word = replacements.get(n, None)
            if word is None:
                continue  # fallback: skip unknown safely

            self.cards[10 ** n] = (word, 1)
            self.ords[10 ** n] = (word + "es", 1)
        
    def set_mid_numwords(self, cards, ords):
        for key, val in cards:
            self.cards[key] = val
        for key, val in ords:
            self.ords[key] = val

    def set_low_numwords(self, cards, ords):
        for key, val in cards:
            self.cards[key] = val
        for key, val in ords:
            self.ords[key] = val

    def setup(self):
        super(Num2Word_ET, self).setup()

        self.negword = "miinus "
        self.pointword = "koma"
        self.exclude_title = ["koma", "miinus"]

        self.mid_numwords = [
            (1000, ("tuhat", 1)),
            (100, ("sada", 1)),
            (90, [("üheksakümmend", 1)]),
            (80, [("kaheksakümmend", 1)]),
            (70, [("seitsekümmend", 1)]),
            (60, [("kuuskümmend", 1)]),
            (50, [("viiskümmend", 1)]),
            (40, [("nelikümmend", 1)]),
            (30, [("kolmkümmend", 1)]),
        ]

        self.mid_ords = [
            (1000, ("tuhandes", 1)),
            (100, ("sajas", 1)),
            (90, [("üheksakümnes", 1)]),
            (80, [("kaheksakümnes", 1)]),
            (70, [("seitsmekümnes", 1)]),
            (60, [("kuuekümnes", 1)]),
            (50, [("viiekümnes", 1)]),
            (40, [("neljakümnes", 1)]),
            (30, [("kolmekümnes", 1)]),
        ]

        self.low_numwords = [
            (20, [("kakskümmend", 1)]),
            (19, ("üheksateist", 1)),
            (18, ("kaheksateist", 1)),
            (17, ("seitseteist", 1)),
            (16, ("kuusteist", 1)),
            (15, ("viisteist", 1)),
            (14, ("neliteist", 1)),
            (13, ("kolmteist", 1)),
            (12, ("kaksteist", 1)),
            (11, ("üksteist", 1)),
            (10, ("kümme", 1)),
            (9, ("üheksa", 1)),
            (8, ("kaheksa", 1)),
            (7, ("seitse", 1)),
            (6, ("kuus", 1)),
            (5, ("viis", 1)),
            (4, ("neli", 1)),
            (3, ("kolm", 1)),
            (2, ("kaks", 1)),
            (1, ("üks", 1)),
            (0, ("null", 1)),
        ]

        self.low_ords = [
            (20, ("kahekümnes", 1)),
            (19, ("üheksateistkümnes", 1)),
            (18, ("kaheksateistkümnes", 1)),
            (17, ("seitseteistkümnes", 1)),
            (16, ("kuusteistkümnes", 1)),
            (15, ("viieteistkümnes", 1)),
            (14, ("neljateistkümnes", 1)),
            (13, ("kolmeteistkümnes", 1)),
            (12, ("kaheteistkümnes", 1)),
            (11, ("üheteistkümnes", 1)),
            (10, ("kümnes", 1)),
            (9, ("üheksas", 1)),
            (8, ("kaheksas", 1)),
            (7, ("seitsmes", 1)),
            (6, ("kuues", 1)),
            (5, ("viies", 1)),
            (4, ("neljas", 1)),
            (3, ("kolmas", 1)),
            (2, ("teine", 1)),
            (1, ("esimene", 1)),
            (0, ("null", 1)),
        ] 

    def merge(self, lpair, rpair, options):
        ltext, lnum = lpair
        rtext, rnum = rpair

        # http://www.kielitoimistonohjepankki.fi/ohje/49
        fmt = "%s%s"
        # ignore lpair if lnum is 1
        if lnum == 1:
            rtext = inflect(rtext, options)
            # keep "üks" for large units
            if rnum >= 1000000:
                return ("üks" + rtext, rnum)
            return (rtext, rnum)
        # rnum is added to lnum
        elif lnum > rnum:
            ltext = inflect(ltext, options)
            rtext = inflect(rtext, options)
            # separate groups with space
            if lnum >= 1000:
                fmt = "%s%s"
            return (fmt % (ltext, rtext), lnum + rnum)
        # rnum is multiplied by lnum
        elif lnum < rnum:
            if options.ordinal:
                # kahdessadas, not toinensadas
                if lnum == 2:
                    ltext = ("kahde", 45)
                rtext = inflect(rtext, options)
            else:
                # kaksituhatta but kahdettuhannet
                rcase = options.case
                #if options.case == NOM and not options.plural:
                #    rcase = PTV
                rtext = inflect(rtext, options.variation(case=rcase))
            
                if 11 <= lnum <= 19:
                    COMPOUND_TEENS = {
                        11: "üheteist",
                        12: "kaheteist",
                        13: "kolmeteist",
                        14: "neljateist",
                        15: "viieteist",
                        16: "kuueteist",
                        17: "seitsmeteist",
                        18: "kaheksateist",
                        19: "üheksateist",
                    }
                    ltext = COMPOUND_TEENS[lnum]
            ltext = inflect(ltext, options)
            return (fmt % (ltext, rtext), lnum * rnum)

    def to_cardinal(self, value, case='nominative', plural=False, prefer=None):
        case = NAME_TO_CASE[case]
        options = Options(False, case, plural, prefer)
        try:
            assert int(value) == value
        except (ValueError, TypeError, AssertionError):
            if case != NOM:
                raise NotImplementedError(
                    "Cases other than nominative are not implemented for "
                    "cardinal floating point numbers.")
            return self.to_cardinal_float(value)

        out = ""
        if value < 0:
            value = abs(value)
            out = self.negword

        #if value >= self.MAXVAL:
        #    raise OverflowError(self.errmsg_toobig % (value, self.MAXVAL))

        val = self.splitnum(value, options)
        words, num = self.clean(val, options)
        return self.title(out + words)

    def to_ordinal(self, value, case='nominative', plural=False, prefer=None):
        case = NAME_TO_CASE[case]
        options = Options(True, case, plural, prefer)

        self.verify_ordinal(value)
        if value >= self.MAXVAL:
            raise OverflowError(self.errmsg_toobig % (value, self.MAXVAL))

        val = self.splitnum(value, options)
        words, num = self.clean(val, options)
        return self.title(words)

    def to_ordinal_num(self, value, case='nominative', plural=False):
        case = NAME_TO_CASE[case]
        raise NotImplementedError

    def to_year(self, val, suffix=None, longval=True):
        suffix = suffix or ""
        if val < 0:
            val = abs(val)
            suffix = suffix or " ennen ajanlaskun alkua"
        return self.to_cardinal(val).replace(" ", "") + suffix

    def to_currency(self, val, currency="EUR", cents=True, separator=" ja",
                    adjective=False):
        return super(Num2Word_ET, self).to_currency(
            val, currency=currency, cents=cents, separator=separator,
            adjective=adjective)

    def splitnum(self, value, options):
        elems = self.ords if options.ordinal else self.cards
        for elem in elems:
            if elem > value:
                continue

            out = []
            if value == 0:
                div, mod = 1, 0
            else:
                div, mod = divmod(value, elem)

            if div == 1:
                out.append((elems[1], 1))
            else:
                if div == value:  # The system tallies, eg Roman Numerals
                    return [(div * elems[elem], div*elem)]
                out.append(self.splitnum(div, options))

            out.append((elems[elem], elem))

            if mod:
                out.append(self.splitnum(mod, options))

            return out

    def clean(self, val, options):
        out = val
        while len(val) != 1:
            out = []
            left, right = val[:2]
            if isinstance(left, tuple) and isinstance(right, tuple):
                out.append(self.merge(left, right, options))
                if val[2:]:
                    out.append(val[2:])
            else:
                for elem in val:
                    if isinstance(elem, list):
                        if len(elem) == 1:
                            out.append(elem[0])
                        else:
                            out.append(self.clean(elem, options))
                    else:
                        out.append(elem)
            val = out
        return out[0]