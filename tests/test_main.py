import unittest
from main import satisfies

class Tests(unittest.TestCase):
    def test_comparators(self):
        self.assertTrue(satisfies("1.5.0", ">=1.2.0 <2.0.0"))
        self.assertFalse(satisfies("2.0.0", ">=1.2.0 <2.0.0"))
    def test_caret_zero(self):
        self.assertTrue(satisfies("0.2.9", "^0.2.3"))
        self.assertFalse(satisfies("0.3.0", "^0.2.3"))
        self.assertTrue(satisfies("1.9.0", "^1.2.3"))
        self.assertFalse(satisfies("2.0.0", "^1.2.3"))
    def test_tilde_wildcard(self):
        self.assertTrue(satisfies("1.2.9", "~1.2.3"))
        self.assertFalse(satisfies("1.3.0", "~1.2.3"))
        self.assertTrue(satisfies("1.8.0", "1.x"))
    def test_or(self):
        self.assertTrue(satisfies("3.1.2", "^1.0.0 || ^3.1.0"))

if __name__ == "__main__":
    unittest.main()
