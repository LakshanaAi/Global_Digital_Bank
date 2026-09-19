from gdb.domain.account_rules_engine import AccountRulesEngine


def test_minimum_balance():

    assert AccountRulesEngine.get_minimum_balance("SAVINGS") == 1000.0
    assert AccountRulesEngine.get_minimum_balance("CURRENT") == 0.0
    assert AccountRulesEngine.get_minimum_balance("FIXEDDEPOSIT") == 0.0

    print("PASS: Minimum balance rules")


def test_interest_rates():

    assert AccountRulesEngine.get_interest_rate("SAVINGS") == 4.0
    assert AccountRulesEngine.get_interest_rate("FIXEDDEPOSIT") == 6.5
    assert AccountRulesEngine.get_interest_rate("CURRENT") == 0.0

    print("PASS: Interest rate rules")


def test_overdraft_limits():

    assert AccountRulesEngine.get_overdraft_limit("CURRENT") == 10000.0
    assert AccountRulesEngine.get_overdraft_limit("SAVINGS") == 0.0
    assert AccountRulesEngine.get_overdraft_limit("FIXEDDEPOSIT") == 0.0

    print("PASS: Overdraft rules")


def test_savings_withdrawal():

    # 5000 - 3000 = 2000 >= 1000
    assert AccountRulesEngine.validate_withdrawal(
        "SAVINGS",
        5000.0,
        3000.0
    ) is True

    # 5000 - 4500 = 500 < 1000
    assert AccountRulesEngine.validate_withdrawal(
        "SAVINGS",
        5000.0,
        4500.0
    ) is False

    print("PASS: Savings withdrawal rules")


def test_current_withdrawal():

    # 5000 + 10000 overdraft = 15000 available
    assert AccountRulesEngine.validate_withdrawal(
        "CURRENT",
        5000.0,
        15000.0
    ) is True

    # Exceeds 15000 available
    assert AccountRulesEngine.validate_withdrawal(
        "CURRENT",
        5000.0,
        16000.0
    ) is False

    print("PASS: Current account overdraft rules")


def test_invalid_withdrawal():

    assert AccountRulesEngine.validate_withdrawal(
        "SAVINGS",
        5000.0,
        0.0
    ) is False

    assert AccountRulesEngine.validate_withdrawal(
        "SAVINGS",
        5000.0,
        -500.0
    ) is False

    print("PASS: Invalid withdrawal rules")


if __name__ == "__main__":
    test_minimum_balance()
    test_interest_rates()
    test_overdraft_limits()
    test_savings_withdrawal()
    test_current_withdrawal()
    test_invalid_withdrawal()

    print("\nAll Activity 13.1 tests completed successfully!")