import pandas as pd

# 5.1 Pivot Tables
data = [{'Employee': 'Jones', 'Product': 'Widget', 'Region': 'West', 'Revenue': 9000}, \
{'Employee': 'Jones', 'Product': 'Gizmo', 'Region': 'West', 'Revenue': 4000}, \
{'Employee': 'Jones', 'Product': 'Doohickey', 'Region': 'West', 'Revenue': 11000}, \
{'Employee': 'Jones', 'Product': 'Widget', 'Region': 'East', 'Revenue': 4000}, \
{'Employee': 'Jones', 'Product': 'Gizmo', 'Region': 'East', 'Revenue': 5500}, \
{'Employee': 'Jones', 'Product': 'Doohickey', 'Region': 'East', 'Revenue': 2345}, \
{'Employee': 'Smith', 'Product': 'Widget', 'Region': 'West', 'Revenue': 9007}, \
{'Employee': 'Smith', 'Product': 'Gizmo', 'Region': 'West', 'Revenue': 40003}, \
{'Employee': 'Smith', 'Product': 'Doohickey', 'Region': 'West', 'Revenue': 110012}, \
{'Employee': 'Smith', 'Product': 'Widget', 'Region': 'East', 'Revenue': 9002}, \
{'Employee': 'Smith', 'Product': 'Gizmo', 'Region': 'East', 'Revenue': 15500}, \
{'Employee': 'Garcia', 'Product': 'Widget', 'Region': 'West', 'Revenue': 6007}, \
{'Employee': 'Garcia', 'Product': 'Gizmo', 'Region': 'West', 'Revenue': 42003}, \
{'Employee': 'Garcia', 'Product': 'Doohickey', 'Region': 'West', 'Revenue': 160012}, \
{'Employee': 'Garcia', 'Product': 'Gizmo', 'Region': 'East', 'Revenue': 16500}, \
{'Employee': 'Garcia', 'Product': 'Doohickey', 'Region': 'East', 'Revenue': 2458}]
sales = pd.DataFrame(data)
print(sales)

sales_pivot1 = pd.pivot_table(sales,index=['Product','Region'],values=['Revenue'],aggfunc='sum',fill_value=0)
print(sales_pivot1)
# This creates a two level index to show sales by product and region. The revenue values are summed for each product and region.
sales_pivot2 = pd.pivot_table(sales,index='Product',values='Revenue',columns='Region', aggfunc='sum',fill_value=0)
print(sales_pivot2)
# The result here is similar, but instead of a two level index, you have columns to give sales by region.
sales_pivot3 = pd.pivot_table(sales,index='Product',values='Revenue',columns=['Region','Employee'], aggfunc='sum',fill_value=0)
print(sales_pivot3)
# By adding the employee column, you get these revenue numbers broken down by employee.  The fill value is used when there is no corresponding entry.

# 5.2 Using apply()
sales_pivot2['Total'] = sales_pivot2['East'] + sales_pivot2['West'] # adding two columns to make a new one
print(sales_pivot2)
per_employee_sales=sales.groupby('Employee').agg({'Revenue':'sum'})
per_employee_sales['Commission Percentage'] = [0.12, 0.09, 0.1]
per_employee_sales['Commission'] = per_employee_sales['Revenue'] * per_employee_sales['Commission Percentage']
print(per_employee_sales)
# for more complicated
per_employee_sales=sales.groupby('Employee').agg({'Revenue':'sum'})
per_employee_sales['Commission Plan'] = ['A', 'A', 'B']
print(per_employee_sales)

def calculate_commission(row):
    if row['Revenue'] < 10000:
        return 0
    if row['Commission Plan'] == 'A':
        return 1000 + 0.05 * (row['Revenue'] - 10000)
    else:
        return 1400 + 0.04 * (row['Revenue'] - 10000)

per_employee_sales['Commission'] = per_employee_sales.apply(calculate_commission, axis=1)
print(per_employee_sales)

# 5.3: Data cleaning 
# Standardization. For example, you want to represent dates and phone numbers in a standard way.
# Addressing outliers. These are values that appear improbable and were likely entered in error.
# Deduplication.
# Addressing missing values.
# Validation.


# 5.4: Handling Missing data
# isnull(): Find the rows where data is missing.
# dropna(): Removes rows or columns with missing data.
# fillna(): Replaces missing values with specified values.
import pandas as pd

# Sample DataFrame with missing values
data = {'Name': ['Alice', 'Bob', None, 'David'],
        'Age': [24, 27, 22, None],
        'Score': [85, None, 88, 76]}
df = pd.DataFrame(data)

# Find rows with missing data
df_missing = df[df.isnull().any(axis=1)]
print(df_missing)
# Remove rows with missing data
df_dropped = df.dropna()
print(df_dropped)

# Replace missing data with default values
df_filled = df.fillna({'Age': 0, 'Score': df['Score'].mean()})
print(df_filled)

# 5.5: Data Transformation
# Converting data types (e.g., strings to integers).
# Reformatting date strings into datetime objects.
# Creating new features:
    # Combining existing features (e.g., Age and YearsOfExperience to create AgeGroup).
    # Extracting features from existing ones (e.g., extracting Year and Month from a Date column).
    # Generating interaction features (e.g., multiplying two features).
# Data Discretization:
    # Binning continuous variables into discrete categories (e.g., age ranges, income brackets).
    # Using techniques like pd.cut() or pd.qcut().

# Sample DataFrame with mixed data types
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': ['24', '27', '22'],
        'JoinDate': ['2023-01-15', '2022-12-20', '2023-03-01']}
df = pd.DataFrame(data)

# Convert 'Age' column to integers
df['Age'] = df['Age'].astype(int)

# Convert 'JoinDate' column to datetime
df['JoinDate'] = pd.to_datetime(df['JoinDate'])

print(df.dtypes)  # Verify data types
print(df)

# Sample DataFrame

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Location': ['LA', 'LA', 'NY'],
        'JoinDate': ['2023-01-15', '2022-12-20', '2023-03-01']}
df = pd.DataFrame(data)

# Convert 'Location' abbreviations into full names

df['Location'] = df['Location'].map({'LA': 'Los Angeles', 'NY': "New York"})
print(df)

data = {'Name': ['Tom', 'Dick', 'Harry', 'Mary'], 'Phone': [3212347890, '(212)555-8888', '752-9103','8659134568']}
df = pd.DataFrame(data)
df['Correct Phone'] = df['Phone'].astype(str)

def fix_phone(phone):
    if phone.isnumeric():
        out_string = phone
    else:
        out_string = ''
        for c in phone:
            if c in '0123456789':
                out_string += c
    if len(out_string) == 10:
        return out_string
    return None
    
df['Correct Phone'] = df['Correct Phone'].map(fix_phone)
print(df)

# change all of the data
data = {'Name': ['Alice', 'Bob', 'Charlie'],
	'Age': [20, 22, 43]}

df = pd.DataFrame(data)

# Increase the age by 1 as a new year has passed
df['Age'] = df['Age'] + 1
print(df)

# Data discretization
a = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Location': ['LA', 'LA', 'NY'],
        'Grade': [78, 40, 85]}
df = pd.DataFrame(data)

# Convert grade into three catagories, "bad", "okay", "great"

df['Grade'] = pd.cut(df['Grade'], 3, labels = ["bad", "okay", "great"])
print(df)

# 5.6: Removing Duplicates
# drop_duplicates(): Removes duplicate rows based on one or more columns. 
# Why:
# Prevents redundant information in analysis.
# Improves data quality and storage efficiency.
# Ensures unique data for accurate insights.

# Sample DataFrame with duplicates
data = {'Name': ['Alice', 'Bob', 'Alice', 'David'],
        'Age': [24, 27, 24, 32],
        'Score': [85, 92, 85, 76]}
df = pd.DataFrame(data)

# Identify and remove duplicates
df_cleaned = df.drop_duplicates()
print(df_cleaned)

# Remove duplicates based on 'Name' column
df_cleaned_by_name = df.drop_duplicates(subset='Name')
print(df_cleaned_by_name)

# 5.7: Handling Outliers
#  Replace outliers with statistical measures like the median.

# Replace outliers in 'Age' (e.g., Age > 100 or Age < 0)
df['Age'] = df['Age'].apply(lambda x: df['Age'].median() if x > 100 or x < 0 else x)

print("DataFrame after handling outliers:")
print(df)

