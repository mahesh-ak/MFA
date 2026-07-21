from unittest import TestCase

from num2words import num2words

class Num2WordsYOTest(TestCase):

    def test_cardinal(self):
        self.assertEqual(
            num2words(0, lang='yo', to='cardinal'),
            'odo'
        )
        self.assertEqual(
            num2words(1, lang='yo', to='cardinal'),
            'ọ̀kan'
        )
        self.assertEqual(
            num2words(13, lang='yo', to='cardinal'),
            'mẹ́tàlá'
        )
        self.assertEqual(
            num2words(23, lang='yo', to='cardinal'),
            'ogún mẹ́ta'
        )
        self.assertEqual(
            num2words(12, lang='yo', to='cardinal'),
            'méjìlá'
        )
        self.assertEqual(
            num2words(113, lang='yo', to='cardinal'),
            'ọgọ́rùn-ún mẹ́tàlá'
        )
        self.assertEqual(
            num2words(103, lang='yo', to='cardinal'),
            'ọgọ́rùn-ún mẹ́ta'
        )

    def test_cardinal_large_numbers(self):
        self.assertEqual(num2words(130000, lang='yo'), "ọgọ́rùn-ún ọgbọ̀n ẹgbẹ̀rún")
        self.assertEqual(num2words(242, lang='yo'), "igba ogójì méjì")
        self.assertEqual(num2words(800, lang='yo'), "ẹgbẹ̀rin")
        self.assertEqual(num2words(-203, lang='yo'), "kò igba mẹ́ta")
        self.assertEqual(
            num2words(1234567890, lang='yo'),
            "bílíọ̀nù igba ọgbọ̀n mẹ́rin mílíọ̀nù ẹ̀ẹ́dẹ́gbẹ̀ta mẹ́tàdín-àádọ́rin ẹgbẹ̀rún ẹgbẹ̀rin àádọ́rùn-ún"
        )
        