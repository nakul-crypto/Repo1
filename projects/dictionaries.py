#
# def my_dict_store():
#     print("\n Welcome to Our Dict Store !!! ")
#     print("Please enter a list Comma separated dictionary elements that you would want to perform Operation Upon")
#
#     capitals= {}
#     for dict_elem in input \
#             ('for ex:  India : New Delhi , USA : Washington DC, Nepal : Kathmandu, Ukraine :  Kyiv \n').split(","):
#         temp_list = dict_elem.split(":")
#         capitals[temp_list[0].replace('"' ,'').strip()] = temp_list[1].replace('"' ,'').strip()
#
#     while(True):
#         print("\n*************** Menu **********************")
#         print("Operations supported by our program are :")
#         print("1: Display number of elements in the capitals collection")
#         print('2: Add an element to the capitals collection like --> Afghanistan: Kabul')
#         print('3: Add multiple elements to the capitals collection like -->  Albania:Tirana,Algeria:Algiers,Andorra:Andorra la Vella')
#         print("4: Remove an element from the collection")
#         print("5: Exit the Program ")
#         choice = int(input("Please enter your choice "))
#
#         if choice == 1:
#             dict_display_capitals(capitals)
#         elif choice == 2:
#             dict_add_element(capitals)
#         elif choice == 3:
#             dict_add_elements(capitals)
#         elif choice == 4:
#             dict_remove_element(capitals)
#         elif choice == 5:
#             break
#         else:
#             print("Invalid Input , Please Try Again !!!!")
#
# def dict_display_capitals(capitals):
#     print(capitals)
#
# def dict_add_element(capitals):
#     update_element = input("Enter the key:value to be added followed by comma ")
#     for update_element in input().split(","):
#         temp_list1 = update_element(":")
#         capitals[temp_list1[len[capitals].replace('"','').strip()] = temp_list[2].replace('"', '').strip()
#         capitals.update(update_element)
#         print(capitals)
#
#
#
# my_dict_store()
