from gdb.domain.bank_account import BankAccount
from gdb.domain.savings_account import SavingsAccount
from gdb.domain.current_account import CurrentAccount
from gdb.domain.fixed_deposit_account import FixedDepositAccount


def test_abstract_class():

    try:
        BankAccount("ACC001", 5000.0)

        print("Test 1 (Abstract BankAccount): [FAIL]")

    except TypeError:
        print("Test 1 (Abstract BankAccount): [PASS]")


def test_savings_account():

    account = SavingsAccount(
        "SAV001",
        10000.0,
        5.0
    )

    assert account.get_account_type() == "Savings"
    assert account.calculate_interest() == 500.0

    print("Test 2 (Savings Account): [PASS]")


def test_current_account():

    account = CurrentAccount(
        "CUR001",
        10000.0
    )

    assert account.get_account_type() == "Current"
    assert account.calculate_interest() == 0.0

    print("Test 3 (Current Account): [PASS]")


def test_fixed_deposit_account():

    account = FixedDepositAccount(
        "FD001",
        10000.0,
        6.0,
        2
    )

    assert account.get_account_type() == "Fixed Deposit"
    assert account.calculate_interest() == 1200.0

    print("Test 4 (Fixed Deposit Account): [PASS]")


def test_template_method():

    accounts = [
        SavingsAccount("SAV002", 10000.0, 5.0),
        CurrentAccount("CUR002", 10000.0),
        FixedDepositAccount("FD002", 10000.0, 6.0, 2)
    ]

    print("\n=== Account Information ===")

    for account in accounts:
        account.display_account_info()


def main():

    print("=== Activity 9: Abstract Classes and Template Methods ===")

    test_abstract_class()
    test_savings_account()
    test_current_account()
    test_fixed_deposit_account()

    test_template_method()

    print("\nAll Activity 9 tests completed successfully!")


if __name__ == "__main__":
    main()