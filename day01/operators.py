# arithmetic: +,-,*,/,%

print(10 - 2)
print(10 + 2)
print(10 * 3)
print(10 / 2)
print(10 / 3)
print(10 % 3)

print(int (100 / 2))

# shorthand assignment operators: =,+=,-=,*=,/=,%=
a = 100
a = 200
print(a)

a += 200
print(a)

a -= 50
print(a)

a /= 2
print(a)

# logical operators: and, or, not

s = "Hello World"
print('H' and 'W' in s)

print(True and True)
print( True or False)

s = 'Java Python C# C++'

print('Java' or 'Rubby' in s)
age = 29
citizen_ship = 'USA'
is_eligible = age >= 18 and citizen_ship == 'USA'

print(is_eligible)

has_java = 'Java' in s
print(has_java)

# !contains() in Java
print('Python' not in s)

print(not False)
print(not True) # ! in Java

print('---------------------------------------------')


s = 'Java'
s2 = 'Java'

print(s is s2)  # to check if two variables referencing to the same object (== operator of Java)




