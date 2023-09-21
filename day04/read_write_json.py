# import json that one import all the methods
from json import load, dumps


path = 'files/Test1.json'

json_file = open(path, 'r')

# print(json_file.read())

dictionary = json.load(json_file)

print(dictionary)

json_file.close()

print('------------write json file-----------')

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

json_file = open('files/Test2.json', 'w')
# indent make the code in json format better
json_object = json.dumps(students, indent=3)  # converting dictionary object to json object

json_file.write(json_object)

print(json_object)
