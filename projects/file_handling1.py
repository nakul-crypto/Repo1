

def file_handling():
    try:
        file1 = open('my_first_file1.txt','r')
    except FileNotFoundError:
        print("File not found, so creating one")
        file1 = open('my_first_file1.txt','wt')
        file1.writelines("Hi there\nHope you're doing good\nHow is the weather there?\nGood to talk to you again\nBye")
        # file1.seek(0)
        # temp = file1.readlines()
        # print(temp)
        # with open('my_first_file1.txt','w+')as file1:
        #     file1.seek(0)
        #     print(file1.tell())
        #     print(file1.readline())
        #     file1.close()
        #
file_handling()


