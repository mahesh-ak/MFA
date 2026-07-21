from unittest import TestCase

from num2words import num2words


class Num2WordsKATest(TestCase):

    def test_cardinal(self):
        self.assertEqual(
            num2words(0, lang='ka', to='cardinal'),
            'ნულოვანი'
        )
        self.assertEqual(
            num2words(1, lang='ka', to='cardinal'),
            'პირველი'
        )
        self.assertEqual(
            num2words(13, lang='ka', to='cardinal'),
            'მეცამეტე'
        )
        self.assertEqual(
            num2words(23, lang='ka', to='cardinal'),
            'ოცდამესამე'
        )
        self.assertEqual(
            num2words(12, lang='ka', to='cardinal'),
            'მეთორმეტე'
        )
        self.assertEqual(
            num2words(113, lang='ka', to='cardinal'),
            'ას მეცამეტე'
        )
        self.assertEqual(
            num2words(103, lang='ka', to='cardinal'),
            'ას მესამე'
        )

    def test_cardinal(self):
        self.assertEqual(num2words(130000, lang='ka'), "ას ოცდაათი ათასი")
        self.assertEqual(num2words(242, lang='ka'), "ორას ორმოცდაორი")
        self.assertEqual(num2words(800, lang='ka'), "რვაასი")
        self.assertEqual(num2words(-203, lang='ka'), "მინუს ორას სამი")
        self.assertEqual(
            num2words(1234567890, lang='ka'),
            "ერთი მილიარდი ორას ოცდათოთხმეტი მილიონი "
            "ხუთას სამოცდაშვიდი ათასი რვაას ოთხმოცდაათი"
        )

#    def test_year(self):
#        self.assertEqual(num2words(1398, lang='ka', to='year'),
#                         "ათას სამას ოთხმოცდათვრამეტი")
#        self.assertEqual(num2words(1399, lang='ka', to='year'),
#                         "ათას სამას ოთხმოცდაცხრამეტი")
#        self.assertEqual(
#            num2words(1400, lang='ka', to='year'),
#            "ათას ოთხასი"
#        )

#    def test_currency(self):
#        self.assertEqual(
#            num2words(1000, lang='ka', to='currency'),
#            'ათასი ლარი'
#        )
#        self.assertEqual(
#            num2words(1500000, lang='ka', to='currency'),
#            'ერთი მილიონი ხუთასი ათასი ლარი'
#        )

 
    def test_overflow(self):
        with self.assertRaises(OverflowError):
            num2words("1000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "00000000000000000000000000000000")