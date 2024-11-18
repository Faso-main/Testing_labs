import unittest
from Laba4 import *

class TestLaba4f(unittest.TestCase):

    def test_create_with_valid_number(self):
        laba = Laba4(123)
        self.assertEqual(laba.add_time(), 'Ваше число: 123 руб.')

    def test_create_with_boundary_number(self):
        laba = Laba4(999)
        self.assertEqual(laba.add_time(), 'Ваше число: 999 руб.')

    def test_create_with_invalid_number(self):
        with self.assertRaises(ValueError) as context:
            Laba4(1000)
        self.assertEqual(str(context.exception), "Число не должно быть больше 999.")

    def test_add_time_with_valid_number(self):
        laba = Laba4(456)
        self.assertEqual(laba.add_time(), 'Ваше число: 456 руб.')


if __name__ == '__main__':
    unittest.main()
