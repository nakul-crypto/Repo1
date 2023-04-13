from calc_def import *


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

function = int(input("Select 0 to exit or 1, 2 and 3 for sum, square or exponential function: "))
if function == 0:
    exit()
function = True
while function != 0:
    if function == 1:
        sum(num1, num2)
        print("The sum of the two numbers is: ", sum(num1, num2))

    elif function == 2:
        square(num1)
        print("The square of the first number is: ", square(num1))

    elif function == 3:
        square_2(num1, num2)
        print("The first number squared to the power of second number: ", square_2(num1, num2))



