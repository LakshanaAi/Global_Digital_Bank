from gdb.domain.Account import Account

def main():
    print("=== Activity 3: Enhanced Account Test ===")

    # Create account
    account = Account(
        account_number="ACC1001",
        age=20,
        initial_balance=5000.0,
        pin="1234"
    )

    print(
        f"Initial Balance: Rs {account.get_balance()} "
        f"| Status: {account.get_status()}"
    )

    # Withdraw with correct PIN
    result = account.withdraw(1000.0, "1234")

    print(
        f"Withdraw with correct PIN: "
        f"{'SUCCESS' if result else 'FAILED'} "
        f"| Balance: Rs {account.get_balance()}"
    )

    # Withdraw with wrong PIN
    result = account.withdraw(1000.0, "9999")

    print(
        f"Withdraw with wrong PIN: "
        f"{'SUCCESS' if result else 'FAILED'} "
        f"| Balance: Rs {account.get_balance()}"
    )

    # Suspend account
    account.suspend()
    print("Account Suspended.")

    # Try withdrawal on suspended account
    result = account.withdraw(1000.0, "1234")

    print(
        f"Withdraw on SUSPENDED account: "
        f"{'SUCCESS' if result else 'FAILED'} "
        f"| Balance: Rs {account.get_balance()}"
    )

    # Reactivate account
    account.activate()
    print("Account Re-Activated.")

    # Change PIN
    # Since the provided activity only requires PIN validation,
    # we directly demonstrate the existing PIN after reactivation.
    result = account.withdraw(1000.0, "1234")

    print(
        f"Withdraw after re-activation: "
        f"{'SUCCESS' if result else 'FAILED'} "
        f"| Balance: Rs {account.get_balance()}"
    )


if __name__ == "__main__":
    main()