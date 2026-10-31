# Employee Payroll and Deduction Analysis

## 1. Problem Statement
Calculate an employee's gross and net salary using basic pay, allowances and deductions.

## 2. Objectives
Calculate gross salary and net salary.

## 3. Assumptions
HRA = 20% of basic salary, DA = 10% of basic salary, and deduction = 5% of gross salary.

## 4. Algorithm
1. Enter the basic salary.
2. Calculate HRA and DA.
3. Calculate gross salary.
4. Calculate the deduction.
5. Display net salary.

## 5. Flowchart 
              _____________
             /             \
            /     START     \
            \               /
             \_____________/
                    |
                    v
              /-------------/
             / Input basic  /
            / salary       /
            \-------------/
                    |
                    v
          +---------------------+
          | Calculate           |
          | allowances          |
          +---------------------+
                    |
                    v
          +---------------------+
          | Calculate gross     |
          | salary              |
          +---------------------+
                    |
                    v
          +---------------------+
          | Calculate           |
          | deductions          |
          +---------------------+
                    |
                    v
              /-------------/
             / Display net  /
            / salary       /
            \-------------/
                    |
                    v
              _____________
             /             \
            /      END      \
            \               /
             \_____________/

## 6. Pseudocode
```text
START
INPUT basic_salary
hra = basic_salary * 20 / 100
da = basic_salary * 10 / 100
gross = basic_salary + hra + da
deduction = gross * 5 / 100
net = gross - deduction
DISPLAY gross, deduction, net
STOP
```

## 7. Python Source Code
```python
basic = float(input("Enter basic salary: "))

hra = basic * 0.20
da = basic * 0.10

gross = basic + hra + da
deduction = gross * 0.05
net = gross - deduction

print("Basic Salary:", basic)
print("HRA:", hra)
print("DA:", da)
print("Gross Salary:", gross)
print("Deduction:", deduction)
print("Net Salary:", net)
```

## 8. Test Case
Basic salary = 20000.

## 9. Expected Output
```text
HRA: 4000
DA: 2000
Gross Salary: 26000
Deduction: 1300
Net Salary: 24700
```

## 10. Conclusion
The program calculates allowances and deductions from the basic pay. It subtracts the deduction to display the employee's net salary.
