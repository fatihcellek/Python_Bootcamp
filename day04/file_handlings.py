import json
import csv
import os

path = 'files/Test1.txt'

text_file = open(path, 'r')

# print(text_file.read())

print(text_file.readline())  # reading line by line
print(text_file.readline())
print(text_file.readline())

text_file.close()

print('-----------------writing a file-----------------------')

path = 'files/Test2.txt'

text_file2 = open(path, 'w')

text_file2.write('This a new text file\nPython created this file')

text_file2.close()

print('-----------------removing a file-----------------------')

# os.remove('files/Test3.txt')  # file is removed
