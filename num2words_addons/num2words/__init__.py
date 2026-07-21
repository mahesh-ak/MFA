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

from . import (lang_AF, lang_AM, lang_AR, lang_AST, lang_AZ, lang_BE, lang_BG, lang_BN, lang_CA, lang_CE, lang_CEB, lang_CKB,
               lang_CS, lang_CY, lang_DA, lang_DE, lang_EL, lang_EN, lang_EN_IN, lang_ET,
               lang_EN_NG, lang_EO, lang_ES, lang_ES_CO, lang_ES_CR,
               lang_ES_GT, lang_ES_NI, lang_ES_VE, lang_FA, lang_FF, lang_FI, lang_FR,
               lang_FR_BE, lang_FR_CH, lang_FR_DZ, lang_GA, lang_GL, lang_HA, lang_HE, lang_HI, lang_HR, lang_HU,
               lang_HY, lang_ID, lang_IS, lang_IT, lang_JA, lang_JV, lang_KA, lang_KM, lang_KN, lang_KO, lang_KY,
               lang_KZ, lang_LG, lang_LO, lang_LT, lang_LV, lang_MI, lang_MK, lang_ML, lang_MN, lang_MY, lang_MR, lang_MS, lang_MT, lang_NE, lang_NL, lang_NO, lang_NY, lang_OM, lang_OR, lang_PA, lang_PL, lang_PS,
               lang_PT, lang_PT_BR, lang_RO, lang_RU, lang_SK, lang_SL, lang_SN, lang_SO,
               lang_SR, lang_SV, lang_SW, lang_TA, lang_TE, lang_TET, lang_TG, lang_TH, lang_TR,
               lang_UK, lang_UR, lang_UZ, lang_VI, lang_WO, lang_XH, lang_YO, lang_ZH, lang_ZH_CN, lang_ZH_HK, lang_ZH_TW, lang_ZU)

CONVERTER_CLASSES = {
    'af': lang_AF.Num2Word_AF(),
    'am': lang_AM.Num2Word_AM(),
    'ar': lang_AR.Num2Word_AR(),
    'ast': lang_AST.Num2Word_AST(),
    'az': lang_AZ.Num2Word_AZ(),
    'be': lang_BE.Num2Word_BE(),
    'bg': lang_BG.Num2Word_BG(),
    'bn': lang_BN.Num2Word_BN(),
    'ca': lang_CA.Num2Word_CA(),
    'ce': lang_CE.Num2Word_CE(),
    'ceb': lang_CEB.Num2Word_CEB(),
    'ckb': lang_CKB.Num2Word_CKB(),
    'cs': lang_CS.Num2Word_CS(),
    'cy': lang_CY.Num2Word_CY(),
    'da': lang_DA.Num2Word_DA(),
    'de': lang_DE.Num2Word_DE(),
    'el': lang_EL.Num2Word_EL(),
    'en': lang_EN.Num2Word_EN(),
    'en_IN': lang_EN_IN.Num2Word_EN_IN(),
    'en_NG': lang_EN_NG.Num2Word_EN_NG(),
    'et': lang_ET.Num2Word_ET(),
    'eo': lang_EO.Num2Word_EO(),
    'es': lang_ES.Num2Word_ES(),
    'es_CO': lang_ES_CO.Num2Word_ES_CO(),
    'es_CR': lang_ES_CR.Num2Word_ES_CR(),
    'es_GT': lang_ES_GT.Num2Word_ES_GT(),
    'es_NI': lang_ES_NI.Num2Word_ES_NI(),
    'es_VE': lang_ES_VE.Num2Word_ES_VE(),
    'fa': lang_FA.Num2Word_FA(),
    'ff': lang_FF.Num2Word_FF(),
    'fi': lang_FI.Num2Word_FI(),
    'fr': lang_FR.Num2Word_FR(),
    'fr_BE': lang_FR_BE.Num2Word_FR_BE(),
    'fr_CH': lang_FR_CH.Num2Word_FR_CH(),
    'fr_DZ': lang_FR_DZ.Num2Word_FR_DZ(),
    'ga': lang_GA.Num2Word_GA(),
    'gl': lang_GL.Num2Word_GL(),
    'ha': lang_HA.Num2Word_HA(),
    'he': lang_HE.Num2Word_HE(),
    'hi': lang_HI.Num2Word_HI(),
    'hr': lang_HR.Num2Word_HR(),
    'hu': lang_HU.Num2Word_HU(),
    'hy': lang_HY.Num2Word_HY(),
    'id': lang_ID.Num2Word_ID(),
    'is': lang_IS.Num2Word_IS(),
    'it': lang_IT.Num2Word_IT(),
    'ja': lang_JA.Num2Word_JA(),
    'jv': lang_JV.Num2Word_JV(),
    'ka': lang_KA.Num2Word_KA(),
    'km': lang_KM.Num2Word_KM(),
    'kn': lang_KN.Num2Word_KN(),
    'ko': lang_KO.Num2Word_KO(),
    'ky': lang_KY.Num2Word_KY(),
    'kz': lang_KZ.Num2Word_KZ(),
    'lg': lang_LG.Num2Word_LG(),
    'lo': lang_LO.Num2Word_LO(),
    'lt': lang_LT.Num2Word_LT(),
    'lv': lang_LV.Num2Word_LV(),
    'mi': lang_MI.Num2Word_MI(),
    'mk': lang_MK.Num2Word_MK(),
    'ml': lang_ML.Num2Word_ML(),
    'mn': lang_MN.Num2Word_MN(),
    'mr': lang_MR.Num2Word_MR(),
    'ms': lang_MS.Num2Word_MS(),
    'mt': lang_MT.Num2Word_MT(),
    'my': lang_MY.Num2Word_MY(),
    'ne': lang_NE.Num2Word_NE(),
    'nl': lang_NL.Num2Word_NL(),
    'no': lang_NO.Num2Word_NO(),
    'ny': lang_NY.Num2Word_NY(),
    'om': lang_OM.Num2Word_OM(),
    'or': lang_OR.Num2Word_OR(),
    'pa': lang_PA.Num2Word_PA(),
    'pl': lang_PL.Num2Word_PL(),
    'pt': lang_PT.Num2Word_PT(),
    'ps': lang_PS.Num2Word_PS(),
    'pt_BR': lang_PT_BR.Num2Word_PT_BR(),
    'ro': lang_RO.Num2Word_RO(),
    'ru': lang_RU.Num2Word_RU(),
    'sk': lang_SK.Num2Word_SK(),
    'sl': lang_SL.Num2Word_SL(),
    'sn': lang_SN.Num2Word_SN(),
    'so': lang_SO.Num2Word_SO(),
    'sr': lang_SR.Num2Word_SR(),
    'sv': lang_SV.Num2Word_SV(),
    'sw': lang_SW.Num2Word_SW(),
    'ta': lang_TA.Num2Word_TA(),
    'te': lang_TE.Num2Word_TE(),
    'tet': lang_TET.Num2Word_TET(),
    'tg': lang_TG.Num2Word_TG(),
    'th': lang_TH.Num2Word_TH(),
    'tr': lang_TR.Num2Word_TR(),
    'uk': lang_UK.Num2Word_UK(),
    'ur': lang_UR.Num2Word_UR(),
    'uz': lang_UZ.Num2Word_UZ(),
    'vi': lang_VI.Num2Word_VI(),
    'wo': lang_WO.Num2Word_WO(),
    'xh': lang_XH.Num2Word_XH(),
    'yo': lang_YO.Num2Word_YO(),
    'zh': lang_ZH.Num2Word_ZH(),
    'zh_CN': lang_ZH_CN.Num2Word_ZH_CN(),
    'zh_HK': lang_ZH_HK.Num2Word_ZH_HK(),
    'zh_TW': lang_ZH_TW.Num2Word_ZH_TW(),
    'zu': lang_ZU.Num2Word_ZU(),
}

CONVERTES_TYPES = ['cardinal', 'ordinal', 'ordinal_num', 'year', 'currency']


def num2words(number, ordinal=False, lang='en', to='cardinal', **kwargs):
    # We try the full language first
    if lang not in CONVERTER_CLASSES:
        # ... and then try only the first 2 letters
        lang = lang[:2]
    if lang not in CONVERTER_CLASSES:
        raise NotImplementedError()
    converter = CONVERTER_CLASSES[lang]

    if isinstance(number, str):
        number = converter.str_to_number(number)

    # backwards compatible
    if ordinal:
        to = 'ordinal'

    if to not in CONVERTES_TYPES:
        raise NotImplementedError()

    return getattr(converter, 'to_{}'.format(to))(number, **kwargs)
