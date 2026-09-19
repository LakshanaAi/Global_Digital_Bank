from gdb.domain.iaccount import IAccount
from gdb.domain.salary_account import SalaryAccount
from gdb.domain.account_factory import AccountFactory


def test_salary_account_creation():

    account = AccountFactory.create_account(
        "salary",
        "SAL001",
        10000.0
    )

    assert isinstance(account, IAccount)
    assert isinstance(account, SalaryAccount)

    print("PASS: Salary account created through factory")


def test_account_properties():

    account = AccountFactory.create_account(
        "salary",
        "SAL002",
        10000.0
    )

    assert account.account_number == "SAL002"
    assert account.balance == 10000.0
    assert account.get_account_type() == "Salary"

    print("PASS: Account properties")


def test_deposit():

    account = AccountFactory.create_account(
        "salary",
        "SAL003",
        10000.0
    )

    result = account.deposit(2000.0)

    assert result is True
    assert account.balance == 12000.0

    print("PASS: Deposit through interface")


def test_withdraw():

    account = AccountFactory.create_account(
        "salary",
        "SAL004",
        10000.0
    )

    result = account.withdraw(3000.0)

    assert result is True
    assert account.balance == 7000.0

    print("PASS: Withdrawal through interface")


def test_factory_invalid_type():

    try:
        AccountFactory.create_account(
            "unknown",
            "ACC001",
            5000.0
        )

        print("FAIL: Invalid account type accepted")

    except ValueError:
        print("PASS: Invalid account type rejected")


if __name__ == "__main__":

    test_salary_account_creation()
    test_account_properties()
    test_deposit()
    test_withdraw()
    test_factory_invalid_type()

    print("\nAll Activity 11 tests completed successfully!")