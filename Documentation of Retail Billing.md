# Retail Billing with Multiple Discount Rules

## 1. Problem Statement
Calculate a retail purchase amount and apply the discount rules to determine the customer's final bill.

## 2. Objectives
Calculate product cost, discount and final amount.

## 3. Assumptions
Purchases above Rs. 5000 receive a 10% discount.

## 4. Algorithm
1. Enter product name, price and quantity.
2. Calculate the total amount.
3. Check discount eligibility.
4. Calculate the final bill.
5. Display the invoice.

## 5. Flowchart (Text Representation)
Start → Enter product details → Calculate total → Check discount → Calculate final bill → Display invoice → End.

## 6. Pseudocode
```text
START
INPUT product, price, quantity
total = price * quantity
IF total > 5000
    discount = total * 0.10
ELSE
    discount = 0
final = total - discount
DISPLAY final
STOP
```

## 7. Python Source Code
```python
product = input("Enter product name: ")
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

if total > 5000:
    discount = total * 0.10
else:
    discount = 0

final = total - discount

print("Product:", product)
print("Total Amount:", total)
print("Discount:", discount)
print("Final Amount:", final)
```

## 8. Test Case
Price = Rs. 2000, Quantity = 3.

## 9. Expected Output
```text
Total Amount: 6000
Discount: 600
Final Amount: 5400
```

## 10. Conclusion
The program generates a retail bill and checks the applicable discount rules. It displays the discount and final amount payable.
