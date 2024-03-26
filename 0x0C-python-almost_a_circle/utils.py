import unittest
from tests import *

class TestStringUtils(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(StringUtils.is_palindrome("racecar"))
        self.assertTrue(StringUtils.is_palindrome("level"))
        self.assertFalse(StringUtils.is_palindrome("hello"))
        self.assertTrue(StringUtils.is_palindrome(""))  # Edge case: empty string

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("123456789", 1000.0)

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 1000.0)

    def test_deposit(self):
        self.account.deposit(500.0)
        self.assertEqual(self.account.get_balance(), 1500.0)

    def test_withdraw_sufficient_balance(self):
        self.account.withdraw(500.0)
        self.assertEqual(self.account.get_balance(), 500.0)

    def test_withdraw_insufficient_balance(self):
        with unittest.mock.patch('builtins.print') as mock_print:
            self.account.withdraw(1500.0)
            mock_print.assert_called_once_with("Insufficient balance")
        self.assertEqual(self.account.get_balance(), 1000.0)  # Balance should remain unchanged

class TestAddFunction(unittest.TestCase):
    def test_add_integers(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-10, 5), -5)
        self.assertEqual(add(0, 0), 0)

    def test_add_floats(self):
        self.assertAlmostEqual(add(3.5, 2.5), 6.0)
        self.assertAlmostEqual(add(-2.5, 1.5), -1.0)

if __name__ == '__main__':
    unittest.main()
