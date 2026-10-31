# Student Performance Trend Analysis

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
