
def file_handling():
    try:
        file1 = open('my_first_file.txt','rt')
        file1.read()
        file1.close()
    except FileNotFoundError:
        print("File is not present, so creating one")
        file2 = open('my_first1_file.txt','wt')
        file2.write("Hi there \nHope you're doing good \nHow is the weather there?\nGood to talk to you again\nBye")
        file2.close()


file_handling()