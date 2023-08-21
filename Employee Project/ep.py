employees = []
projects = []
departments =[]

def save_all_employees(emps):
    pass

def load_employees():
    # check for the existence of pickle file/s
    # If they exist, then load data from them, else from the csv file
    pass

def load_projects():
    # load data from the csv file
    pass

def load_departments():
    # load data from the csv file
    pass

def load_data():
    load_employees()
    load_projects()
    load_departments()

# add constructors for all the classes

class Employee:
    def compute_bonus(self):
        pass
    
    def get_immediate_subordinates(self):
        pass

    def get_all_subordinates(self):
        pass

    def get_hourly_salary(self):
        pass

    def get_projects_assigned(self):
        pass

    def __str__(self):
        # Override __str__() for all the classes
        pass

    

class Project:
    def __str__(self):
        pass

    def get_points(self):
        pass

class Department:
    def __str__(self):
        pass


# Create one function for each menu item. These function can be composed.
# They should take the required inputs as parameters and return either a list of object or
# a single object. Some functions may not need to return anything or they may need to return a more
# complicated data structure. Design wisely. 
# No input/output/printing should be performed in these functions.

def list_employees():
    return employees

def list_employees_by_project(project_id):
    return []

def list_departments():
    return departments

def list_projects():
    return projects

def list_employees_by_department(department_id):
    return []

# one function for each menu option

# util function
def print_list(list_):
    for item in list_:
        print(item) # passing a user defined object to print() will only work if __str__() is overridden


def print_menu():
    print('''
==============================================
WELCOME
==============================================
1.list employees
2.list employees by project (user enters project id)
3.list departments
4.list projects
5.list employees of a department (user enters dept id)
6.global search (user enters text)
7.search for employee (user enters text)
8.search for project (user enters text)
9.display immediate subordinates (user enters employee id)
10.display all subordinates (user enters employee id)
11.Load data from disk
12.Save data to disk
13.Edit Employee (user enters employee id)
14.Most overworked employee (max number of projects assigned)
15.Top 3 most overworked employees
16.Compute Employee bonus. Bonus = 10 points (base) + per project points (given in table)
17.List employees by hourly salary (show name and hourly salary)

''')


# main code goes here
load_data()

while True:
    print_menu()
    option = int(input("Enter the option number: "))

    if option == 1:
        emps = list_employees()
        print_list(emps)

    elif option == 2:
        project_id = int(input("Enter the project id: "))
        emps = list_employees_by_project(project_id)
        print_list(emps)

    elif option == 3:
        deps = list_departments()
        print_list(deps)

    elif option == 4:
        projs = list_projects()
        print_list(projs)



