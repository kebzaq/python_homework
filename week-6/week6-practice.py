import pandas as pd
import re

#  6.1 Handling Missing Data
# Sample DataFrame
data = {'Name': ['Alice', None, 'Charlie', 'David'],
        'Age': [24, None, 22, 35],
        'Salary': [50000, 60000, None, None]}
df = pd.DataFrame(data)

# Drop rows with missing data
df_dropped = df.dropna()

# Replace missing values
df_filled = df.fillna({'Name': 'Unknown', 'Age': df['Age'].mean(), 'Salary': 0})

print("DataFrame with missing data handled:")
print(df_filled)

# 6.2 Data Transformation

# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': ['24', '27', '22'],
        'Join_Date': ['2023-01-15', '2022-12-20', '2023-03-01']}
df = pd.DataFrame(data)
print(df.info())

# Convert 'Age' to integer
df['Age'] = df['Age'].astype(int)

# Convert 'Join_Date' to datetime
df['Join_Date'] = pd.to_datetime(df['Join_Date'])

print("Transformed DataFrame:")
print(df)
print(df.info())

# 6.3 Using Regular Expressions

# compile the regular expression
# This regex captures the username from a gmail address as a subgroup
# It requires one or more word chacaters at the beginning, then any number of words, digits, periods and '-''s
# The first `()` will be available a group(1) if there is a match
gmail = re.compile(r'(\w+[\w\d\.\-]*)@gmail.com')
search_target = 'Boa-Dreamcode.public@gmail.com'
# match the entire string
match = gmail.match(search_target)
# print the group and subgroup
print(match.group()) # => Boa-Dreamcode.public@gmail.com (same as group(0))
print(match.group(1)) # => Boa-Dreamcode.public
# now serch within a longer string
search_target = 'My email is Boa-Dreamcode.public@gmail.com, what is yours?'
match = gmail.search(search_target)
print(match.group()) # => Boa-Dreamcode.public@gmail.com (same as group(0))
print(match.group(1)) # => Boa-Dreamcode.public

# using replace()
df = pd.DataFrame({
   'phone_number': ['(123) 456-7890', '+1-555-123-4567', '555.456.7890']
})
# Remove all non-digit characters
df['phone_number_clean'] = df['phone_number'].str.replace(r'\D', '', regex=True)
print(df)

# Removing html tags from scraped data.
df = pd.DataFrame({
    'html_content': [
        '<p>This is a paragraph.</p>',
        '<div>Some <strong>bold</strong> text</div>'
    ]
})
# <.*?> matches <, then any characters as few as possible (.*? is a non-greedy match), then >
df['text_only'] = df['html_content'].str.replace(r'<.*?>', '', regex=True)
print(df)


# USING extract() - only uses regex
df = pd.DataFrame({
    'email': [
        'john.doe@example.com',
        'jane_smith@my-domain.org',
        'user123@anotherdomain.net'
    ]
})
df['domain'] = df['email'].str.extract(r'@(\w+[\w\.-]+)')
print(df)

# USING contains() - get all rows which contain valid emails
df = pd.DataFrame({
    'email': ['test@example.com', 'invalid-email', 'hello@mydomain.org']
})
valid_emails = df[df['email'].str.contains(r'^\w+[\w\.-]+@\w+[\w\.-]+\.\w+$')]
print(valid_emails)

# Combining filters using bitwise operators 
orders = [
    "Order 1: 2x Cheddar, 1x Gouda",
    "Order 2: 3x Stilton, 2x Rye Crackers",
    "Order 3: 2x Saltines",
    "Order 4: 1x Camembert, 2x Jahrlsberg",
    "Order 5: 2x Gouda, 2x Rye Crackers",
    "Order 6: 1x Ritz, 1x Jahrlsberg",
    "Order 7: 1x Parmesan, 1x Brie",
    "Order 8: 3x Saltine Crackers",
    "Order 9: 2x Rye Crackers",
    "Order 10: 2x Mozzarella, 1x Cheddar",
    "Order 11: 1X Water Crackers"
    "Order 12: 3x Blue Cheese",
    "Order 13: 1x Triscuits",
    "Order 14: 1x Butter Crackers, 2x Multigrain Crackers",
    "Order 15: 1x Feta",
    "Order 16: 1x Havarti",
    "Order 17: 2x Wheat Crackers",
    "Order 18: 1x Ricotta",
    "Order 19: 1x Garlic Herb Crackers"
]
orders = pd.Series(orders)
favored_cheeses = orders.str.contains(r'Cheddar|'
                                       r'Stilton|'
                                       r'Camembert|'
                                       r'Jahrlsberg|'
                                       r'Gouda', case=False, regex=True)
favored_crackers = orders.str.contains(r'Ritz|'
                                       r'Triscuit|'
                                       r'Rye Crackers|'
                                       r'Multigrain Crackers|'
                                       r'Water Crackers', case=False, regex=True)
print(orders[favored_cheeses | favored_crackers])
print(orders[favored_cheeses & favored_crackers])
print(orders[~favored_cheeses])

# USING filter() - select or drop matching columns
df = pd.DataFrame({
    'col_2021': [1, 2, 3],
    'col_2022': [4, 5, 6],
    'col_other': [7, 8, 9]
})
# Select columns that end with digits
df_year = df.filter(regex=r'\d+$')  
print(df_year)

# 6.4 Removing Duplicates
# duplicated() - Identifies duplicates
# drop_duplicates() - Removes duplicate rows
# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Alice', 'David'],
        'Age': [24, 27, 24, 35],
        'Salary': [50000, 60000, 50000, 80000]}
df = pd.DataFrame(data)

# Remove duplicates
df_no_duplicates = df.drop_duplicates()

print("DataFrame with duplicates removed:")
print(df_no_duplicates)

# 6.5 Handling Outliers
# Replace outliers in 'Age' (e.g., Age > 100 or Age < 0)
df['Age'] = df['Age'].apply(lambda x: df['Age'].median() if x > 100 or x < 0 else x)

print("DataFrame after handling outliers:")
print(df)

# 6.6 Standardizing Data 
# Standardize 'Name' column
# df['Name'] = df['Name'].str.lower().str.strip()

# Standardize 'City' column with mapping
# df['City'] = df['City'].replace({'ny': 'New York', 'la': 'Los Angeles'})

print("Standardized DataFrame:")
# print(df)

# 6.7 Validating Data Ranges
# Replace invalid ages with NaN
df['Age'] = df['Age'].apply(lambda x: x if 18 <= x <= 65 else None)

# Fill missing values with median
df['Age'] = df['Age'].fillna(df['Age'].median())

print("DataFrame after validating age ranges:")
print(df)

# 6.8 Handling Categorical Data
# Sample DataFrame with categorical data
data = {'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red']}
df = pd.DataFrame(data)

# Label encoding: Convert categories to numbers
df['Color_Label'] = df['Color'].map({'Red': 1, 'Blue': 2, 'Green': 3})

# One-Hot Encoding: Create binary columns for each category
df_encoded = pd.get_dummies(df['Color'], prefix='Color')

print("DataFrame with Categorical Data Handled:")
print(df_encoded)

# 6.9 Handling Inconsistent Data
# Sample DataFrame with inconsistent data
data = {'City': ['New York', 'new york', 'San Francisco', 'San fran']}
df = pd.DataFrame(data)

# Standardize text data (convert to lowercase and strip spaces)
df['City'] = df['City'].str.lower().str.strip()

# Use Regex to replace shorthand names
df['City'] = df['City'].replace({'san fran': 'san francisco'})

print("DataFrame with Inconsistent Data Handled:")
print(df)

# 6.10 Feature Engineering 
# Sample DataFrame with numerical data
data = {'Age': [24, 35, 30, 45, 61]}
df = pd.DataFrame(data)

# Binning Age into age groups
bins = [0, 30, 60, 100]
labels = ['Young', 'Middle-Aged', 'Old']
df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels)

print("DataFrame after Feature Engineering:")
print(df)