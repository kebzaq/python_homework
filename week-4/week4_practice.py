import pandas as pd
# Week 4: practice

# Using lock[] and ilock[]
# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [24, 27, 22, 32],
        'Score': [85, 92, 88, 76]}
df = pd.DataFrame(data)

# Select the 'Name' column
print(df['Name'])

# Select rows and specific columns
print(df.loc[0:2, ['Name', 'Age']])

# Select rows by position
print(df.iloc[:2])  # First two rows
print(df.loc[0:2])  # This prints the first 3 rows! It starts with the row with index 0 and continues up to and including the row with index 2.
print(df.iloc[:2]) # This prints the first 2 rows only.  iloc[] works like list slicing.  It does not include the row with index 2.
print(df.loc[[0,2]]) # This prints row 0 and row 2.  You specify a list of the rows you want.  You can't do this with lists!

print(df[df['Age'] > 24])
# print(df[df['Age'] > 24 and df['Score'] >=88])         Doesn't work!  'and' is not a valid operator for Series!
print(df[(df['Age'] > 24) & (df['Score'] >=88)])        # This one does work! It does the boolean AND of corresponding series elements.
# print(df["a" in df['Name']])                          Doesn't work!  The "in" operator doesn't work for Series!
print(df[df['Name'].str.contains("a")])                 # This does work!  
# There are a bunch of useful str functions for Series.  While we're at it:
# df['Name'] = df['Name'].upper()                       Doesn't work!!
df['Name'] = df['Name'].str.upper()                     # Does work! 
print(df)

#  DATA AGGREGATION
# Group data by a column and calculate the sum
data = {'Category': ['A', 'B', 'A', 'B', 'C'],
        'Values': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Group by 'Category' and calculate the sum
grouped = df.groupby('Category').sum()
print(grouped) # grouped is another DataFrame with summary data

# Calculate the mean for each group
mean_values = df.groupby('Category')['Values'].mean()
print(mean_values)

#  advanced aggregation

# Group data by a column and calculate the sum
data = {'Category': ['A', 'B', 'A', 'B', 'C'],
        'Values': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Group by 'Category' and calculate the sum
grouped = df.groupby('Category').sum()
print(grouped) # grouped is another DataFrame with summary data

# Calculate the mean for each group
mean_values = df.groupby('Category')['Values'].mean()
print(mean_values)

# MERGING AND JOINING

# Sample DataFrames
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [1, 2, 4], 'Score': [85, 92, 88]})

# Merge on the 'ID' column
merged_df = pd.merge(df1, df2, on='ID', how='inner')
print(merged_df)  # Inner merge

# Sample DataFrames

df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Date': ['2021-01-01', '2021-01-02', '2021-01-03'],
    'Name': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Date': ['2021-01-01', '2021-01-02', '2021-01-03'],
    'Score': [85, 92, 88]
})

# Merge on both 'ID' and 'Date'
merged_df = pd.merge(df1, df2, on=['ID', 'Date'], how='inner')
print(merged_df)

# Join DataFrames by index
df1 = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie']}, index=[1, 2, 3])
df2 = pd.DataFrame({'Score': [85, 92, 88]}, index=[1, 2, 4])

joined_df = df1.join(df2, how='outer')
print(joined_df)

#  Data Transformatiton

joined_df['bogus']=['x','y','z','w'] # adds a column
print(joined_df)
joined_df['bogus']=joined_df['bogus'] + "_value"  # replaces a column
print(joined_df)
joined_df.drop('bogus', axis=1, inplace=True) # deletes the column.  You need axis=1 to identify that the drop is for a column, not a row
print(joined_df)

import numpy
data = {'Name': ['A','B','C'],'Value':[1,2,3]}
new_df = pd.DataFrame(data)
print(new_df)
new_df['Value'] = new_df['Value'] ** 2  # using an operator
print(new_df)
new_df['Value'] = numpy.sqrt(new_df['Value']) # using a numpy function.  You can't use math.sqrt() on a Series.
print(new_df)
new_df['EvenOdd'] = new_df['Value'].map(lambda x : 'Even' if x % 2 == 0 else 'Odd') # the map method for a Series
print(new_df)
new_df['Value'] = new_df['Value'].astype(int) # type conversion method for a Series
print(new_df)

#  changin column names
joined_df.rename(columns={'Score':'Test Score'}, inplace=True)
print(joined_df)
#  converting a column to an Index
renamed_df=joined_df.set_index('Name')
print(renamed_df)

# sorting a DataFrame
joined_df.sort_values(by='Test Score',ascending=False,inplace=True)
print(joined_df)
# resetting the Index
joined_df.reset_index(inplace=True, drop=True)
print(joined_df)



