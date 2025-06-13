import unittest
import HtmlTestRunner

class TestOperations(unittest.TestCase):

    # Addition
    def test_addition_positive_ints(self):
        self.assertEqual(2 + 3, 5)

    def test_addition_negative_ints(self):
        self.assertEqual(-2 + -3, -5)

    def test_addition_mixed_signs(self):
        self.assertEqual(-2 + 3, 1)

    def test_addition_floats(self):
        self.assertEqual(1.5 + 2.5, 4.0)

    # Subtraction
    def test_subtraction_positive_ints(self):
        self.assertEqual(5 - 2, 3)

    def test_subtraction_negative_ints(self):
        self.assertEqual(-5 - -2, -3)

    def test_subtraction_mixed_signs(self):
        self.assertEqual(-5 - 2, -7)

    def test_subtraction_floats(self):
        self.assertEqual(5.5 - 2.5, 3.0)

    # Multiplication
    def test_multiplication_positive_ints(self):
        self.assertEqual(4 * 3, 12)

    def test_multiplication_negative_ints(self):
        self.assertEqual(-4 * -3, 12)

    def test_multiplication_mixed_signs(self):
        self.assertEqual(-4 * 3, -12)

    def test_multiplication_floats(self):
        self.assertEqual(2.0 * 2.5, 5.0)

    def test_multiplication_with_zero(self):
        self.assertEqual(0 * 999, 0)

    # Division
    def test_division_positive_ints(self):
        self.assertEqual(10 / 2, 5.0)

    def test_division_negative_ints(self):
        self.assertEqual(-10 / -2, 5.0)

    def test_division_mixed_signs(self):
        self.assertEqual(-10 / 2, -5.0)

    def test_division_floats(self):
        self.assertEqual(7.5 / 2.5, 3.0)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            _ = 5 / 0


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output='reports',
            report_name='OperatorTests',
            report_title='Arithmetic Operator Tests',
            combine_reports=True,
            verbosity=2
        )
    )