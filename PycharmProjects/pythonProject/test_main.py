import unittest
from io import StringIO
from unittest.mock import patch

from main import (BankAccount)  # Замените "your_module" на имя вашего модуля


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("Джокоев Нурдин")

    def test_deposit(self):
        self.account.deposit(100)
        self.assertEqual(self.account.balance, 100)

    def test_withdraw(self):
        self.account.deposit(100)
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 50)

    def test_display_balance(self):
        captured_output = StringIO()
        expected_output = "Текущий баланс: 0.00 US Dollar\n"
        with patch('sys.stdout', new=captured_output):
            self.account.display_balance()
            self.assertEqual(captured_output.getvalue(), expected_output)

    def test_add_transaction(self):
        self.account.add_transaction(100, "Test transaction")
        self.assertEqual(len(self.account.expected_transactions), 1)

    def test_set_account_limit(self):
        self.account.set_account_limit(500)
        self.assertEqual(self.account.account_limit, 500)

    def test_apply_transactions(self):
        self.account.add_transaction(100, "Test transaction")
        self.account.apply_transactions()
        self.assertEqual(self.account.balance, 100)

    def test_show_transaction_statistics(self):
        self.account.add_transaction(100, "Test transaction 1")
        self.account.add_transaction(200, "Test transaction 2")
        captured_output = StringIO()
        expected_output = "Статистика по ожидаемым пополнениям:\n100.00 US Dollar: 1 платеж(а)\n200.00 US Dollar: 1 платеж(а)\n"
        with patch('sys.stdout', new=captured_output):
            self.account.show_transaction_statistics()
            self.assertEqual(captured_output.getvalue(), expected_output)

    # Добавьте другие тесты по мере необходимости


if __name__ == '__main__':
    unittest.main()
