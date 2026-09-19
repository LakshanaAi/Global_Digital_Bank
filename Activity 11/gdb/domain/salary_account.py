from gdb.domain.abstract_account import AbstractAccount


class SalaryAccount(AbstractAccount):

    def __init__(self, account_number: str, balance: float):
        super().__init__(account_number, balance)

    def calculate_interest(self) -> float:
        return self._balance * 0.04

    def get_account_type(self) -> str:
        return "Salary"