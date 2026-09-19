from gdb.domain.account_rules_engine import AccountRulesEngine
from gdb.domain.account_rules_properties_loader import (
    AccountRulesPropertiesLoader
)


def test_savings_properties():

    assert AccountRulesEngine.get_minimum_balance(
        "savings"
    ) == 1000.0

    assert AccountRulesEngine.get_interest_rate(
        "savings"
    ) == 4.0

    print("PASS: Savings properties loaded")


def test_current_properties():

    assert AccountRulesEngine.get_overdraft_limit(
        "current"
    ) == 10000.0

    print("PASS: Current properties loaded")


def test_fixed_deposit_properties():

    assert AccountRulesEngine.get_interest_rate(
        "fixeddeposit"
    ) == 6.5

    print("PASS: Fixed deposit properties loaded")


def test_salary_properties():

    assert AccountRulesEngine.get_interest_rate(
        "salary"
    ) == 0.0

    assert AccountRulesEngine.get_minimum_balance(
        "salary"
    ) == 0.0

    print("PASS: Salary properties loaded")


def test_loader_directly():

    rules = AccountRulesPropertiesLoader.load("savings")

    assert rules["minBalance"] == "1000.0"
    assert rules["interestRate"] == "4.0"

    print("PASS: Properties loader")


def test_savings_withdrawal():

    # 5000 - 1000 minimum balance = 4000 maximum withdrawal

    assert AccountRulesEngine.validate_withdrawal(
        "savings",
        5000.0,
        4000.0
    ) is True

    assert AccountRulesEngine.validate_withdrawal(
        "savings",
        5000.0,
        4001.0
    ) is False

    print("PASS: Savings withdrawal rule")


def test_current_overdraft():

    # 5000 + 10000 overdraft = 15000 available

    assert AccountRulesEngine.validate_withdrawal(
        "current",
        5000.0,
        15000.0
    ) is True

    assert AccountRulesEngine.validate_withdrawal(
        "current",
        5000.0,
        15001.0
    ) is False

    print("PASS: Current overdraft rule")


def test_fixed_deposit_withdrawal():

    assert AccountRulesEngine.validate_withdrawal(
        "fixeddeposit",
        5000.0,
        5000.0
    ) is True

    assert AccountRulesEngine.validate_withdrawal(
        "fixeddeposit",
        5000.0,
        5001.0
    ) is False

    print("PASS: Fixed deposit withdrawal rule")


if __name__ == "__main__":

    test_savings_properties()
    test_current_properties()
    test_fixed_deposit_properties()
    test_salary_properties()
    test_loader_directly()
    test_savings_withdrawal()
    test_current_overdraft()
    test_fixed_deposit_withdrawal()

    print("\nAll Activity 14 tests completed successfully!")