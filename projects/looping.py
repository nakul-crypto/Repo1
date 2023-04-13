
# Print Odd numbers from 1 to 9

# for odd in range(10):
#     if(odd % 2 != 0):
#         print(odd)
#
# odd = 1
# while (odd<=9):
#     if odd% 2 !=0:
#         print(odd)
#     odd +=1

#
# num = 1
# while(num<13):
#     if num % 2 != 0 and num<11:
#         print(num)
#         num +=1


# num = 1
# while(num < 10):
#     if num < 6:
#         pass
#     num+=1
#     print(num)





def fizz_buzz(num):
        if num == 0:
            exit()
        if num % 3 == 0:
            if num % 5 == 0:
                print("Fizz Buzz")
            else:
                print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print("Invalid Input")

choice = 'Y'
while(choice == 'Y'):
    fizz_buzz()
    choice = input("Press N/n to exit")















