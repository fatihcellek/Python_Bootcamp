"""
18. Create a python file named grade, a variable named grade is given. write a program to print the following messages:
            'A': excellent
            'B': great job
            'C': good
            'D': passed
            'F': failed
            other wise: invalid

            NOTE: MUST USE NESTED IF. DO NOT USE MORE THAN ONE PRINT STATEMENT
"""

grade = 'C'
result = None

if grade == 'A' or grade == 'B' or grade == 'C' or grade == 'D' or grade == 'F':
    if grade == 'A':
        result = 'excellent'
    elif grade == 'B':
        result = 'great job'
    elif grade == 'C':
        result = 'good'
    elif grade == 'D':
        result = 'passed'
    elif grade == 'F':
        result = 'failed'
else:
    result = 'invalid Grade ', grade

print(result)