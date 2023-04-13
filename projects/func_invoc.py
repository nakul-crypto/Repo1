from func_def import *

# Dollar to INR
dollar = int(input("Enter the value of Dollar: "))
print("INR Value:", dollar_inr(dollar))

# height_cm_feet(150)
# print("The equivalent height in feet and inches is: ",height_cm_feet(feet, inch))
#

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("The sum of the two numbers is: ", sum(num1, num2))
print("The square of the first number is: ", square(num1))
print("The first number squared to the power of second number: ", square_2(num1, num2))

# upper_case

greeting = input("Enter text here: ")
print(upper_case(greeting))