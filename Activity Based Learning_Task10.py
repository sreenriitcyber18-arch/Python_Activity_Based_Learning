#Python Source Code
password = input("Enter password: ")
upper = False 
lower = False
digit = False 
for ch in password:
    if ch.isupper():
        upper = True   
    elif ch.islower():
        lower = True  
    elif ch.isdigit(): 
        digit = True 
if len(password) >= 8 and upper and lower and digit: 
    print("Valid Password") 
else:
    print("Invalid Password")
    if len(password) < 8: 
        print("Minimum 8 characters required")
    if not upper:
        print("At least one uppercase letter required")
    if not lower:
        print("At least one lowercase letter required")
    if not digit:
        print("At least one number required")