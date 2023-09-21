from functools import reduce

print('----------------closure------------')


#  function that is in another function

def display_message():
    def method():
        for i in range(0, 5):
            print('Hello World')
            print('Hello Python')
            print('-------------')

    method()
    method()
    method()
    method()


display_message()

print('-----------------------------------------------')


def display_palindromes(strings: list):
    def is_palindrome(s: str) -> bool:
        return s[::-1].lower() == s.lower()

    for s in strings:
        if is_palindrome(s):
            print(s)

    # for s in strings:
    #     new_s = ''
    #     for i in range(0, len(str(s))):
    #         new_s += s[i]


print('--------------------map------------------------')

nums = [10, 20, 30, 40, 50, 60, 70, 80]

nums = list(map(lambda x: x * 10, nums))

print(nums)

names = ('Java', 'JAVA', 'java', 'ruby', 'swift', 'CyDeO', 'JavaScript')

names = list(map(lambda s: str(s).upper(), names))  # to make all the string elements uppercase

print(names)

dictionary = {'x': 100, 'y': 200, 'z': 300}

dictionary = dict(map(lambda t: (t[0], t[1] * 10), dictionary.items()))

print(dictionary)

print('--------------------filter------------------------')

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# nums = [x for x in nums if x % 5 == 0]

nums = list(filter(lambda x: x % 5 == 0, nums))  # second way to filter

print(nums)

names = ('Java', 'JAVA', 'java', 'ruby', 'swift', 'CyDeO', 'JavaScript')

# names = [s for s in names if not s.lower().startswith('j')]

names = list(filter(lambda s: not str(s).lower().startswith('j'), names))

print(names)

print('--------------------reduce------------------------')

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(reduce(lambda x, y: x + y, list1))

list1
