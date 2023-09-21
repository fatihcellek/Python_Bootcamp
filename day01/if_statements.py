
if True:
    print('Python Programming') # in block of if statement

if False:
    print('Rubby Programming')  # in block of if statement

print('Java Programming') # not in block of if statement

print('----------------------------------')

score = 70

if score >= 60:
    print('Congrats! You passed the exam')

"""
if(true){ in Java
}
"""

s = 'Hello World'
if 'H' and 'W' in s:
    print(s, 'has', 'H' and 'W')


print('----------------------------------')

if score >= 60:
    print('Passed')
else:
    print('Failed')

print('----------------------------------')

age = 20
result = None

if age >= 21:
    result = 'Eligible'
else:
    result = "Not Eligible"

print(result)

print('----------------------------------')

# Ternary example

age = 26
result = 'Eligible' if age >= 21 else 'Not Eligible'
print(result)

print('----------------------------------')

num = 100
result = None

if num > 0:
    result = 'Positive'
elif num < 0:
    result = 'Negative'
else:
    result = 'Zero'

print(result)

print('----------------------------------')

# Ternary It can be used only if and elif

num = 200

result2 = 'Positive' if num > 0 else 'Zero'

print(result2)

print('----------------------------------')

score = -300

# if score >= 0 and score <= 100:
#    pass

if 0 <= score <= 100:

    if score >= 60:
        print("Passed")
    else:
        print("Failed")
else:
    print("Invalid Score")

print('----------------------------------')

score = 95

if 0 <= score <= 100:
    if score >= 90:
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')
    elif score >= 60:
        print('D')
    else:
        print('F')
else:
    pass















