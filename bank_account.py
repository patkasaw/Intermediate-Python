import unittest

class BankAccount:
  def __init__(self, initial_balance=0):
    self.balance = initial_balance

  def deposit(self, amount):
    if amount <= 0:
      raise ValueError('Deposit amount must be positive')
    self.balance += amount

  def withdraw(self, amount):
    if amount <= 0:
      raise ValueError('Withdrawal amount must be positive')
    if amount > self.balance:
      raise ValueError('Insufficient funds')
    self.balance -= amount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.bank_account = BankAccount(100)
    
    def tearDown(self):
        self.bank_account = None

    def test_initial_balance(self):
        self.assertEqual(self.bank_account.balance, 100)

    def test_deposit_positive_amount(self):
        self.bank_account.deposit(50)
        self.assertEqual(self.bank_account.balance, 150)
      
    def test_deposit_zero_amount(self):
        with self.assertRaises(ValueError):
            self.bank_account.deposit(0)
    
    def test_deposit_negative_amount(self):
       with self.assertRaises(ValueError):
          self.bank_account.deposit(-40)

    def test_withdraw_sufficent_funds(self):
       self.bank_account.withdraw(30)
       self.assertEqual(self.bank_account.balance, 70)

    def test_withdraw_insufficent_funds(self):
       with self.assertRaises(ValueError):
          self.bank_account.withdraw(200)

    def test_withdraw_zero_amount(self):
       with self.assertRaises(ValueError):
          self.bank_account.withdraw(0)

    def test_withdraw_negative_amount(self):
       with self.assertRaises(ValueError):
          self.bank_account.withdraw(-50)


if __name__ == '__main__':
    unittest.main()
