# Python Source Code
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