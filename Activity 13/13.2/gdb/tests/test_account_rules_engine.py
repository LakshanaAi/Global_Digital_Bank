from gdb.domain.account_rules_engine import AccountRulesEngine


def test_minimum_balance_rules():

    assert AccountRulesEngine.get_minimum_balance("SAVINGS") == 1000.0
    assert AccountRulesEngine.get_minimum_balance("CURRENT") == 0.0
    assert AccountRulesEngine.get_minimum_balance("FIXEDDEPOSIT") == 0.0

    print("PASS: Minimum balance rules")


def test_interest_rate_rules():

    assert AccountRulesEngine.get_interest_rate("SAVINGS") == 4.0
    assert AccountRulesEngine.get_interest_rate("FIXEDDEPOSIT") == 6.5
    assert AccountRulesEngine.get_interest_rate("CURRENT") == 0.0

    print("PASS: Interest rate rules")


def test_overdraft_rules():

    assert AccountRulesEngine.get_overdraft_limit("CURRENT") == 10000.0
    assert AccountRulesEngine.get_overdraft_limit("SAVINGS") == 0.0
    assert AccountRulesEngine.get_overdraft_limit("FIXEDDEPOSIT") == 0.0

    print("PASS: Overdraft rules")


def test_case_insensitive_lookup():

    assert AccountRulesEngine.get_interest_rate("savings") == 4.0
    assert AccountRulesEngine.get_interest_rate("Savings") == 4.0
    assert AccountRulesEngine.get_interest_rate("SAVINGS") == 4.0

    print("PASS: Case-insensitive lookup")


def test_savings_withdrawal():

    # Balance = 5000
    # Minimum balance = 1000
    # Maximum withdrawal = 4000

    assert AccountRulesEngine.validate_withdrawal(
        "SAVINGS",
        5000.0,
        4000.0
    ) is True

    assert AccountRulesEngine.validate_withdrawal(
        "SAVINGS",
        5000.0,
        4001.0
    ) is False

    print("PASS: Savings withdrawal rules")


def test_current_overdraft():

    # Balance = 5000
    # Overdraft = 10000
    # Maximum withdrawal = 15000

    assert AccountRulesEngine.validate_withdrawal(
        "CURRENT",
        5000.0,
        15000.0
    ) is True

    assert AccountRulesEngine.validate_withdrawal(
        "CURRENT",
        5000.0,
        15001.0
    ) is False

    print("PASS: Current overdraft rules")


def test_fixed_deposit():

    assert AccountRulesEngine.validate_withdrawal(
        "FIXEDDEPOSIT",
        5000.0,
        5000.0
    ) is True

    assert AccountRulesEngine.validate_withdrawal(
        "FIXEDDEPOSIT",
        5000.0,
        5001.0
    ) is False

    print("PASS: Fixed deposit rules")


def test_invalid_amount():

    assert AccountRulesEngine.validate_withdrawal(
        "SAVINGS",
        5000.0,
        0.0
    ) is False

    assert AccountRulesEngine.validate_withdrawal(
        "SAVINGS",
        5000.0,
        -100.0
    ) is False

    print("PASS: Invalid withdrawal amount")


def test_multiple_products():

    accounts = [
        ("SAVINGS", 10000.0),
        ("CURRENT", 10000.0),
        ("FIXEDDEPOSIT", 10000.0)
    ]

    for account_type, balance in accounts:

        minimum = AccountRulesEngine.get_minimum_balance(
            account_type
        )

        interest = AccountRulesEngine.get_interest_rate(
            account_type
        )

        overdraft = AccountRulesEngine.get_overdraft_limit(
            account_type
        )

        assert minimum >= 0
        assert interest >= 0
        assert overdraft >= 0

        print(
            f"PASS: {account_type} - "
            f"minimum={minimum}, "
            f"interest={interest}, "
            f"overdraft={overdraft}"
        )


if __name__ == "__main__":

    test_minimum_balance_rules()
    test_interest_rate_rules()
    test_overdraft_rules()
    test_case_insensitive_lookup()
    test_savings_withdrawal()
    test_current_overdraft()
    test_fixed_deposit()
    test_invalid_amount()
    test_multiple_products()

    print("\nAll Activity 13.2 tests completed successfully!")