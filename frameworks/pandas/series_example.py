import pandas as pd

# Create a Pandas Series
data = [10, 20, 30, 40, 50]
labels = ['A', 'B', 'C', 'D', 'E']
series = pd.Series(data, index=labels)

# Display the Series
print("Series:")
print(series)

# Access an element by index
print("\nElement at index 'C':", series['C'])

# Perform mathematical operations
print("\nSeries multiplied by 2:")
print(series * 2)

# Filtering based on a condition
print("\nElements greater than 25:")
print(series[series > 25])

# Using built-in Series functions
print("\nSummary statistics:")
print(series.describe())
