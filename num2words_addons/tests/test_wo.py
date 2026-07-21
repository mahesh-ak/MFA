from unittest import TestCase

from num2words import num2words


class Num2WordsWOTest(TestCase):
    maxDiff = None
    def test_cardinal_basic(self):
        self.assertEqual(
            num2words(0, lang='wo'),
            'tus'
        )
        self.assertEqual(
            num2words(1, lang='wo'),
            'benn'
        )
        self.assertEqual(
            num2words(9, lang='wo'),
            'juróom-ñeent'
        )

    def test_cardinal_under_100(self):
        self.assertEqual(
            num2words(10, lang='wo'),
            'fukk'
        )
        self.assertEqual(
            num2words(13, lang='wo'),
            'fukk ak ñett'
        )
        self.assertEqual(
            num2words(20, lang='wo'),
            'ñaar-fukk'
        )
        self.assertEqual(
            num2words(23, lang='wo'),
            'ñaar-fukk ak ñett'
        )
        self.assertEqual(
            num2words(40, lang='wo'),
            'ñaar ñaar-fukk'
        )

    def test_cardinal_hundreds(self):
        self.assertEqual(
            num2words(100, lang='wo'),
            'téeméer'
        )
        self.assertEqual(
            num2words(103, lang='wo'),
            'téeméer ak ñett'
        )
        self.assertEqual(
            num2words(242, lang='wo'),
            'ñaar téeméer ak ñaar ñaar-fukk ak ñaar'
        )
        self.assertEqual(
            num2words(800, lang='wo'),
            'juróom-ñett téeméer'
        )

    def test_cardinal_thousands(self):
        self.assertEqual(
            num2words(130000, lang='wo'),
            'téeméer ak ñaar-fukk ak fukk junni'
        )
        self.assertEqual(
            num2words(-203, lang='wo'),
            'minus ñaar téeméer ak ñett'
        )

    def test_large_number(self):
        self.assertEqual(
            num2words(1234567890, lang='wo'),
            'benn milyaar ak ñaar téeméer ak ñaar-fukk ak fukk ak ñeent milyoŋ ak juróom téeméer ak ñett ñaar-fukk ak juróom-ñaar junni ak juróom-ñett téeméer ak ñeent ñaar-fukk ak fukk'
        )