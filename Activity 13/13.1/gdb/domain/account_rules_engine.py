class AccountRulesEngine:

    @staticmethod
    def get_minimum_balance(account_type: str) -> float:
        account_type = account_type.upper()

        if account_type == "SAVINGS":
            return 1000.0
        else:
            return 0.0

    @staticmethod
    def get_interest_rate(account_type: str) -> float:
        account_type = account_type.upper()

        if account_type == "SAVINGS":
            return 4.0
        elif account_type == "FIXEDDEPOSIT":
            return 6.5
        else:
            return 0.0

    @staticmethod
    def get_overdraft_limit(account_type: str) -> float:
        account_type = account_type.upper()

        if account_type == "CURRENT":
            return 10000.0
        else:
            return 0.0

    @staticmethod
    def validate_withdrawal(
        account_type: str,
        current_balance: float,
        withdrawal_amount: float
    ) -> bool:

        account_type = account_type.upper()

        if withdrawal_amount <= 0:
            return False

        minimum_balance = AccountRulesEngine.get_minimum_balance(
            account_type
        )

        overdraft_limit = AccountRulesEngine.get_overdraft_limit(
            account_type
        )

        # Current accounts can use their overdraft limit
        if account_type == "CURRENT":
            return withdrawal_amount <= (
                current_balance + overdraft_limit
            )

        # Other accounts must maintain their minimum balance
        remaining_balance = current_balance - withdrawal_amount

        return remaining_balance >= minimum_balance