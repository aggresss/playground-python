# calcalatorTest.py

from unittest import TestCase
from calculator import Calculator
import unittest


class calculatorTest(TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_sum(self):
        answer = self.calc.sum(2, 4)
        self.assertEqual(answer, 6)


def suite():
    suite = unittest.TestSuite()
    suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(calculatorTest)
    )

    return suite


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite())
