import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# -----------------------------
# 1. Create / Load Dataset
# -----------------------------
# Replace this with: df = pd.read_csv("your_file.csv")
df = pd.DataFrame({
    "Age": [25, 30, 22, 40, 35, 120, 28, 32, 45, 29],  # 120 is an outlier
    "Salary": [50000, 60000, 52000, 80000, 75000, 200000, 58000, 62000, 90000, 61000],
    "Experience": [2, 5, 1, 10, 7, 25, 3, 6, 12, 4]
})

print("=== Dataset ===")
print(df)

# -----------------------------
# 2. Correlation Analysis
# -----------------------------
print("\n=== Correlation Matrix ===")
corr = df.corr()
print(corr)

# Heatmap visualization
plt.figure(figsize=(6,4))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# -----------------------------
# 3. Outlier Detection (IQR Method)
# -----------------------------
def detect_outliers_iqr(data):
    outliers = {}
    for col in data.columns:
        Q1 = data[col].quantile(0.25)
        Q3 = data[col].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outlier_rows = data[(data[col] < lower_bound) | (data[col] > upper_bound)]
        outliers[col] = outlier_rows

    return outliers

outliers = detect_outliers_iqr(df)

print("\n=== Outliers Detected ===")
for col, rows in outliers.items():
    print(f"\nColumn: {col}")
    print(rows)

# Boxplot to visualize outliers
plt.figure(figsize=(8,5))
sns.boxplot(data=df)
plt.title("Boxplot for Outlier Detection")
plt.show()

# -----------------------------
# 4. Clustering (K-Means)
# -----------------------------
# Scale data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# Apply KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_data)

print("\n=== Clustered Data ===")
print(df)

# Visualize clusters (2D projection)
plt.figure(figsize=(6,5))
plt.scatter(df["Age"], df["Salary"], c=df["Cluster"], cmap='viridis')
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("K-Means Clustering")
plt.show()