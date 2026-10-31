# Hospital Billing and Patient Classification

## 1. Problem Statement
Calculate hospital bills from consultation, diagnostic and treatment charges. Apply a 10% discount when the patient is aged 60 or above.

## 2. Objectives
Calculate the total bill and apply a concession.

## 3. Assumptions
Senior citizens aged 60 or above receive a 10% discount.

## 4. Algorithm
1. Get consultation, diagnostic and treatment charges.
2. Calculate the total bill.
3. Check the patient's age.
4. Apply the discount if eligible.
5. Display the final bill.

## 5. Flowchart (Text Representation)
Start → Input charges and age → Calculate total → Check age → Apply discount → Display bill → End.

## 6. Pseudocode
```text
START
INPUT consultation, diagnostic, treatment, age
total = consultation + diagnostic + treatment
IF age >= 60
    discount = total * 0.10
ELSE
    discount = 0
final_bill = total - discount
DISPLAY final_bill
STOP
```

## 7. Python Source Code
```python
consultation = float(input("Consultation charge: "))
diagnostic = float(input("Diagnostic charge: "))
treatment = float(input("Treatment charge: "))
age = int(input("Patient age: "))

total = consultation + diagnostic + treatment

if age >= 60:
    discount = total * 0.10
else:
    discount = 0

final_bill = total - discount

print("Total Bill:", total)
print("Discount:", discount)
print("Final Bill:", final_bill)
```

## 8. Test Case
Consultation = 500, Diagnostic = 1000, Treatment = 2500, Age = 65.

## 9. Expected Output
```text
Total Bill: 4000
Discount: 400
Final Bill: 3600
```

## 10. Conclusion
The program adds all hospital charges and checks the patient's age. It applies the eligible senior-citizen discount and displays the final bill.
