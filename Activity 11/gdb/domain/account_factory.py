from gdb.domain.iaccount import IAccount
from gdb.domain.abstract_account import AbstractAccount
from gdb.domain.salary_account import SalaryAccount


class AccountFactory:

    @staticmethod
    def create_account(account_type: str,
                       account_number: str,
                       balance: float) -> IAccount:

        account_type = account_type.lower()

        if account_type == "salary":
            return SalaryAccount(account_number, balance)

        elif account_type == "abstract":
            return AbstractAccount(account_number, balance)

        else:
            raise ValueError(f"Unknown account type: {account_type}")