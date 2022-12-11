import pandas as pd

# Q1
df1 = pd.read_csv("https://raw.githubusercontent.com/data602sps/datasetspractice/main/kobe.csv")
df2 = pd.read_csv("https://raw.githubusercontent.com/data602sps/datasetspractice/main/salarydata.csv")
df3 = pd.read_csv("Civil_Service_List__Active_.csv")
df4 = pd.read_csv("Medallion_Drivers_-_Active.csv")

# Q2
#this displays the first 5 and last 5 rows and as many variable columns that fit in the console
# seems equivalent to calling both head() and tail()
print(df1)
print(df2)
print(df3)
print(df4)

# Q3
print("df1 size", df1.shape,"\n", df1.dtypes)
print("df2 size", df2.shape,"\n", df2.dtypes)
print("df3 size", df3.shape,"\n", df3.dtypes)
print("df4 size", df4.shape,"\n", df4.dtypes)

# Q4
# describe seems to give summary statistics
print(df1.describe())
print(df2.describe())
print(df3.describe())
print(df4.describe())

# Q5
# these print out the first 5 and last 5 rows of the dataframe
print(df1.head())
print(df1.tail())
print(df2.head())
print(df2.tail())
print(df3.head())
print(df3.tail())
print(df4.head())
print(df4.tail())
