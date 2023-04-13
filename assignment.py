"""1. Write a Python program that accept a number of words and then those number of words and Print
the number of distinct words and number of occurrences for each distinct word according to their appearance."""

no_of_words = int(input("Enter the number of words: "))

input_words_list = []

for i in range(no_of_words):
    input_words = str.casefold(input("Enter the words: "))
    input_words_list.append(input_words)
    # print(input_words_list)
    x = input_words_list.count(input_words)
    # print(x)
    print(input_words, ": ", x)







# from collections import Counter, OrderedDict
# class OrderedCounter(Counter,OrderedDict):
#    pass
# word_array = []
# n = int(input("Input number of words: "))
# print("Input the words: ")
# for i in range(n):
#    word_array.append(input().strip())
# word_ctr = OrderedCounter(word_array)
# # print(len(word_ctr))
# for word in word_ctr:
#    print(word_ctr[word],end=' ')
