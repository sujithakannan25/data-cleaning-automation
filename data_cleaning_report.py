import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("=" * 50)
print("DATA CLEANING & REPORTING AUTOMATION")
print("=" * 50)

# ===== SAMPLE DIRTY DATA =====
data = {
    'Name': ['Alice', 'Bob', None, 'David', 'Bob',
              'Frank', None, 'Henry', 'Alice', 'Jack'],
    'Age': [25, 30, 22, None, 30,
             28, 35, None, 25, 40],
    'Salary': [50000, 60000, 45000, 70000, 60000,
                None, 80000, 55000, 50000, 90000],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'IT',
                   'HR', 'Finance', 'Finance', 'HR', None],
    'Score': [85, 90, None, 78, 90,
               88, 92, None, 85, 95]
}

df = pd.DataFrame(data)

print("\nBEFORE CLEANING:")
print(df)
print(f"\nMissing Values:\n{df.isnull().sum()}")

# ===== CLEANING - Fixed for Python 3.13 =====
print("\n" + "=" * 50)
print("CLEANING PROCESS...")
print("=" * 50)

# Fix 1: inplace panna maatom - direct assign pannrom
df['Name'] = df['Name'].fillna('Unknown')
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Department'] = df['Department'].fillna('General')
df['Score'] = df['Score'].fillna(df['Score'].mean())
print("Missing values fixed!")

# Fix 2: Duplicates
before = len(df)
df = df.drop_duplicates()
after = len(df)
print(f"Duplicates removed: {before - after} rows deleted!")

# Fix 3: Int conversion - NaN safe way
df['Age'] = df['Age'].round(0).astype('Int64')
df['Salary'] = df['Salary'].round(0).astype('Int64')
print("Data types corrected!")

print("\nAFTER CLEANING:")
print(df)
print(f"\nMissing Values After: {df.isnull().sum().sum()}")

# ===== AUTOMATED REPORT =====
print("\n" + "=" * 50)
print("AUTOMATED REPORT SUMMARY")
print("=" * 50)
print(f"Total Employees   : {len(df)}")
print(f"Average Age       : {df['Age'].mean():.1f}")
print(f"Average Salary    : {df['Salary'].mean():,.0f}")
print(f"Average Score     : {df['Score'].mean():.1f}")
print(f"Top Department    : {df['Department'].value_counts().index[0]}")
print(f"Highest Salary    : {df['Salary'].max():,}")
print(f"Lowest Salary     : {df['Salary'].min():,}")

print("\nDepartment wise Salary:")
print(df.groupby('Department')['Salary'].mean().round(0))

# ===== CHARTS =====
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('Automated Data Report', fontsize=16, fontweight='bold')

dept_count = df['Department'].value_counts()

axes[0,0].bar(dept_count.index, dept_count.values,
              color=['blue','green','orange','red'])
axes[0,0].set_title('Employees per Department')
axes[0,0].set_xlabel('Department')
axes[0,0].set_ylabel('Count')

axes[0,1].hist(df['Salary'].dropna(), bins=5,
               color='green', edgecolor='black')
axes[0,1].set_title('Salary Distribution')
axes[0,1].set_xlabel('Salary')
axes[0,1].set_ylabel('Frequency')

dept_salary = df.groupby('Department')['Salary'].mean()
axes[1,0].bar(dept_salary.index, dept_salary.values, color='purple')
axes[1,0].set_title('Avg Salary by Department')
axes[1,0].set_xlabel('Department')
axes[1,0].set_ylabel('Avg Salary')

axes[1,1].pie(dept_count.values, labels=dept_count.index,
              autopct='%1.1f%%')
axes[1,1].set_title('Department Distribution')

plt.tight_layout()
plt.savefig('C:/Users/sujit/OneDrive/Desktop/data_report.png')
plt.show()

print("\nReport saved: data_report.png")
print("All Done! Ready to Submit!")
