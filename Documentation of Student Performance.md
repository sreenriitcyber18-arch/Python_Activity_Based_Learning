# Student Performance Trend Analysis

## 1. Problem Statement
Analyse a student's marks across three examinations, calculate the average and report the performance trend and pass/fail result.

## 2. Objectives
Calculate average marks and identify improvement or decline.

## 3. Assumptions
The passing mark is 40.

## 4. Algorithm
1. Enter the student name.
2. Enter marks from three examinations.
3. Calculate the average.
4. Compare first and last examination marks.
5. Display performance.

## 5. Flowchart (Text Representation)
Start → Enter marks → Calculate average → Compare marks → Classify performance → Check pass/fail → End.

## 6. Pseudocode
```text
START
INPUT name
INPUT marks1, marks2, marks3
average = (marks1 + marks2 + marks3) / 3
IF marks3 > marks1
    DISPLAY "Improved"
ELSE IF marks3 < marks1
    DISPLAY "Declined"
ELSE
    DISPLAY "No Change"
DISPLAY average
STOP
```

## 7. Python Source Code
```python
name = input("Enter student name: ")

marks = []

for i in range(3):
    mark = int(input("Enter exam marks: "))
    marks.append(mark)

average = sum(marks) / len(marks)

print("Student:", name)
print("Average Marks:", average)

if marks[2] > marks[0]:
    print("Performance Improved")
elif marks[2] < marks[0]:
    print("Performance Declined")
else:
    print("No Change")

if average >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")
```

## 8. Test Case
Marks = 50, 65, 80.

## 9. Expected Output
```text
Average Marks: 65.0
Performance Improved
Result: Pass
```

## 10. Conclusion
The program calculates the average marks and compares examination performance. It reports whether marks improved, declined or stayed the same and shows the result.
