import unittest
from prime import prime
class Testfactorial(unittest.TestCase):
    def test_prime1(self):
        result = prime(13)
        self.assertEqual(result,1)
    def test_prime2(self):
        result = prime(19)
        self.assertEqual(result,1)
    def test_prime3(self):
        result = prime(3)
        self.assertEqual(result,1)
    def test_prime4(self):
        result = prime(6)
        self.assertEqual(result,1)
    def test_prime5(self):
        result = prime(11)
        self.assertEqual(result,0)

if __name__ == '__main__':
    unittest.main()