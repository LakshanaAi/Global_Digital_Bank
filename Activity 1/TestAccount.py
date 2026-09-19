from Account import Account

class TestAccount:
    def displayAccount(self):
        return(f"Account #{self._accountNumber} |"
               f"{self._getName()} ({self._getAge()} yrs)"
               f"{self._getAccountType()} |"
               f"Rs{self._getBalance()} |"
               f"{self._getStatus}")

    #@cla3ssmethod
    def run_test(self):
        print(">>> 1. Creating Account")
        acc1 =Account(1001,"John Doe",25,1000.0,"Savings")
        print("Account Created!")
        print(self.displayAccount(acc1))

        print(">>> 2. Deposit Money")
        amount = 500.0
        if acc1.deposit(amount):
            print(f"Depositing Rs{amount}: Success")
            print(f"New Balance: Rs{acc1.getBalance()}")
        else:
            print(f"Depositing Rs{amount}: Failed (Invalid Amount)")

        invalid_deposit =-100.0
        if acc1.deposit(invalid_deposit):
            print(f"Depositing Rs{invalid_deposit}: Success")
            print(f"New Balance: Rs{acc1.getBalance()}")
        else:
            print(f"Depositing Rs{invalid_deposit}: Failed (Invalid Amount)")

        print(">>> 3. Withdraw Money")
        withdraw_amount = 200.0
        if acc1.withdraw(withdraw_amount):
            print(f"Withdrawing Rs{withdraw_amount}: SUCCESS"
                f"New Balance Rs{acc1.getBalance}")
        else:
            print(f"Withdrawing Rs{withdraw_amount}: Failed")

        print(">>>4.Creating Another account")
        acc2 =Account(1002,"jANE sMITH",30,2000.0,"Current")
        print(self.displayAccount(acc2))

if __name__ == "__main__":
    tester = TestAccount()
    tester.run_test()
        
        

