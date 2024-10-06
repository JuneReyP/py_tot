import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('data.csv')

# Display the original dataframe
print("=========================================")
print("Original DataFrame:")
print(df)

# Clean the data
# Fill missing values in the 'Age' column with the mean of the column
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
# df.method({df['Age']: df['Age'].mean()}, inplace=True)
# Display the cleaned dataframe
print("\nCleaned DataFrame:")
print(df)

# analyze the data
# Calculate basic statistics
mean_age = df['Age'].mean()
mean_salary = df['Salary'].mean()

print("\nBasic Statistics:")
print(f"Mean Age: {mean_age}")
print(f"Mean Salary: {mean_salary}")
