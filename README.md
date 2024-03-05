# M2 Project: Presenting Data to Different Teams

I am creating this project at the end of Module 2.

I have considered my first business case as restaurant business. For this purpose, I have considered the dataset “Restaurant_revenue (1).csv”. Then I have prepared different reports to present.

For Data Science/Programming Team Head:

•	I focussed on the following technical details to analyze restaurant revenue data : 

i)	Importing pandas, numpy and matplotlib.pyplot Python packages.
ii)	Loading the csv file.
iii)	Checking if there are any missing values in the dataset
iv)	Checking the column head
v)	Checking the first few rows
vi)	Checking shape, values, columns and index of the dataset

Python codes:

# Import pandas with alias pd
# Import numpy with alias np
# Import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Use the csv dataset of Restaurant_revenue (1) and read in Python
rest_df = pd.read_csv(r"C:\Users\MR ASIS\Restaurant_revenue (1).csv")

# Check each column for missing values
print(rest_df.isna().any())

# Look at column heads of the dataset
print(rest_df.info())

# Look at first few rows of the dataset
print(rest_df.head())

# Look at other properties of the dataset
print(rest_df.shape)
print(rest_df.values)
print(rest_df.columns)
print(rest_df.index)





