import pandas as pd

data = [1 ,3 , 5, 7, 9]
s = pd.Series(data, name="numbers")
print(s)

# Series
data2 = pd.Series(['Tom', 'Li', 'Antonio', 'Mary'], index=[5, 2, 2, 3])
print(data2)
# Output:
# 5 Tom
# 2 Li
# 2 Antonio
# 3 Mary
print(data2[2])
# Output:
# 2 Li
# 2 Antonio
# print(data2[1])
# This gives a key error!

data3 = data2.reset_index()
print(data3)
# output:
# 0 Tom
# 1 Li
# 2 Antonio
# 3 Mary


# Creating a DataFrame from a dict
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'San Francisco', 'Chicago']
}
df = pd.DataFrame(data)
print(df)

import numpy as np # load the numpy library
# Create a Pandas DataFrame using NumPy arrays
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df = pd.DataFrame(data, columns=['A', 'B', 'C'])

print(df)

# COnverting columns to numeric
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Height": ["5.5", "unknown", "5.9"],  # "unknown" is not numeric
    "Weight": ["60", "70", "NaN"]        # "NaN" is a missing placeholder
}
df = pd.DataFrame(data)

print("Before conversion:")
print(df)

# Replace placeholders with NaN and convert to numeric
df["Height"] = df["Height"].replace("unknown", pd.NA)
df["Height"] = pd.to_numeric(df["Height"], errors="coerce")
df["Weight"] = pd.to_numeric(df["Weight"], errors="coerce")

print("\nAfter conversion to numeric:")
print(df)

# Handling missing values with fillna()
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Height": ["5.5", "unknown", "5.9"],  # "unknown" is not numeric
    "Weight": ["60", "70", "NaN"]        # "NaN" is a missing placeholder
}
df = pd.DataFrame(data)

print("Before conversion:")
print(df)

# Replace placeholders with NaN and convert to numeric
df["Height"] = df["Height"].replace("unknown", pd.NA)
df["Height"] = pd.to_numeric(df["Height"], errors="coerce")
df["Weight"] = pd.to_numeric(df["Weight"], errors="coerce")

print("\nAfter conversion to numeric:")
print(df)

# Forward and backward fill
data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Sales": [100, np.nan, 150, np.nan, 200]
}
df = pd.DataFrame(data)

print("Original Sales Data:")
print(df)

# Forward fill (propagate last valid observation forward)
df_ffill = df.copy()
df_ffill["Sales"] = df_ffill["Sales"].fillna(method="ffill")

# Backward fill (use next valid observation to fill gaps)
df_bfill = df.copy()
df_bfill["Sales"] = df_bfill["Sales"].fillna(method="bfill")

print("\nForward Fill Result:")
print(df_ffill)

print("\nBackward Fill Result:")
print(df_bfill)

# TExt sttandartization (strip, upper, lower)
data = {
    "Department": [" SALES ", "   HR", "FinanCe  ", "Sales", "MARKETING "],
    "Location": [" New York ", " Boston", "Chicago   ", "  Boston ", "LOS ANGELES"]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Strip whitespace
df["Department"] = df["Department"].str.strip()
df["Location"] = df["Location"].str.strip()

# Convert columns to uppercase
df["Department_upper"] = df["Department"].str.upper()
df["Location_upper"] = df["Location"].str.upper()

# Or lowercase, if you prefer
df["Department_lower"] = df["Department"].str.lower()

print("\nAfter text standardization:")
print(df) 

# COnvertting dates and datetime
# Sample data with dates in various formats and some invalid values
data = {
    "Event": ["Project Start", "Client Meeting", "Beta Release", "Final Launch"],
    "Date": ["2021/01/15", "2021-02-30", "03-15-2021", "April 31, 2021"]  # Some invalid or unusual dates
}
df = pd.DataFrame(data)

print("Before conversion:")
print(df)

# Convert 'Date' to datetime
# errors="coerce" will turn invalid dates into NaT (Not a Time)
df["Date_converted"] = pd.to_datetime(df["Date"], errors="coerce")

print("\nAfter converting to datetime:")
print(df)

# You can check how many values became NaT (invalid dates)
num_invalid_dates = df["Date_converted"].isna().sum()
print(f"\nNumber of invalid dates converted to NaT: {num_invalid_dates}")


# Save a DataFrame to a CSV File

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [26, 31, 36],
    'City': ['New York', 'Los Angeles', 'Chicago'],
    'Salary': [70000, 80000, 90000]
}
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv("employees.csv", index=False)

print("DataFrame saved to employees.csv")