from gdb.domain.account import Account

from gdb.exceptions.invalid_amount_exception import InvalidAmountException
from gdb.exceptions.insufficient_balance_exception import InsufficientBalanceException
from gdb.exceptions.inactive_account_exception import InactiveAccountException


def test_invalid_deposit():
    acc = Account(
        account_number="ACC6001",
        age=20,
        initial_balance=5000.0,
        pin="1234"
    )

    try:
        acc.deposit(-500.0)

        # No exception means the test failed
        print("Test 1 (Invalid Deposit): [FAIL]")

    except InvalidAmountException:
        print("Test 1 (Invalid Deposit): [PASS]")

    except Exception as e:
        print(
            f"Test 1 (Invalid Deposit): [FAIL] "
            f"Unexpected exception: {type(e).__name__}"
        )


def test_insufficient_balance():
    acc = Account(
        account_number="ACC6002",
        age=20,
        initial_balance=5000.0,
        pin="1234"
    )

    try:
        acc.withdraw(6000.0, "1234")

        # No exception means the test failed
        print("Test 2 (Insufficient Balance): [FAIL]")

    except InsufficientBalanceException:
        print("Test 2 (Insufficient Balance): [PASS]")

    except Exception as e:
        print(
            f"Test 2 (Insufficient Balance): [FAIL] "
            f"Unexpected exception: {type(e).__name__}"
        )


def test_inactive_account():
    acc = Account(
        account_number="ACC6003",
        age=20,
        initial_balance=5000.0,
        pin="1234"
    )

    # Make account inactive
    acc.suspend()

    try:
        acc.withdraw(1000.0, "1234")

        # No exception means the test failed
        print("Test 3 (Inactive Account): [FAIL]")

    except InactiveAccountException:
        print("Test 3 (Inactive Account): [PASS]")

    except Exception as e:
        print(
            f"Test 3 (Inactive Account): [FAIL] "
            f"Unexpected exception: {type(e).__name__}"
        )


def main():
    print("=== Activity 6: Testing Exceptions ===")

    test_invalid_deposit()
    test_insufficient_balance()
    test_inactive_account()

    print("All exception tests completed!")


if __name__ == "__main__":
    main()