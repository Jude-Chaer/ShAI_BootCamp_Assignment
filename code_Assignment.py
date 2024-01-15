import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import time
# Load your dataset
df = pd.read_csv('/content/Salaries.csv')
df.head()
df.columns
num_rows, num_cols = df.shape
#1.Basic Data Exploration:
print("Task 1:\n")
print("Number of rows:", num_rows)
print("Number of columns:", num_cols)
print("\n")

data_types = df.dtypes
print("data types:")
print(data_types.to_string())
print("\n")

missing_values = df.isnull().sum()
print("missing values:")
print(missing_values.to_string())

#2.Descriptive Statistics:
print("\nTask 2:\n")
'''the task is not clear on what is the "salary" is, so i will use the "TotalPayBenefits"
   witch will give weird results (for the salary rage for example) because there is 
   a nigative value'''
mean_salary = df['TotalPayBenefits'].mean()
median_salary = df['TotalPayBenefits'].median()
mode_salary = df['TotalPayBenefits'].mode().values[0]
min_salary = df['TotalPayBenefits'].min()
max_salary = df['TotalPayBenefits'].max()
# Print the results
print("Mean salary:", mean_salary)
print("Median salary:", median_salary)
print("Mode of salary:", mode_salary)
print("Minimum salary:", min_salary)
print("Maximum salary:", max_salary)
print("\n")

salary_range = df['TotalPayBenefits'].max() - df['TotalPayBenefits'].min()
print("Salary range:", salary_range)
print("\n")

salary_std = df['TotalPayBenefits'].std()
print("Standard deviation of salaries:", salary_std)

#3.Data Cleaning:
print("\nTask 3:\n")
'''I choose the fill the missing values in the "Benefits" column with 0
   because the the "TotalPayBenefits" and the "TotalPay" for these rows are the same'''
df['Benefits'].fillna(0, inplace=True)
print('the missing values in the "Benefits" column are filled with 0')

#4.Basic Data Visualization:
print("\nTask 4:\n")
# Create a histogram to visualize the distribution of salaries
plt.hist(df['TotalPayBenefits'], bins=10)
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.title('Distribution of Salaries')
plt.show()

# Create a pie chart to represent the proportion of employees in different departments
department_counts = df['JobTitle'].value_counts()
#by default i will not show the lables because it will slow the code and they rae not readable

#comment out the next line to show lables
#plt.pie(department_counts, labels=department_counts.index, autopct='%1.1f%%')

#please comment the next line if you showed the previos line
plt.pie(department_counts)

plt.axis('equal')
plt.title('Proportion of Employees in Different Departments')
plt.show()

#5.Grouped Analysis: 
print("\nTask 5:\n")

average_salary_by_department = df.groupby('JobTitle')['TotalPayBenefits'].mean()
#to show all values add ".to_string()" like below
print(average_salary_by_department)
print("\n")

# Compare the average salaries across different groups
average_salary_by_year = df.groupby('Year')['TotalPayBenefits'].mean()
print(average_salary_by_year.to_string())

#6.Simple Correlation Analysis: 
print("\nTask 6:\n")

# again the salary is TotalPayBenefits
correlation = df['TotalPayBenefits'].corr(df['BasePay'])
print("Correlation between salary and base pay:", correlation)

plt.scatter(df['BasePay'], df['TotalPayBenefits'])
plt.xlabel('Base Pay')
plt.ylabel('Salary')
plt.title('Relationship between Salary and Base Pay')
plt.show()


#7.Simple Correlation Analysis:
print("\nTask 7:\n")

print(f"""a brief report summarizing the findings:
The dataset contains {num_rows} rows and {num_cols} columns.
The data types of the columns include
{data_types.to_string()}
The mean salary is {mean_salary}, the median salary is {median_salary}, and the mode is {mode_salary}.
the minimum salary is {min_salary} and max salary is {max_salary}.
The range of salaries is {salary_range} and the standard deviation is {salary_std}.""")