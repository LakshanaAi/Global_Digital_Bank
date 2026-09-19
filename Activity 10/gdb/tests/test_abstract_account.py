from gdb.domain.bank_account import BankAccount
from gdb.domain.savings_account import SavingsAccount
from gdb.domain.current_account import CurrentAccount
from gdb.domain.fixed_deposit_account import FixedDepositAccount


def test_interest_calculations():
    savings = SavingsAccount("S001", 10000.0, 5.0)
    current = CurrentAccount("C001", 10000.0)
    fixed_deposit = FixedDepositAccount("FD001", 10000.0, 6.0, 2)

    assert savings.calculate_interest() == 500.0
    assert current.calculate_interest() == 0.0
    assert fixed_deposit.calculate_interest() == 1200.0

    print("PASS: Interest calculations")


def test_minimum_balance_assertions():
    savings = SavingsAccount("S002", 5000.0, 5.0)
    current = CurrentAccount("C002", 5000.0)
    fixed_deposit = FixedDepositAccount("FD002", 5000.0, 6.0, 2)

    assert savings._balance >= 0
    assert current._balance >= 0
    assert fixed_deposit._balance >= 0

    print("PASS: Minimum balance assertions")


def test_polymorphic_operations():
    accounts = [
        SavingsAccount("S003", 10000.0, 5.0),
        CurrentAccount("C003", 10000.0),
        FixedDepositAccount("FD003", 10000.0, 6.0, 2)
    ]

    for account in accounts:
        assert isinstance(account, BankAccount)
        assert isinstance(account.calculate_interest(), float)
        assert isinstance(account.get_account_type(), str)

    print("PASS: Polymorphic operations")


def test_abstract_class():
    try:
        BankAccount("B001", 10000.0)
        print("FAIL: BankAccount should not be instantiated")
    except TypeError:
        print("PASS: BankAccount is abstract")


def test_display_account_info():
    accounts = [
        SavingsAccount("S004", 10000.0, 5.0),
        CurrentAccount("C004", 10000.0),
        FixedDepositAccount("FD004", 10000.0, 6.0, 2)
    ]

    for account in accounts:
        account.display_account_info()

    print("PASS: Display account information")


if __name__ == "__main__":
    test_interest_calculations()
    test_minimum_balance_assertions()
    test_polymorphic_operations()
    test_abstract_class()
    test_display_account_info()

    print("\nAll Activity 10 tests completed successfully!")