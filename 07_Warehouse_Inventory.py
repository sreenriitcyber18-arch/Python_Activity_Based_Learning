# Warehouse Inventory Reconciliation

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
