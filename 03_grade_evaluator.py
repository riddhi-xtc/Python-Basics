
print("================================")
print("       GRADE EVALUATOR")
print("================================")

name = input("Enter your name: ")
marks = int(input("Enter your marks: "))

print("\n========== RESULT ==========")
print("Student Name:", name)
print("Marks:", marks)

if marks >= 90:
    print("Grade: A")

elif marks >= 75:
    print("Grade: B")

elif marks >= 60:
    print("Grade: C")

elif marks >= 40:
    print("Grade: D")

else:
    print("Result: Needs improvement")

print("============================")