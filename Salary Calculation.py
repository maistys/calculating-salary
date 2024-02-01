#1835072 Seong-Hyun Ryu
data = [
    [1, 'John Doe', 'Male', 30, 60000],
    [2, 'Jane Doe', 'Female', 28, 55000],
    [3, 'Bob Smith', 'Male', 35, 75000],
    [4, 'Alice Johnson', 'Female', 25, 50000],
    [5, 'Charlie Brown', 'Male', 40, 80000],
    [6, 'Emma Davis', 'Female', 32, 65000],
    [7, 'Tom Wilson', 'Male', 45, 90000],
    [8, 'Olivia White', 'Female', 29, 60000],
    [9, 'Michael Clark', 'Male', 38, 85000],
    [10, 'Sophia Rodriguez', 'Female', 27, 58000],
    [11, 'Daniel Turner', 'Male', 33, 72000],
    [12, 'Ava Martinez', 'Female', 31, 68000],
    [13, 'William Harris', 'Male', 42, 95000],
    [14, 'Mia Lee', 'Female', 26, 52000],
    [15, 'Ethan Taylor', 'Male', 37, 82000],
    [16, 'Grace Anderson', 'Female', 34, 77000],
    [17, 'Liam Brown', 'Male', 28, 60000],
    [18, 'Chloe Wilson', 'Female', 39, 88000],
    [19, 'Mason Johnson', 'Male', 36, 79000],
    [20, 'Lily Moore', 'Female', 30, 62000]

]

new_employee = [21, 'New Employee', 'Male', 26, 70000]
data.append(new_employee)

salaries = [person[4] for person in data]

average_salary = sum(salaries) / len(salaries)

print(f" This company's average salary is {average_salary:.0f}")

gender_salaries = {'Male': [], 'Female': []}

for employee in data:
    gender = employee[2]
    salary = employee[4]
    gender_salaries[gender].append(salary)

average_of_male_salary = sum(gender_salaries['Male']) / len(gender_salaries['Male'])
average_of_female_salary = sum(gender_salaries['Female']) / len(gender_salaries['Female'])

print(f"Average salary for males: {average_of_male_salary:.0f}")
print(f"Average salary for females: {average_of_female_salary:.0f}")


def print_introduction():
    intro = 'this program will show your salary status'
    message = intro.title()
    print(message)

print_introduction()

employee_name = input("Enter the employee's name: ")
found = False

for g in data:
    if g[1] == employee_name:
        found = True
        if g[-1] <= average_salary:
            print(f'{employee_name}: lower than average')
        else:
            print(f'{employee_name}: higher than average')
if not found:
    print(f'{employee_name} is not exist.')

