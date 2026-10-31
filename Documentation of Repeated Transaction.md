# Repeated Transaction Detection

## 1. Problem Statement
Examine transaction IDs and amounts to identify duplicate transactions and flag amounts above the specified limit.

## 2. Objectives
Detect duplicate transaction IDs and suspicious amounts.

## 3. Assumptions
Transactions above Rs. 10000 are flagged as suspicious.

## 4. Algorithm
1. Create transaction ID and amount lists.
2. Enter transaction details.
3. Check duplicate IDs.
4. Check amounts above Rs. 10000.
5. Display suspicious transactions.

## 5. Flowchart (Text Representation)
Start → Enter transactions → Check duplicate IDs → Check transaction amount → Display suspicious records → End.

## 6. Pseudocode
```text
START
INPUT transaction IDs and amounts
FOR each transaction
    IF ID is repeated
        DISPLAY "Duplicate Transaction"
    IF amount > 10000
        DISPLAY "Suspicious Amount"
STOP
```

## 7. Python Source Code
```python
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
```

## 8. Test Case
Transactions: T101 = Rs. 5000, T102 = Rs. 15000, T101 = Rs. 3000.

## 9. Expected Output
```text
T101 Duplicate Transaction
T102 Suspicious Amount: 15000
T101 Duplicate Transaction
```

## 10. Conclusion
The program identifies repeated transaction IDs and examines transaction amounts. It flags duplicate IDs and suspicious high-value transactions.
