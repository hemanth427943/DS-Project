import pandas as pd
# Create hierarchical index
index = pd.MultiIndex.from_tuples(
    [
        ('Engineering', 'Civil'),
        ('Engineering', 'EEE'),
        ('Mathematics','Algebra'),
        ('Mathematics','Calculs'),
        ('Science', 'Physics'),
        ('Science', 'Chemistry')
    ],
    names=['Department', 'Branch']
)
# Create tabular data
data = pd.DataFrame(
    {
        '2025': [85, 78, 90, 95, 92, 88],
        '2026': [90, 82, 88, 96, 95, 91]
    },
    index=index
)
print("Original Tabular Data:")
print(data)
# Unstack the inner level
unstacked_data = data.unstack()
print("\nData after Unstack():")
print(unstacked_data)
# Stack the data back
stacked_data = unstacked_data.stack()
print("\nData after Stack():")
print(stacked_data)
