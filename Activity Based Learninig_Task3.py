
#Python Source Code 
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