# Dollar INR Convertor
def dollar_inr(dollar):
    conversion_inr = dollar * 82
    return conversion_inr


# Height conversion from cm to feet
def height_cm_feet(height_cm):
    length = height_cm/2.54
    feet = int(length//12)
    inch = round(length-12 * feet)

    return feet, inch

def sum(num1, num2):
    return num1 + num2
def square(num1):
     return num1**2
def square_2(num1, num2):
    return num1**num2


# Upper case
def upper_case(greeting):
    greeting = greeting.upper()
    return greeting