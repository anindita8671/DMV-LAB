import pandas as pd

# Load dataset (replace with your file path)
# Example: df = pd.read_csv("data.csv")
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", None],
    "Age": [25, None, 30, 22],
    "Salary": [50000, 60000, None, 52000]
})

print("=== Original Data ===")
print(df)

# 1. Check missing values (True/False)
print("\n=== Missing Values (True = Missing) ===")
print(df.isnull())

# 2. Count missing values per column
print("\n=== Missing Values Count ===")
print(df.isnull().sum())

# 3. Percentage of missing values
print("\n=== Missing Values Percentage ===")
missing_percent = (df.isnull().sum() / len(df)) * 100
print(missing_percent)

# 4. Total missing values in dataset
total_missing = df.isnull().sum().sum()
print("\nTotal Missing Values:", total_missing)

# 5. Drop rows with missing values
df_dropped = df.dropna()
print("\n=== Data after Dropping Missing Rows ===")
print(df_dropped)

# 6. Fill missing values
# Fill numeric columns with mean
df_filled = df.copy()
df_filled["Age"].fillna(df_filled["Age"].mean(), inplace=True)
df_filled["Salary"].fillna(df_filled["Salary"].mean(), inplace=True)

# Fill categorical columns with placeholder
df_filled["Name"].fillna("Unknown", inplace=True)

print("\n=== Data after Filling Missing Values ===")
print(df_filled)