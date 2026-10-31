# Manufacturing Cost and Profitability Analysis

## 1. Problem Statement
Calculate manufacturing cost from the given expenses and compare revenue with cost to determine profit or loss.

## 2. Objectives
Identify whether production meets the profit target.

## 3. Assumptions
The profit target is Rs. 5000.

## 4. Algorithm
1. Enter material cost.
2. Enter labour cost.
3. Enter machine cost.
4. Calculate total production cost.
5. Calculate selling price and profit.
6. Check the profit target.

## 5. Flowchart
             .---------------.
            /                 \
           (      START        )
            \_________________/
                    |
                    v
              /-------------/
             / Input costs /
            /             /
            \-------------/
                    |
                    v
          +---------------------+
          | Calculate total     |
          | cost                |
          +---------------------+
                    |
                    v
          +---------------------+
          | Calculate profit    |
          +---------------------+
                    |
                    v
                /---------\
               / Check    \
              <  target?   >
               \           /
                \---------/
                    |
                    v
              /-------------/
             / Display      /
            / result       /
            \-------------/
                    |
                    v
             .---------------.
            /                 \
           (        END        )
            \_________________/

## 6. Pseudocode
```text
START
INPUT material, labour, machine, selling_price
cost = material + labour + machine
profit = selling_price - cost
IF profit >= 5000
    DISPLAY "Target Achieved"
ELSE
    DISPLAY "Target Not Achieved"
STOP
```

## 7. Python Source Code
```python
material = float(input("Material cost: "))
labour = float(input("Labour cost: "))
machine = float(input("Machine cost: "))
selling = float(input("Selling price: "))

total_cost = material + labour + machine
profit = selling - total_cost

print("Total Cost:", total_cost)
print("Selling Price:", selling)
print("Profit:", profit)

if profit >= 5000:
    print("Target Achieved")
else:
    print("Target Not Achieved")
```

## 8. Test Case
Material = 10000, Labour = 5000, Machine = 3000, Selling price = 25000.

## 9. Expected Output
```text
Total Cost: 18000
Profit: 7000
Target Achieved
```

## 10. Conclusion
The program adds the manufacturing expenses to find the total cost. It compares cost with revenue to show the profit or loss.
