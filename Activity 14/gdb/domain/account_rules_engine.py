from gdb.domain.account_rules_properties_loader import (
    AccountRulesPropertiesLoader
)


class AccountRulesEngine:

    @staticmethod
    def get_minimum_balance(account_type: str) -> float:

        return AccountRulesPropertiesLoader.get_float(
            account_type,
            "minBalance",
            0.0
        )

    @staticmethod
    def get_interest_rate(account_type: str) -> float:

        return AccountRulesPropertiesLoader.get_float(
            account_type,
            "interestRate",
            0.0
        )

    @staticmethod
    def get_overdraft_limit(account_type: str) -> float:

        return AccountRulesPropertiesLoader.get_float(
            account_type,
            "overdraftLimit",
            0.0
        )

    @staticmethod
    def validate_withdrawal(
        account_type: str,
        current_balance: float,
        withdrawal_amount: float
    ) -> bool:

        if withdrawal_amount <= 0:
            return False

        minimum_balance = (
            AccountRulesEngine.get_minimum_balance(account_type)
        )

        overdraft_limit = (
            AccountRulesEngine.get_overdraft_limit(account_type)
        )

        maximum_withdrawal = (
            current_balance
            + overdraft_limit
            - minimum_balance
        )

        return withdrawal_amount <= maximum_withdrawal