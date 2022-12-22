import pandas as pd

df = pd.DataFrame({"col1" :[1, 2 , 3, 4, 5], "col2": ["x", "y","x", "y", "y"]})

print(df["col1"].sum())

print(df.groupby("col2")["col1"].sum())