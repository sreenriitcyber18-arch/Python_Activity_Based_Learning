# Password Policy Validation Engine

## 1. Problem Statement
Validate a password by checking its length and whether it contains uppercase letters, lowercase letters and digits.

## 2. Objectives
Check whether a password meets the security rules.

## 3. Assumptions
A valid password must have at least 8 characters, one uppercase letter, one lowercase letter and one digit.

## 4. Algorithm
1. Enter the password.
2. Check password length.
3. Check uppercase letters.
4. Check lowercase letters.
5. Check numbers.
6. Display the validation result.

## 5. Flowchart (Text Representation)
Start → Enter password → Check length → Check character types → Display valid or invalid → End.

## 6. Pseudocode
```text
START
INPUT password
IF length < 8
    DISPLAY "Minimum 8 characters required"
IF no uppercase
    DISPLAY "Uppercase required"
IF no lowercase
    DISPLAY "Lowercase required"
IF no digit
    DISPLAY "Number required"
IF all conditions satisfied
    DISPLAY "Valid Password"
STOP
```

## 7. Python Source Code
```python
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
```

## 8. Test Case
Password = Python123.

## 9. Expected Output
```text
Valid Password
```

## 10. Conclusion
The program validates the password using basic string operations and conditional statements. It displays whether the password is valid and identifies missing requirements.
