import unittest

from FibonacciRecursivo import fibonacci


class TestFibonacci(unittest.TestCase):

    def test_fibonacci_5(self):
        resultado = fibonacci(5)
        self.assertEqual(resultado,5)
    
    def test_fibonacci_13(self):
        resultado = fibonacci(13)
        self.assertEqual(resultado,233)

    def test_fibonacci_24(self):
        resultado = fibonacci(24)
        self.assertEqual(resultado,46368)
    
    def test_fibonacci_37(self):
        resultado = fibonacci(37)
        self.assertEqual(resultado,24157817)
    
            


unittest.main()