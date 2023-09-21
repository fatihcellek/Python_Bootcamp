days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday", "Sunday",1,2,3,4,5,True,False)

# tuple size is fixed and unchangeable

print(type(days))
print(len(days))

print(days[0]) # first index
print(days[-1]) # last index


days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday", "Sunday")

var = days[1:4]
print(var)

tuple1 = (1,2,3)
tuple2 = (1,2,3)

print(tuple1 == tuple2)
print(tuple1 is tuple2)

var = tuple1 + tuple2 # to merge two tuples

print(var)

var = tuple1 * 5

print(var)

reversed_tuple = days[::-1] # to reverse tuple
print(reversed_tuple)

print(tuple(reversed(days))) # second way to reverse

# to get tuple index number

print(days.index('Wednesday'))

# how many specific element

numbers = (10,10,10,10,10,20,20,30,40,50,10,)

print(numbers.count(10)) # to count the index numbers

print('--------------------------------------------')

for x in days:
    print(x)

print('--------------------------------------------')

for x in range(0,len(days)): # normal order
    print(x)

print('--------------------------------------------')

for x in reversed(range(len(days))):
    print(x)







