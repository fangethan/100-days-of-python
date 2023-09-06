import pandas as pd
import matplotlib.pyplot as plt

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

# Given that the TAG serves as our category column, can you figure out how to count the number of posts per language? 
print(file.groupby("TAG").sum())

# Can you count how many months of posts exist for each programming language?
print(file.groupby("TAG").count())

print(file['DATE'][1])
print(type(file['DATE'][1]))
print(file.DATE[1])
print(type(file.DATE[1]))

file.DATE = pd.to_datetime(file.DATE)
print(file.head())

# test_df = pd.DataFrame({'Age': ['Young', 'Young', 'Young', 'Young', 'Old', 'Old', 'Old', 'Old'],
#                         'Actor': ['Jack', 'Arnold', 'Keanu', 'Sylvester', 'Jack', 'Arnold', 'Keanu', 'Sylvester'],
#                         'Power': [100, 80, 25, 50, 99, 75, 5, 30]})
# print(test_df)
# pivoted_df = test_df.pivot(index='Age', columns='Actor', values='Power')
# print(pivoted_df)

reshaped_df = file.pivot(index="DATE", columns="TAG", values="POSTS" )
reshaped_df.fillna(0, inplace=True) 
print(reshaped_df)

plt.plot(reshaped_df.index, reshaped_df.java)
# plt.plot(reshaped_df.index, reshaped_df['java'])
roll_df = reshaped_df.rolling(window=6).mean()
 
plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
 
# plot the roll_df instead
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column], 
             linewidth=3, label=roll_df[column].name)
 
plt.legend(fontsize=16)
