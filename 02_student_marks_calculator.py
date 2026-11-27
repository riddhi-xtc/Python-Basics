
print("================================")
print("      STUDENT MARKS CALCULATOR")
print("================================")

name = input("Enter student name: ")

subject1 = int(input("Enter marks in Subject 1: "))
subject2 = int(input("Enter marks in Subject 2: "))
subject3 = int(input("Enter marks in Subject 3: "))

total = subject1 + subject2 + subject3
average = total / 3

print("\n========== RESULT ==========")

print("Student Name:", name)
print("Subject 1:", subject1)
print("Subject 2:", subject2)
print("Subject 3:", subject3)

print("Total Marks:", total)
print("Average Marks:", average)

print("============================")