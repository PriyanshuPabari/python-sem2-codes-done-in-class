
# Write a Pandas program to find and replace the missing values in a given DataFrame which do not have any valuable information.

import pandas as pd
import numpy as np

# Sample DataFrame (same type as previous question)
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily'],
    'score': [12.5, 9, 16.5, np.nan, 9],
    'attempts': [1, 3, 2, 3, 2],
    'qualify': ['yes', 'no', 'yes', 'no', 'no']
}

df = pd.DataFrame(exam_data)

print("Original DataFrame:\n", df)

# Replace missing values (NaN) with 0
df_filled = df.fillna(0)

print("\nAfter replacing missing values with 0:\n", df_filled)