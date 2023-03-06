# unittest for akarilib.test.py

import unittest
from akarilib import akarilib

class TestAkariLib(unittest.TestCase):
    # exist method
    def test_exist(self):
        self.assertTrue(akarilib.rsaConnection)
        self.assertTrue(akarilib.passwordConnection)
        self.assertTrue(akarilib.disconnect)
        self.assertTrue(akarilib.run)
        self.assertTrue(akarilib.sudo)
        self.assertTrue(akarilib.put)
        self.assertTrue(akarilib.get)
        self.assertTrue(akarilib.putFiles)
        self.assertTrue(akarilib.getFiles)

if __name__ == "__main__":
    unittest.main()
