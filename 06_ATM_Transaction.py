# ATM Transaction Sequence Simulation

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
