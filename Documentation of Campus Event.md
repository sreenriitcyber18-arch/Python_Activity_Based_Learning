# Campus Event Financial Planning

## 1. Problem Statement
Calculate campus event expenses and determine the participant contribution or registrations needed to meet the budget.

## 2. Objectives
Calculate total expenses and participant registration fees.

## 3. Assumptions
Each participant pays Rs. 500.

## 4. Algorithm
1. Enter venue, equipment, catering and transport expenses.
2. Calculate total expenses.
3. Enter sponsorship amount.
4. Calculate remaining expenses.
5. Calculate the minimum number of participants required.

## 5. Flowchart (Text Representation)
Start → Input expenses → Calculate total → Subtract sponsorship → Calculate participants → Display result → End.

## 6. Pseudocode
```text
START
INPUT venue, equipment, catering, transport
INPUT sponsorship
total = venue + equipment + catering + transport
remaining = total - sponsorship
participants = remaining / 500 (rounded up)
DISPLAY total, remaining
DISPLAY minimum participants
STOP
```

## 7. Python Source Code
```python
import math

venue = float(input("Venue cost: "))
equipment = float(input("Equipment cost: "))
catering = float(input("Catering cost: "))
transport = float(input("Transport cost: "))
sponsorship = float(input("Sponsorship amount: "))

total = venue + equipment + catering + transport
remaining = max(0, total - sponsorship)

participants = math.ceil(remaining / 500)

print("Total Expenses:", total)
print("Sponsorship:", sponsorship)
print("Remaining Amount:", remaining)
print("Minimum Participants:", participants)
```

## 8. Test Case
Venue = 10000, Equipment = 5000, Catering = 15000, Transport = 5000, Sponsorship = 10000.

## 9. Expected Output
```text
Total Expenses: 35000
Sponsorship: 10000
Remaining Amount: 25000
Minimum Participants: 50
```

## 10. Conclusion
The program calculates event expenses and compares them with the budget. It calculates the required participant registrations to cover the remaining cost.
