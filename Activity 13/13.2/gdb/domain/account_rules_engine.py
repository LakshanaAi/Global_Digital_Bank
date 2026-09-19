class AccountRulesEngine:

    RULES = {
        "SAVINGS": {
            "minimum_balance": 1000.0,
            "interest_rate": 4.0,
            "overdraft_limit": 0.0
        },
        "CURRENT": {
            "minimum_balance": 0.0,
            "interest_rate": 0.0,
            "overdraft_limit": 10000.0
        },
        "FIXEDDEPOSIT": {
            "minimum_balance": 0.0,
            "interest_rate": 6.5,
            "overdraft_limit": 0.0
        }
    }

    @staticmethod
    def _get_rules(account_type: str) -> dict:
        account_type = account_type.upper()

        return AccountRulesEngine.RULES.get(
            account_type,
            {
                "minimum_balance": 0.0,
                "interest_rate": 0.0,
                "overdraft_limit": 0.0
            }
        )

    @staticmethod
    def get_minimum_balance(account_type: str) -> float:
        return AccountRulesEngine._get_rules(
            account_type
        )["minimum_balance"]

    @staticmethod
    def get_interest_rate(account_type: str) -> float:
        return AccountRulesEngine._get_rules(
            account_type
        )["interest_rate"]

    @staticmethod
    def get_overdraft_limit(account_type: str) -> float:
        return AccountRulesEngine._get_rules(
            account_type
        )["overdraft_limit"]

    @staticmethod
    def validate_withdrawal(
        account_type: str,
        current_balance: float,
        withdrawal_amount: float
    ) -> bool:

        if withdrawal_amount <= 0:
            return False

        rules = AccountRulesEngine._get_rules(account_type)

        minimum_balance = rules["minimum_balance"]
        overdraft_limit = rules["overdraft_limit"]

        # Amount available including overdraft
        maximum_withdrawal = (
            current_balance + overdraft_limit - minimum_balance
        )

        return withdrawal_amount <= maximum_withdrawal