"""
17. Create a python file named crew_and_passanger, Given a number of people on the ship, determine how many need to be crew members and how many can be passengers. Print how many of each type there should be.

            Total: 50  ====> 20 crew, 30 passengers
            Total: 75  ====> 25 crew, 50 passengers
            Total: 100 ====> 30 crew, 70 passengers
            Any other number of people on the ship is not valid

            NOTE: MUST USE NESTED IF. DO NOT USE MORE THAN ONE PRINT STATEMENT

"""
number = 200  # number should be 100, 75 or 50
result = None

if number == 100 or number == 75 or number == 50:
    if number == 100:
        result = '30 crew, 70 passengers'
    elif number == 75:
        result = '25 crew, 50 passengers'
    elif number == 50:
        result = '20 crew, 30 passengers'
else:
    result = 'Invalid', number

print(result)
