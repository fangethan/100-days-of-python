import pandas as pd
df = pd.read_csv('salaries_by_college_major.csv')

# print(df.head())
# print(df.shape)
# print(df.columns)
# print(df.isna())
# print(df.tail())
      
clean_df = df.dropna()
clean_df.tail()

# print(clean_df)
# print(clean_df['Starting Median Salary'])
# print(clean_df['Starting Median Salary'].max())
print(clean_df['Starting Median Salary'].idxmax())
print(clean_df['Undergraduate Major'].loc[43])
print(clean_df.loc[43])

# What college major has the highest mid-career salary? How much do graduates with this major earn? (Mid-career is defined as having 10+ years of experience).
print(clean_df.loc[clean_df['Mid-Career Median Salary'].idxmax()])

# Which college major has the lowest starting salary and how much do graduates earn after university?
print(clean_df['Undergraduate Major'].loc[clean_df['Starting Median Salary'].idxmin()])

# Which college major has the lowest mid-career salary and how much can people expect to earn with this degree? 
print(clean_df.loc[clean_df['Mid-Career Median Salary'].idxmin()])

spread_col = clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])
clean_df.insert(1, 'Spread', spread_col)
clean_df.head()

low_risk = clean_df.sort_values('Spread')
print(low_risk[['Undergraduate Major', 'Spread']].head())

print(clean_df.groupby('Group').count())

