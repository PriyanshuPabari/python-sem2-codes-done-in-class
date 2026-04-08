import numpy as np
import pandas as pd
a=pd.DataFrame({
    "rollno":[101,102,103],
    "Python":[85,90,78],
    "DS":[80,88,92],
    "ML":[82,91,89]
})
print(type(a))
print(a)
print(a["Python"])
print(a[["Python","ML"]])