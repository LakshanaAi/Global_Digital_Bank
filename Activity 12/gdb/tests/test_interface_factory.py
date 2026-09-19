from gdb.domain.iaccount import IAccount
from gdb.domain.account_factory import AccountFactory


def test_all_account_types():

    account_types = [
        "savings",
        "current",
        "salary",
        "fixed"
    ]

    for account_type in account_types:

        account = AccountFactory.create_account(
            account_type,
            account_type.upper() + "001",
            10000.0
        )

        assert isinstance(account, IAccount)

        print(
            f"PASS: {account_type} account "
            f"created through AccountFactory"
        )


def test_interface_properties():

    account = AccountFactory.create_account(
        "salary",
        "SAL001",
        10000.0
    )

    # Access only through IAccount contract
    assert account.account_number == "SAL001"
    assert account.balance == 10000.0
    assert isinstance(account.get_account_type(), str)

    print("PASS: Interface properties")


def test_interface_deposit():

    account = AccountFactory.create_account(
        "salary",
        "SAL002",
        10000.0
    )

    result = account.deposit(2000.0)

    assert result is True
    assert account.balance == 12000.0

    print("PASS: Interface deposit")


def test_interface_withdraw():

    account = AccountFactory.create_account(
        "salary",
        "SAL003",
        10000.0
    )

    result = account.withdraw(3000.0)

    assert result is True
    assert account.balance == 7000.0

    print("PASS: Interface withdrawal")


def test_polymorphic_interface_operations():

    accounts = [
        AccountFactory.create_account(
            "savings", "SAV001", 10000.0
        ),
        AccountFactory.create_account(
            "current", "CUR001", 10000.0
        ),
        AccountFactory.create_account(
            "salary", "SAL004", 10000.0
        ),
        AccountFactory.create_account(
            "fixed", "FD001", 10000.0
        )
    ]

    for account in accounts:

        assert isinstance(account, IAccount)

        account.deposit(1000.0)

        assert account.balance == 11000.0

        interest = account.calculate_interest()

        assert isinstance(interest, float)

        account_type = account.get_account_type()

        assert isinstance(account_type, str)

        print(
            f"PASS: {account_type} account "
            f"operated through IAccount"
        )


def test_invalid_account_type():

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

    test_all_account_types()
    test_interface_properties()
    test_interface_deposit()
    test_interface_withdraw()
    test_polymorphic_interface_operations()
    test_invalid_account_type()

    print("\nAll Activity 12 tests completed successfully!")