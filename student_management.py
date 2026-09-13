#FYCS Practice Program: Student Details & simple calculator
def greet_student() :
print("="* 40)
print("   WELCOME TO FYCS PYTHON LAB    ")
print("="* 40)
def main() :
  greet_student()
  # 1. User Input & Variables
name = input("Enter your name:")
roll_no = input("Enter your Roll number:")
print(f'\nHello {name}! (Roll No: {roll_no})")
# 2. Conditional Statements (Grading logic)
print("\n---Marks Evalution---")
marks = float?(input("Enter your total marks (out of 100):"))
if marks >= 75:
   grade = "Distinction"
elif marks >= 60:
   grade = "First Class"
elif marks >= 40:
   grade = "Pass Class"
else:
   grade = "Needs Improvement"
print(f"Result Status: {grade}")
#3. Loop (Simple Table Generator)
print("\n--- Loop Example: Multiplication Table ---")
num = int(input("Enter a number to print its table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
if ___name___=='__main__":
   main()
    
