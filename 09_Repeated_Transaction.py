# Repeated Transaction Detection

ids = []
amounts = []

n = int(input("Enter number of transactions: "))

for i in range(n):
    tid = input("Enter transaction ID: ")
    amount = float(input("Enter amount: "))

    ids.append(tid)
    amounts.append(amount)

print("Transaction Analysis")

for i in range(n):
    if ids.count(ids[i]) > 1:
        print(ids[i], "Duplicate Transaction")

    if amounts[i] > 10000:
        print(ids[i], "Suspicious Amount:", amounts[i])
