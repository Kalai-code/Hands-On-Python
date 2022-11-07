import unittest
import FizzBuzz

class FizzBuzzTests(unittest.TestCase):

    def test_FizzBuzz(self):
        self.assertEqual(FizzBuzz.FizzBuzzOutput(15),"FizzBuzz")
        self.assertEqual(FizzBuzz.FizzBuzzOutput(6),"Fizz")
        self.assertEqual(FizzBuzz.FizzBuzzOutput(10),"Buzz")
        self.assertEqual(FizzBuzz.FizzBuzzOutput(14),"14")


if __name__ == "__main__":
    unittest.main()