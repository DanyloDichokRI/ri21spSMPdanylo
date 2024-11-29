import unittest


class Calculator:


    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Ділення на нуль!")
        return a / b


class TestCalculator(unittest.TestCase):
    def setUp(self):

        self.calc = Calculator()


    def test_addition(self):
        # Позитивні числа
        self.assertEqual(self.calc.add(2, 3), 5)
        # Від'ємні числа
        self.assertEqual(self.calc.add(-2, -3), -5)
        # Комбінація позитивного і негативного числа
        self.assertEqual(self.calc.add(-2, 3), 1)


    def test_subtraction(self):
        # Позитивні числа
        self.assertEqual(self.calc.subtract(5, 3), 2)
        # Від'ємні числа
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        # Комбінація позитивного і негативного числа
        self.assertEqual(self.calc.subtract(3, -2), 5)


    def test_multiplication(self):
        # Позитивні числа
        self.assertEqual(self.calc.multiply(3, 4), 12)
        # Від'ємні числа
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        # Множення на нуль
        self.assertEqual(self.calc.multiply(3, 0), 0)


    def test_division(self):
        # Позитивні числа
        self.assertEqual(self.calc.divide(10, 2), 5)
        # Від'ємні числа
        self.assertEqual(self.calc.divide(-10, 2), -5)
        # Комбінація позитивного і негативного числа
        self.assertEqual(self.calc.divide(10, -2), -5)
        # Ділення на одиницю
        self.assertEqual(self.calc.divide(10, 1), 10)


    def test_division_by_zero(self):
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        self.assertTrue("Ділення на нуль!" in str(context.exception))


if __name__ == '__main__':
    unittest.main()
