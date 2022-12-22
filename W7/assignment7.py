# Assignment 7

## Import Packages
import pandas as pd

## Intoduction
'''
The data I chose was a list of environmental cleanup sites from the open NYC data source you provided. I chose it because it was
a popular data set per the open NYC site and it is a manageable file size at under 1MB. It is available at 
https://data.cityofnewyork.us/Environment/OER-Cleanup-Sites/3279-pp7v
'''

## Data Exploration

# load data from github
df = pd.read_csv("https://raw.githubusercontent.com/adavidowitz100/DATA602/main/W7/OER_Cleanup_Sites.csv")

print(df.head())
print(df.shape)
print(df.info())

'''
After loading the data, there does not appear to be any non-categorical numeric data. As a result there aren't any summary statistics
to generate except counts. The data set seems relatively dense with no null values in most columns. Some variables are not flat and contain a concatenation
of multiple values.
(OER Project Numbers, NTA)
'''

# showing missing data by column
print(df.isna().sum())
# out of 1319 sites 10 sites have missing lat/long and other location data missing while 59 are missing census tracts and BIN

# Demonstrating counts of site by borough showing Brooklyn with the most and Staten Island(surprisingly for a place famous for a landfill)
# with the least
per_borough = df['Borough'].value_counts()
print(per_borough)


## Data Wrangling

#Create a subset of your original data and perform the following.
df_sub = df.iloc[:, 0:10]
print(df_sub.head())

# 1. Modify multiple column names.
df_sub = df_sub.rename(columns={"OER Project Numbers": "OER_PN", "Project Name": "Project_Name",
"Project-Specific Document Repository page": "repo", "Street Number": "ST_Number", "Street Name": "ST_Name",
"OER Program": "OER_Program"})
df_sub = df_sub.rename(str.lower, axis='columns')
print(df_sub.columns)

# 2. Look at the structure of your data – are any variables improperly coded? Such as strings or characters? 
# Convert to correct structure if needed.

df_sub['borough'] = pd.Categorical(df_sub.borough)
df_sub['phase'] = pd.Categorical(df_sub.phase)
df_sub['class'] = pd.Categorical(df_sub['class'])
print(df_sub.info())
print (df_sub['borough'].cat.categories)
print (df_sub['phase'].cat.categories)
print (df_sub['class'].cat.categories)

# 3. Fix missing and invalid values in data.
# there is no missing or invalid values

# 4. Create new columns based on existing columns or calculations.
df_sub["st_num_name"] = df_sub["st_number"] + " " + df_sub["st_name"]
print(df_sub["st_num_name"].head())

# 5. Drop column(s) from your dataset.
df_sub = df_sub.drop(["st_number", "st_name"], axis=1)
print(df_sub.columns)

# 6. Drop a row(s) from your dataset.
df_sub = df_sub.drop(labels=[100, 101, 142], axis=0)
print(df_sub.shape)

# 7. Sort your data based on multiple variables.
df_sub = df_sub.sort_values(by=["borough", "phase"])

# 8. Filter your data based on some condition.
df_sub = df_sub[df_sub["borough"] == "Queens"]
print(df_sub.head())

# 9. Convert all the string values to upper or lower cases in one column.
df_sub["borough"] = df_sub["borough"].str.upper
print(df_sub.head())

# 10. Check whether numeric values are present in a given column of your dataframe.
print(10, "burough", pd.to_numeric(df_sub['borough'], errors='coerce').notnull().all())
print(10, "phase", pd.to_numeric(df_sub['phase'], errors='coerce').notnull().all())

# 11. Group your dataset by one column, and get the mean, min, and max values by group. Groupby() agg() or .apply()
borough_count = df_sub.groupby("borough").count()
print(borough_count)

# 12. Group your dataset by two columns and then sort the aggregated results within the groups.
borough_phase_count = df_sub.groupby(["borough", "phase"]).count()
borough_phase_count = borough_phase_count.sort_values(by="class", ascending=False)
print(borough_phase_count)