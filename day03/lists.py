groceries_list = ['Eggs', 'Milk', 'Rice' ]

groceries_list.append('Chicken')
groceries_list.extend(('Beef','Oranges','Onion'))

print(len(groceries_list))
print(groceries_list)

groceries_list[-2] = 'Cherry'

print(len(groceries_list))
print(groceries_list)

print('---------------------------------------------')

numbers_list = [10, 20, 30, 40, 50, 60, 70, 80] # list

print(numbers_list)

numbers_list[ 2:-2 ] = [300,4000,5,600000] # to update the elements

print(numbers_list)


print('---------------------------------------------')


characters = ['a','b','c','d','f','g','h','i']

print(characters)

list = characters[2: len(characters) - 3]

print(list)

list2 = characters[:4]

print(list2)

list3 = characters[2:]

print(list3)

characters[2:5] = ['C','D','E','D','D','E','X','Y','Z'] # the rest will be shifted


print(characters)

print('---------------------------------------------')

names = ['Conor','Steve','Breanna']

for x in names:
    print(x)

print('---------------------------------------------')

nums = [10,20,30,40,50,60]

for i in range(0,len(nums)):
    nums[i] /= 5

print(nums)

print('---------------------------------------------')


nums = [10,20,30,40,50,60]

for i in reversed(range(len(nums))):
    print(nums[i])

print('---------------------------------------------')


for x in nums[::-1]: # reverse version
    print(x)

print('---------------------------------------------')

for x in reversed(nums): # that also make reverse the elements
    print(x)

print('---------------------------------------------')

i = 0

while i < len(nums):
    print(nums[i])
    i += 1
print('---------------------------------------------')

for i in range(1,6):
    print(i + 2)
print('---------------------------------------------')

# sort method

nums = [60,500,10,20,15,5,0]

# nums.sort() # sorted ascending order
nums.sort(reverse = True)

print(nums)

print('---------------------------------------------')

list1 = [10,20,30,40,]

list1.reverse()

print(list1)

print('---------------------------------------------')

# tuple_elements = ('Java', 'Python', 'C#', 'Ruby')
#
# list_elements = list(tuple_elements)
# list_elements[-2] = 'C++'
# list_elements.append('SWIFT')
#
# print(list_elements)
#
# tuple_elements = tuple(list_elements)
#
# print(tuple_elements)

print('---------------------------------------------')

list1 = [1,2,3,4,5] # list
list2 = [1,2,3,4,5]

print(list1 is  list2 )

tuple1 = (1,2,3,4,5) # tuple
tuple2 = (1,2,3,4,5)

print(tuple2 is tuple1)


print('---------------------------------------------')



groceries_list = ['Eggs', 'Milk', 'Rice' ]

groceries_list.append('Chicken')
groceries_list.extend(('Beef','Oranges','Onion'))

print(groceries_list)

groceries_list.remove('Beef')

print(groceries_list)

groceries_list.pop() # remove the last index

print(groceries_list)

groceries_list.pop(1) # remove the specific element

print(groceries_list)

groceries_list.insert(2,'Apple') # add the element at the specific place

print(groceries_list)

print(groceries_list.index('Apple'))

nums = [1,2,3,4,5,1,1,1,1,1] # to count the given element

print(nums.count(1))

print('-----------------Comprehensions----------------------------')

nums = []

for x in range(1,51):
    nums.append(x)

print(nums)


print('---------------------------------------------')
"""

divisible_by_5 = []

for x in nums:
    if x % 5 == 0:
        divisible_by_5.append(x)

print(divisible_by_5)

"""
divisible_by_5 = tuple([x for x in nums if x % 5 == 0])

print(divisible_by_5)


print('---------------------------------------------')

even_nums = [x for x in nums if x % 2 == 0]
odd_nums = [x for x in nums if x % 2 != 0]

print(even_nums)
print(odd_nums)

print('---------------------------------------------')

names = ['Python','Java','Java','JavaScript','java','JaVa','Ruby']

names = [x for x in names if x.lower() != 'java']

print(names)

print('---------------------------------------------')







