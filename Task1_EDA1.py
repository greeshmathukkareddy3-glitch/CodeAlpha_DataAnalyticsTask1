import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create Dataset
data = {
    "Name": ["Ravi", "Sita", "Ram", "Priya", "John"],
    "Maths": [85, 90, 70, 95, 80],
    "Science": [80, 85, 75, 90, 88]
}

df = pd.DataFrame(data)

print("STUDENT PERFORMANCE DATA")
print(df)

# Step 2: First Five Rows
print("\nFirst Five Rows:")
print(df.head())

# Step 3: Dataset Information
print("\nDataset Information:")
df.info()

# Step 4: Statistical Analysis
print("\nStatistical Analysis:")
print(df.describe())

# Step 5: Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 6: Duplicate Values
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Step 7: Average Marks
print("\nAverage Marks:")
print("Maths:", df["Maths"].mean())
print("Science:", df["Science"].mean())

# Step 8: Visualization
df[["Maths", "Science"]].mean().plot(kind="bar")

plt.title("Average Marks Analysis")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.show()

# Step 9: Final Results
print("\nEDA RESULTS")
print("Total Students:", len(df))
print("EDA Completed Successfully!")