from gdb.domain.account import Account


def test_pin_authentication():
    account = Account(
        account_number="ACC1001",
        age=20,
        initial_balance=5000.0,
        pin="1234"
    )

    # Correct PIN
    assert account.validate_pin("1234") is True

    # Wrong PIN
    assert account.validate_pin("9999") is False

    # None PIN
    assert account.validate_pin(None) is False


def test_active_transactions():
    account = Account(
        account_number="ACC1002",
        age=20,
        initial_balance=5000.0,
        pin="1234"
    )

    # Account should initially be ACTIVE
    assert account.get_status().lower() == "active"

    # Valid deposit
    assert account.deposit(1000.0) is True
    assert account.get_balance() == 6000.0

    # Valid withdrawal
    assert account.withdraw(1000.0, "1234") is True
    assert account.get_balance() == 5000.0


def test_inactive_status_invariant():
    account = Account(
        account_number="ACC1003",
        age=20,
        initial_balance=5000.0,
        pin="1234"
    )

    # Change account status to Inactive
    account._status = "Inactive"

    # Deposit should be blocked
    assert account.deposit(1000.0) is False

    # Withdrawal should be blocked
    assert account.withdraw(1000.0, "1234") is False

    # Balance should remain unchanged
    assert account.get_balance() == 5000.0


def main():
    test_pin_authentication()
    print("Test 1 (PIN Authentication): [PASS]")

    test_active_transactions()
    print("Test 2 (Active Transactions): [PASS]")

    test_inactive_status_invariant()
    print("Test 3 (Inactive Status Blocks Transactions): [PASS]")

    print("All Activity 4 tests passed successfully!")


if __name__ == "__main__":
    main()