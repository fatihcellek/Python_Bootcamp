employee1 = {}

employee1['name'] = 'James'
employee1['name'] = 'Daniel'
employee1['age'] = 33
employee1['gender'] = 'Male'
employee1['salary'] = 65000

print(employee1)

employee2 = {
    'name': 'James',
    'age': 29,
    'salary': 80_000,
    'full-time': False
}

print(employee2)
print(employee2['name'])
employee2['salary'] += 10000
print(employee2)

employee2.update({'age': 45})  # to update the value

print(employee2)

employee2['full-time'] = True

print(employee2)

employee2.pop('full-time')  # to remove the pairs

print(employee2)

print(help(dict.popitem))

employee2.popitem()

print(employee2)

l = employee2.copy()  # to copy all the pairs of dictionary
print(l)

print('--------------Iterating the Dictionary------------------')

employee3 = {
    'name': 'Shay',
    'age': 29,
    'salary': 110_000,
    'full-time': False,
    'job_title': 'Developer',
    'company': 'Apple Inc'
}

print(list(employee3.keys()))

for key in employee3.keys():  # to print every single key
    print(f'{key} : {employee3.get(key)}')  # {employee3[key]} second way of second part

print('-----------------------------------------------------')

values = list(employee3.values())
print(values)

for value in employee3.values():
    print(values)

print('-----------------------------------------------------')

for x in employee3.items():
    print(f'{x[0]} : {x[1]}')

print('-----------------------------------------------------')

students = {
    'A01': {
        'name': 'James',
        'gender': 'Male',
        'gpa': 3.5,
        'subjects': ['Math', 'Physics']
    },
    'A02': {
        'name': 'Hazel',
        'gender': 'Female',
        'gpa': 3.8,
        'subjects': ['Biology', 'Programming']
    },
    'A03': {
        'name': 'Yulia',
        'gender': 'Female',
        'gpa': 4,
        'subjects': ['Chemistry', 'Programming']
    }
}

print(students)

students['A01']['gpa'] = 2.5  # to access the values

print(students)
students['A02']['name'] = 'Daniel'  # to update the value
students['A02']['gender'] = 'Female'

print(students)

students['A02'].update({'name': 'Fatih', 'gender': 'Male'})  # second way to update the value

print(students)

students['A02']['subjects'][1] = 'SDET'

print(students)

print('------------------')

for x in students.items():
    print(x[1])
    for y in x[1]:
        print(y)

print('------------------')

for value in students.values():
    print(values)
    for item in value.items():
        print(item[1])