# Employee data management system project

Create a command line Employee data management system that stores the following data:

### Employee
- Id
- Manager id
- Name
- Salary
- Department id


### Department
- Name
- Id
- HOD id


### Project
- Id 
- Name
- Priority
- deadline
- employees

Allow the user to select from the following menu options: 

For the options that require additional user input, ask for it.

### Menu options
1. list employees
2. list employees by project (user enters project id)
3. list departments
4. list projects
5. list employees of a department (user enters dept id)
6. global search (user enters text)
7. search for employee (user enters text)
8. search for project (user enters text)
9. display immediate subordinates (user enters employee id) 
10. display all subordinates (user enters employee id)
11. Load data from disk
12. Save data to disk
13. Edit Employee (user enters employee id)
14. Most overworked employee (max number of projects assigned)
15. Top 3 most overworked employees
16. Compute Employee bonus. Bonus = 10 points (base) + per project points (given in table)
17. List employees by monthly salary (show name and monthly salary)

Persist all data to disk using the pickle module. The data should be loaded from any pickle files if present.
If no pickle files are present, load the initial data from the csv/json files

#### Use the starter code in `ep.py`


| Priority  | Points |
| ------------- | ------------- |
| 1-3  | 5  |
| 4-6  | 3  |
| 7-10  | 2  |