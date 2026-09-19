from Account import Account


print("=== Activity 2: Test Account Suite ===")

# Step 1: Test Account Creation & Initial Balance
account = Account(5000.0)

if account.getBalance() == 5000.0:
    print("Test 1 (Initial Balance 5000.0): [PASS]")
else:
    print("Test 1 (Initial Balance 5000.0): [FAIL]")


# Step 2: Test Valid Deposit
result = account.deposit(2000.0)

if result and account.getBalance() == 7000.0:
    print("Test 2 (Deposit 2000.0 -> Balance 7000.0): [PASS]")
else:
    print("Test 2 (Deposit 2000.0 -> Balance 7000.0): [FAIL]")


# Step 3: Test Negative Deposit
result = account.deposit(-500.0)

if not result and account.getBalance() == 7000.0:
    print("Test 3 (Negative Deposit -> Rejected): [PASS]")
else:
    print("Test 3 (Negative Deposit -> Rejected): [FAIL]")


# Step 4: Test Valid Withdrawal
result = account.withdraw(3000.0)

if result and account.getBalance() == 4000.0:
    print("Test 4 (Withdraw 3000.0 -> Balance 4000.0): [PASS]")
else:
    print("Test 4 (Withdraw 3000.0 -> Balance 4000.0): [FAIL]")


# Step 5: Test Withdrawal Exceeding Balance
result = account.withdraw(10000.0)

if not result and account.getBalance() == 4000.0:
    print("Test 5 (Exceeding Withdrawal -> Rejected): [PASS]")
else:
    print("Test 5 (Exceeding Withdrawal -> Rejected): [FAIL]")


# Step 6: Test Negative Withdrawal
result = account.withdraw(-100.0)

if not result and account.getBalance() == 4000.0:
    print("Test 6 (Negative Withdrawal -> Rejected): [PASS]")
else:
    print("Test 6 (Negative Withdrawal -> Rejected): [FAIL]")


print("All Account tests completed successfully!")