"""
10. Create a python file named shipping_address
            Ask the user to enter the following info, and display the shipping address of the user:
                    1. "Enter your full name"
                     2. "Enter your building number"
                     3. "Enter your street name"
                     4. "Enter your city name"
                     5. "Enter your state name"
                     6. "enter your zip code"

             Given data:
                name = "Aaron Kissinger"
                building_number = 13621A
                street_name = "Legacy Circle"
                city = "Fairfax"
                state = "VA"
                zip_code = 22030

            Output:
                Your shipping addrrees is:
                        Aaron Kissinger
                        13621A Legacy Circle
                        Fairfax, VA 22030

"""
name = input("Enter your full name")
building_number = input("Enter your building number")
street_name = input("Enter your street name")
city = input("Enter your city name")
state = input("Enter your state name")
zip_code = float(input("enter your zip code"))

print(f'Your shipping address is:\n'
      f'\t\t{name}\n'
      f'\t\t{building_number} {street_name}\n'
      f'\t\t{city} {state} {zip_code}')
