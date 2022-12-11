import pandas as pd

#1. What is pandas and why use it?
# pandas is a package used for tabular data analysis in Python

#2. Give an example of how to import a csv file using pandas
# pd.read_csv("file_name.csv")

#3. Show how to view the first 10 rows of a dataset using pandas
#df.head(10)

#4. Write a Pandas program to compare the elements of the two Pandas Series.
#Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 10]
df1 = pd.Series([2, 4, 6, 8, 10])
df2 = pd.Series([1, 3, 5, 7, 10])

def element_size(a, b):
    equal_size = a.size == b.size
    return equal_size

print(element_size(df1, df2))


#5. Change the first character of each word to upper case in each word of df1
df1 = pd.Series(['hello', 'to', 'cuny', 'class?'])
df1 = df1.str.capitalize()
print(df1)
