

# Height conversion from cm to feet

height_cm = float(input("Enter the height in cms: "))
length = height_cm/2.54
feet = int(length//12)
inch = round(length -12*feet)
print("The equivalent height in feet and inches is: ", feet,"feet and ", inch, "inches")
