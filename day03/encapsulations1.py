class Person:

    def __init__(self, name: str = 'Unknown', age: int = 1):
        self.__name = None
        self.__age = None
        self.set_name(name)
        self.set_age(age)

    def get_name(self) -> str:
        if self.__name is None or self.__name == '' or type(self.__name) != str:
            raise RuntimeError(f'Invalid name has been set:  {self.__name}')

        return self.__name

    def set_name(self,name: str):
        if type(name) != str:
            print(f'Name must be string')
        if name == '':
            raise RuntimeError(f'Person name can not be empty')
        self.__name = name

    def get_age(self) -> int:
        return self.__age
    def set_age(self, age):
        if age < 0 or age > 150:
            raise RuntimeError(f'Invalid age {age}')
        self.__age = age

    def __str__(self): # name of tha class and curly braces
        return str(f'{type(self).__name__} {self.__dict__}')


person1 = Person('James', 33)

print(person1.get_name())
print(person1.get_age())

person1 = Person('Fatih')

print(person1.get_name())

person2 = Person('Cems',32)

print(person2.get_name(), person2.get_age())

print('--------------------------------------------------')

print(person1)
print(person2)


