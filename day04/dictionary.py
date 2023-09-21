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



