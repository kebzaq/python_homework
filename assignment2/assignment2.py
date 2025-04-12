import csv
import os
import custom_module
from datetime import datetime

# Task 2: Read a CSV File
def read_employees():
    my_data = {}
    try:
        with open('../csv/employees.csv', 'r') as f:
            csvreader = csv.reader(f)
            # get fields
            fields = next(csvreader)
            my_data["fields"] = fields
            # get rows/data
            rows = [row for row in csvreader]
            my_data["rows"] = rows
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
    else:
        # return dictionary
        return my_data
# create global var
employees = read_employees()
# print data
print("Task 2:", employees)


# Task 3: Find the Column Index
def column_index(column_name):
    return employees["fields"].index(column_name)
employee_id_column = column_index("employee_id")
print("Task 3:", employee_id_column)

# Task 4: Find the Employee First Name
def first_name(row_number):
    first_name_index = column_index("first_name")
    return employees['rows'][row_number][first_name_index]
   
print("Task 4:", first_name(0))

# Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    #  function inside function
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    # filters matches
    matches=list(filter(employee_match, employees["rows"]))
    return matches
print("Task 5:", employee_find(1))

# Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
    return list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    # return matches
print("Task 6:", employee_find_2(2))

# Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    last_name_index = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_index])
    return employees['rows']
# print("Task 7:", sort_by_last_name())

# Task 8: Create a dict for an Employee
def employee_dict(emp_values):
    emp_dict = {}
    keys = employees["fields"]
    emp_dict[keys[1]] = emp_values[1]
    emp_dict[keys[2]] = emp_values[2]
    emp_dict[keys[3]] = emp_values[3]
    return emp_dict
print("Task 8:", employee_dict(employee_find(1)[0]))

# Task 9: A dict of dicts, for All Employees
def  all_employees_dict():
    all_emp = {}
    for index, row in enumerate(employees["rows"]):
        emp_dict = {employees["rows"][index][0]: employee_dict(row)}
        all_emp.update(emp_dict)
    return all_emp;

all_emps_dict = all_employees_dict()
print("Task 9:", all_emps_dict)

# Task 10: Use the os Module
def get_this_value():
    return os.getenv("THISVALUE")
print("TASK 10:", get_this_value())

# Task 11: Creating Your Own Module
def set_that_secret(secret):
    return custom_module.set_secret(secret)

print("Task 11: Before:", custom_module.secret)
set_that_secret("code the dream")
print("Task 11: After:", custom_module.secret)

# Task 12: Read minutes1.csv and minutes2.csv

def read_minutes():
    min1 = {}
    min2 = {}
    with open("../csv/minutes1.csv", "r") as f1, open("../csv/minutes2.csv", "r") as f2:
        # minutes-1
        reader_1 = csv.reader(f1)
        fields_1 = next(reader_1)
        rows_1 = [tuple(row) for row in reader_1]
        min1["fields"] = fields_1
        min1["rows"] = list(rows_1)
        # minutes-2
        reader_2 = csv.reader(f2)
        fields_2 = next(reader_2)
        rows_2 = [tuple(row) for row in reader_2]
        min2["fields"] = fields_2
        min2["rows"] = list(rows_2)
    # print(minutes2["rows"][2])
    return min1, min2

minutes1, minutes2 = read_minutes()

# Task 13: Create minutes_set
def create_minutes_set():
    rows_min1 = set(minutes1["rows"])
    rows_min2 = set(minutes2["rows"])
    return rows_min1.union(rows_min2)

minutes_set = create_minutes_set()
print("Task 13:", minutes_set)

#  Task 14: Convert to datetime 
def create_minutes_list():
    converted = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_set))
    return converted

minutes_list = create_minutes_list()
print("Task 14:", minutes_list)

# Task 15: Write Out Sorted List
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    conv_list = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))
    with open("./minutes.csv", "w", newline="") as m1:
        writer = csv.writer(m1)
        writer.writerow(minutes1["fields"])
        writer.writerows(conv_list)
    
    return conv_list;


print("Task 15", write_sorted_list())

