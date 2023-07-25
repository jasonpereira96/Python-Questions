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


# main code goes here

