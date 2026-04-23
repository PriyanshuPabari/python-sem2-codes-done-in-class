
#      Write a Pandas program to get the powers of an array values element-wise. 
# Note: First array elements raised to powers from second array
# Sample data: {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
# Expected Output:
# X Y Z
# 0 78 84 86
# 1 85 94 97
# 2 96 89 96
# 3 80 83 72
# 4 86 86 83 

#have to do like 7 to the power 8 and not 78 to the power 84

import pandas as pd

# Data
df = pd.DataFrame({
    'X': [78, 85, 96, 80, 86],
    'Y': [84, 94, 89, 83, 86],
    'Z': [86, 97, 96, 72, 83]
})

print("Original Data:\n", df)

result = df.copy()

for col in result.columns:
    result[col] = [int(str(x)[0]) ** int(str(x)[1]) for x in result[col]]

print("\nResult (digit-wise power):\n", result)