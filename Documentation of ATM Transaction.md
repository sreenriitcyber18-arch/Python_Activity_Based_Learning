# ATM Transaction Sequence Simulation

## 1. Problem Statement
Process ATM deposits and withdrawals while checking each transaction against the available account balance.

## 2. Objectives
Maintain account balance and validate transactions.

## 3. Assumptions
The initial account balance is Rs. 5000.

## 4. Algorithm
1. Set the initial balance.
2. Enter the number of transactions.
3. Process deposits and withdrawals.
4. Reject invalid withdrawals.
5. Display the final balance.

## 5. Flowchart 
             .---------------.
           /                   \
          (       START         )
           \___________________/
                    |
                    v
             /----------------\
            / Set initial      /
           / balance          /
           \----------------\
                    |
                    v
             /----------------\
            / Enter transaction/
           / count            /
           \----------------\
                    |
                    v
          +----------------------+
          | Process each deposit |
          | or withdrawal        |
          +----------------------+
                    |
                    v
             /------------------\
            / Update balance or  /
           / show error         /
           \------------------/
                    |
                    v
             /------------------\
            / Display final      /
           / balance            /
           \------------------/
                    |
                    v
             .---------------.
           /                   \
          (         END         )
           \___________________/

## 6. Pseudocode
```text
START
INPUT balance
REPEAT for each transaction
    INPUT type, amount
    IF type is deposit
        balance = balance + amount
    ELSE IF type is withdrawal AND amount <= balance
        balance = balance - amount
    ELSE
        DISPLAY "Invalid Transaction"
DISPLAY balance
STOP
```

## 7. Python Source Code
```python
balance = 5000

n = int(input("Enter number of transactions: "))

for i in range(n):
    print("1. Deposit")
    print("2. Withdraw")

    choice = int(input("Enter choice: "))
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid Amount")

    elif choice == 1:
        balance += amount
        print("Deposit Successful")

    elif choice == 2:
        if amount <= balance:
            balance -= amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    else:
        print("Invalid Choice")

print("Final Balance:", balance)
```

## 8. Test Case
Initial balance = Rs. 5000, deposit = Rs. 2000, withdrawal = Rs. 1000.

## 9. Expected Output
```text
Deposit Successful
Withdrawal Successful
Final Balance: 6000
```

## 10. Conclusion
The program simulates ATM transactions and maintains the account balance. It updates the balance only for valid transactions and displays the final balance.
