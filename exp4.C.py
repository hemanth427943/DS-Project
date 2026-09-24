import pandas as pd
# Create the first DataFrame
df1 = pd.DataFrame(
    {
        'Name': ['Lucky', 'Chowdaiah', 'Arun'],
        'Marks': [85, None, 78],
        'Grade': ['A', 'B', None]
    },
    index=[101, 102, 103]
)
# Create the second DataFrame
df2 = pd.DataFrame(
    {
        'Name': ['Lucky', 'Chowdaiah', 'Manju'],
        'Marks': [90, 88, 82],
        'Grade': ['O', 'A', 'B']
    },
    index=[101, 102, 104]
)
print("First DataFrame:")
print(df1)
print("\nSecond DataFrame:")
print(df2)
# Merge DataFrames using index as merge key
merged = pd.merge(
    df1,
    df2,
    left_index=True,
    right_index=True,
    how='outer',
    suffixes=('_DF1', '_DF2')
)
print("\nMerged DataFrame:")
print(merged)
# Combine data using combine_first()
combined = df1.combine_first(df2)
print("\nDataFrame after combine_first():")
print(combined)
