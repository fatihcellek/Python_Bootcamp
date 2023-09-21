"""
13.  Create a python file named grade_level1.  write a program that asks user to enter the grade level number,  determine and print which school type the person is in is in.
            grade level and types are:
                    1-5: Elementary school
                    6-8: Middle school
                    9-12: High school
                    13-16: College
                    17-18: Grad School

              Assume that the given number is 1 ~ 18
"""
number = int(input('Enter the grade level number: '))

if 1 <= number <= 5:
    print('Elementary school')
elif 6 <= number <= 8:
    print('Middle school')
elif 9 <= number <= 12:
    print('High school')
elif 13 <= number <= 16:
    print('College')
elif 17 <= number <= 18:
    print('Grad School')
else:
    print('Invalid number:', number)
