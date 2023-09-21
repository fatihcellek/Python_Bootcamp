import json
import csv

path = '/Users/cellekair/PycharmProjects/Python_Bootcamp/day04/files/Test.txt'

text_file = open(path, 'r')

# print(text_file.read())

print(text_file.readline())  # reading line by line
print(text_file.readline())
print(text_file.readline())


text_file.close()