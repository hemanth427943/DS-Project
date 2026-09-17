import pandas as pd
# Create a list of lists for hierarchical index
index = [
    ['Engineering', 'Engineering', 'Science', 'Science'],
    ['CSE', 'Ds', 'chemistry', 'Physics']
]
# Create MultiIndex
multi_index = pd.MultiIndex.from_arrays(
    index,
    names=['Department', 'Branch']
)
# Create a Series using the hierarchical index
marks = pd.Series(
    [95, 93, 92, 94],
    index=multi_index
)
print("Original Series:")
print(marks)
# Partial indexing at the outer level
print("\nData for Engineering:")
print(marks.loc['Engineering'])
# Partial indexing at the inner level
print("\nData for CSE:")
print(marks.loc[('Engineering', 'CSE')])
# Selecting a subset using both levels
print("\nData for Science:")
print(marks.loc['Science'])