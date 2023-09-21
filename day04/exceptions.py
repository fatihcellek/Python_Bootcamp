try:
    num = 10 / 0
    print(num)
except:
    print('Something went wrong')
else:
    print('Nothing went wrong')
finally:
    print('Finally block')

print('Test Completed')

print('------------------------------')

tuple1 = (10, 20, 30, 40)
try:
    print(tuple1[2000])
except LookupError:
    print('The index number is too large')
else:
    print('The index number is valid')
finally:
    print('finally block')


print('------------------------------')


try:
    raise FileNotFoundError('No such a file')
except SyntaxError:
    print('Its a syntax error')
except OSError:
    print('It is an operating system error')
except ArithmeticError:
    print('It is an arithmetic error')
finally:
    print('finally blck')

print('-----------------------------------')
"""
Java;
    throw: used for manually throwing an exception
    throws: for exception handling (in method header)
"""
raise LookupError('Invalid entry')





