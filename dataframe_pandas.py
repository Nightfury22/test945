import pandas as pd
pd.set_option('display.max_columns', None)
from datetime import datetime
data = {
    'EmployeeID': [1, 2, 3, 4, 5],

    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],

    'Department': ['HR', 'IT', 'IT', 'HR', 'Finance'],

    'Salary': [60000, 70000, 80000, 65000, 75000],

    'JoiningDate': ['2020-01-15', '2019-06-20', '2018-07-23', '2020-02-10', '2021-03-15'],

    'PerformanceScore': [3, 4, 2, 5, 3]
}
# How can you calculate the average salary for each department?
df = pd.DataFrame(data)
print(df)
average_salary_per_dept = df.groupby('Department')['Salary'].mean().reset_index()
print(average_salary_per_dept)

#2 Write a function to find the employee with the highest performance score in each department.

def highest_performance_employee_per_dept(df):
    # Group by Department and find the row with the maximum PerformanceScore
    idx = df.groupby('Department')['PerformanceScore'].idxmax()

    # Use the index to retrieve the rows with the highest performance score
    highest_performance_employees = df.loc[idx, ['Department', 'EmployeeID', 'Name', 'PerformanceScore', 'Salary']]

    return highest_performance_employees

# Call the function and print the result
result = highest_performance_employee_per_dept(df)
print(result)

#33. How would you add a new column that represents the number of years each employee has been with the company based on the 'JoiningDate'?


# Convert 'JoiningDate' to datetime format
df['JoiningDate'] = pd.to_datetime(df['JoiningDate'])

# Calculate number of years of service
today = datetime.today()
df['YearsInCompany'] = (today - df['JoiningDate']).dt.days // 365

# Display the updated DataFrame
print(df)

#4 Create a pivot table to display the total salary and average performance score for each department.

it_high_performance = df[(df['Department'] == 'Finance') & (df['PerformanceScore'] > 2)]
it_high_performance1 = df[(df['Department'] == 'HR') & (df['PerformanceScore'] > 2)]

print(it_high_performance)
print(it_high_performance1)

#Describe how to perform an inner merge of this DataFrame with another DataFrame containing employee bonus information based on 'EmployeeID'.
data_bonus = {
    'EmployeeID': [1, 2, 3, 4, 5],
    'Bonus': [5000, 6000, 4000, 5500, 7000],
    'Salary': [60000, 70000, 80000, 65000, 75000]
}

df_bonus = pd.DataFrame(data_bonus)
# Inner merge based on 'EmployeeID'
merged_df = pd.merge(df, df_bonus, on='Salary', how='inner')

print(merged_df)
#How can you calculate the cumulative sum of the 'PerformanceScore' column grouped by 'Department'?
df['cumulative_sum_Performance_score'] = df.groupby('Department')['PerformanceScore'].cumsum()
print(df)
#Write a function to rank employees within each department based on their 'Salary'.
df['RankEmployeesDept'] = df.groupby('Department')['Salary'].rank(ascending=False)
print(df)

#How can you filter the DataFrame to show only employees who have been with the company for more than 2 years?

filtered_df = df[df['YearsInCompany'] > 4]

print(filtered_df)