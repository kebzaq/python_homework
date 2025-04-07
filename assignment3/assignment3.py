import pandas as pd
import json
import numpy as np

# Task 1: Inttro to Pandas

# 1.1 Create a DF from a dictionary
dict = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

task1_data_frame = pd.DataFrame(dict)
# print(task1_data_frame)

# 1.2 Add anew column
task1_with_salary = task1_data_frame.copy()
task1_with_salary["Salary"] = [70000, 80000, 90000]
# print(task1_with_salary)

# 1.3: Modify an existing column:
task1_older = task1_with_salary.copy()
task1_older["Age"] += 1
# print(task1_older)

# 1.4: SAve the DF as a CSV file
task1_older.to_csv("employees.csv", index=False)


# Task 2: Loading Data from CSV and JSON

# 2.1: read data from csv
task2_employees = pd.read_csv("employees.csv")
# print(task2_employees)

# 2.2: read data from JSON
json_employees = pd.read_json("additional_employees.json", encoding="utf-8")
print(json_employees)

# 2.3: 
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(more_employees)

# Task 3: 
# 3.1: head()
first_three = more_employees.head(3)
print(first_three)

# 3.2: tail()
last_two = more_employees.tail(2)
print(last_two)

# 3.3: shape
employee_shape = more_employees.shape
print(employee_shape)

# 3.4: info()
print(more_employees.info())

# Task 4: Data Cleaning
# 4.1:dirty data
dirty_data = pd.read_csv("dirty_data.csv")
print(dirty_data)
clean_data = dirty_data.copy()
# clean_data["Salary"] - clean_data["Salary"].replace("NaN", pd.NA).fillna("Unknown")

# 4.2: remove duplicates
clean_data = clean_data.drop_duplicates()
print(clean_data)

# 4.3: convert age
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")
print(clean_data)

# 4.4: convert Salary
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"].replace(["unknown", 'n/a'], np.nan), errors="coerce")
print(clean_data)

# 4.5: Fill missing numeric values
clean_data["Age"] = clean_data["Age"].fillna(clean_data["Age"].mean())
clean_data["Salary"] = clean_data["Salary"].fillna(clean_data["Salary"].median())
print(clean_data)

# 4.6: convert date to datetime
clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], errors="coerce")
print(clean_data)

# 4.7: strip extra whitespaces and make uppercase
clean_data["Name"] = clean_data["Name"].str.strip().str.upper()
clean_data["Department"] = clean_data["Department"].str.strip().str.upper()
print(clean_data)