"""
11. Create a python file named employee_info:
            Ask the user to enter the following info, and diplsay the user entered info:
                        name (String)
                        age (integer)
                        gender (String)
                        company (String)
                        job title (String)
                        salary (float)

            Ex:
                Given Data:
                    name = "Daniel"
                    age = 28
                    gender = 'Male'
                    company_name = 'Google Inc'
                    job_title = "Scrum Master"
                    salary = 90000


                Output:
                    Daniel is 28 years old, gender is Male
                    Daniel works at Google Inc as a Scrum Master
                    Daniel makes $ 90000 per year


"""
name = str(input("Enter your name:"))
age = int(input("Enter your age:"))
gender = str(input("Enter your gender:"))
company_name = str(input("Enter your company:"))
job_title = str(input("Enter your job title:"))
salary = int(input("Enter your salary:"))

print(f'{name} is {age} years old, gender is {gender}\n'
      f'{name} works at {company_name} as a {job_title}\n'
      f'{name} makes $ {salary} per year')
























