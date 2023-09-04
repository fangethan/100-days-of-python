import pandas as pd

# Read the .csv file and store it in a Pandas DataFrame called df. 
# Have a look at the read_csv() documentation and try to provide these column names: ['DATE', 'TAG', 'POSTS']
file = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)

# Look at the first and last 5 rows of the DataFrame.
print(file.head())
print(file.tail())

# How many rows and how many columns does it have?
print(file.shape)

# Count the number of entries in each column.
print(file.count())
