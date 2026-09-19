from gdb.domain.account import Account

from gdb.exceptions.account_exception import AccountException
from gdb.exceptions.invalid_amount_exception import InvalidAmountException
from gdb.exceptions.insufficient_balance_exception import InsufficientBalanceException
from gdb.exceptions.inactive_account_exception import InactiveAccountException
from gdb.exceptions.invalid_pin_exception import InvalidPinException
from gdb.exceptions.minimum_balance_violation_exception import (
    MinimumBalanceViolationException
)


def test_invalid_amount():
    try:
        Account(
            account_number="ACC1001",
            age=20,
            initial_balance=-1000.0,
            pin="1234"
        )
        print("Test 1 (Invalid Initial Amount): [FAIL]")
    except InvalidAmountException:
        print("Test 1 (Invalid Initial Amount): [PASS]")


def test_invalid_pin():
    try:
        Account(
            account_number="ACC1002",
            age=20,
            initial_balance=5000.0,
            pin="123"
        )
        print("Test 2 (Invalid PIN): [FAIL]")
    except InvalidPinException:
        print("Test 2 (Invalid PIN): [PASS]")


def test_wrong_pin():
    account = Account(
        account_number="ACC1003",
        age=20,
        initial_balance=5000.0,
        pin="1234"
    )

    try:
        account.validate_pin("9999")
        print("Test 3 (Wrong PIN): [FAIL]")
    except InvalidPinException:
        print("Test 3 (Wrong PIN): [PASS]")


def test_insufficient_balance():
    account = Account(
        account_number="ACC1004",
        age=20,
        initial_balance=5000.0,
        pin="1234"
    )

    try:
        account.withdraw(6000.0, "1234")
        print("Test 4 (Insufficient Balance): [FAIL]")
    except InsufficientBalanceException:
        print("Test 4 (Insufficient Balance): [PASS]")


def test_invalid_amount():
    account = Account(
        account_number="ACC1005",
        age=20,
        initial_balance=5000.0,
        pin="1234"
    )

    try:
        account.deposit(-500.0)
        print("Test 5 (Negative Deposit): [FAIL]")
    except InvalidAmountException:
        print("Test 5 (Negative Deposit): [PASS]")


def test_inactive_account():
    account = Account(
        account_number="ACC1006",
        age=20,
        initial_balance=5000.0,
        pin="1234"
    )

    account.suspend()

    try:
        account.deposit(1000.0)
        print("Test 6 (Inactive Account): [FAIL]")
    except InactiveAccountException:
        print("Test 6 (Inactive Account): [PASS]")


def test_successful_transaction():
    account = Account(
        account_number="ACC1007",
        age=20,
        initial_balance=5000.0,
        pin="1234"
    )

    try:
        account.deposit(1000.0)
        account.withdraw(1000.0, "1234")

        if account.get_balance() == 5000.0:
            print("Test 7 (Successful Transactions): [PASS]")
        else:
            print("Test 7 (Successful Transactions): [FAIL]")

    except AccountException:
        print("Test 7 (Successful Transactions): [FAIL]")


def main():
    print("=== Activity 5: Custom Account Exceptions Test ===")

    test_invalid_amount()
    test_invalid_pin()
    test_wrong_pin()
    test_insufficient_balance()
    test_invalid_amount()
    test_inactive_account()
    test_successful_transaction()

    print("All exception tests completed!")


if __name__ == "__main__":
    main()