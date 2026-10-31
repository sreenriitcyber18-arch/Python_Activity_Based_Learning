# Warehouse Inventory Reconciliation

## 1. Problem Statement
Calculate closing inventory from opening stock, received stock and dispatched stock, then identify when replenishment is needed.

## 2. Objectives
Calculate closing stock and identify shortages.

## 3. Assumptions
Minimum required stock is 10 units.

## 4. Algorithm
1. Enter the product name.
2. Enter opening stock.
3. Enter received quantity.
4. Enter dispatched quantity.
5. Calculate closing stock.
6. Check the minimum stock level.

## 5. Flowchart (Text Representation)
Start → Enter stock details → Calculate closing stock → Check stock level → Display result → End.

## 6. Pseudocode
```text
START
INPUT product, opening, received, dispatched
closing = opening + received - dispatched
IF closing < 10
    DISPLAY "Replenishment Required"
ELSE
    DISPLAY "Stock Available"
DISPLAY closing
STOP
```

## 7. Python Source Code
```python
product = input("Enter product name: ")
opening = int(input("Opening stock: "))
received = int(input("Received stock: "))
dispatched = int(input("Dispatched stock: "))

closing = opening + received - dispatched

print("Product:", product)
print("Closing Stock:", closing)

if closing < 10:
    print("Replenishment Required")
    print("Required Quantity:", 10 - closing)
else:
    print("Stock Available")
```

## 8. Test Case
Opening = 20, Received = 10, Dispatched = 25.

## 9. Expected Output
```text
Closing Stock: 5
Replenishment Required
Required Quantity: 5
```

## 10. Conclusion
The program calculates closing stock using the stock movement values. It identifies low stock and indicates when replenishment is required.
