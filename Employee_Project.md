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
2. list employees by project
3. list departments
4. list projects
5. list employees of a department
6. global search
7. search for employee
8. search for project
9. display immediate subordinates
10. display all subordinates
11. Load data from disk
12. Save data to disk
13. Edit Employee

Persist all data to disk using the pickle module. The data should be loaded from any pickle files if present.
If no pickle files are present, load the initial data from the csv/json files
