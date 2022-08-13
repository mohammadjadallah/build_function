# I will show you how my function will work works almost like std method in pandas
# We will build our function to calculate the standard deviation

import pandas as pd

# I will try my function on csv file contains some data
# I will leav the csv file with the same name : dirtydata.csv
data = pd.read_csv("dirtydata.csv")

# The result of std method using pandas
print(data.std())
print(data.std(skipna=False))

print("\n", "#" * 150, "\n")

# Build our function to calculate the standard deviation
def STD(data_set, skipna=True) -> list:
    # Get all columns
    columns = data_set.columns
    # To stor each column with it is value
    all_columns = []
    # Create the for loop
    for col in columns:
        # Check if the column is not String "Object"
        if data_set[col].dtype == 'object':
            continue

        # skipna if True so please dropna values
        if skipna:
            without_nan = data[col].dropna(axis=0)
            # mean = data_set.mean()
            mean = sum(without_nan) / len(without_nan)
            calc = sum(([(x - mean) ** 2 for x in without_nan])) / (len(without_nan) - 1)
            std = round(calc ** 0.5, 6)
            all_columns.append(f"{col}    {std}")

        else:
            # mean = data_set.mean()
            mean = sum(data_set[col]) / len(data_set[col])
            calc = sum(([(x - mean) ** 2 for x in data_set[col]])) / (len(data_set[col]) - 1)
            std = round(calc ** 0.5, 6)
            all_columns.append(f"{col}    {std}")

    return all_columns

# The result of user_defined function STD
print(STD(data))
print(STD(data, skipna=False))

# Finished...
