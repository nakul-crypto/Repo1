
# Sum of numbers
# num = int(input("Enter a number: "))
#
# for i in range(num):
#     num = i + num
# print(num)

# Display Prime numbers from 1 till the number

# num = int(input("Enter a number: "))
#
# for number in range(2, num+1):
#     if num > 1:
#         for i in range(2, number):
#             if(number % i) == 0:
#                 break
#         else:
#             print(number)

# Even and Odd numbers from 1 till the number

# num = int(input("Enter a number: "))
#
# for i in range(num+1):
#     if i % 2 == 0:
#         print(i,end = " ")
#
# for j in range(num +1):
#     if j % 2 != 0:
#         print(j,end = " ")

# Fibonacci number till the number

# input_num = int(input("Enter a number: "))
#
# n1, n2 =0,1
# count =0
#
# for i in range(input_num):
#     if input_num <= 0:
#         print("Enter a positive number")
#     elif input_num == 1:
#         print(input_num, ":")
#         print(n1)
#
#     else:
#         while count <= input_num:
#             print(n1)
#             nth = n1 + n2
#
#             n1 = n2
#             n2 = nth
#             count += 1

a = 10
print(type(a))
print(id(a))
