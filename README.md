# M2 Project: 

I am creating this project at the end of Module 2.

# 1. Creation of time decorator:

# Import math package
import math
import time

# Define a square root function using lambda
sqrt_fun = lambda num: "???Please Enter a positive number!" if num < 0 else num ** 0.5

num = int(input("Enter a value:"))  # Input can be any number

# Calculate start time
start_time = time.time()

# Call the sqrt_fun() to find the result
result = sqrt_fun(num)

# Calculate end time
end_time = time.time()

# Print the result
print("Square root is:", result)

# Print execution time
print("Execution time:", end_time - start_time, "seconds")

# 2. Presenting Data to Different Teams

I have considered my first business case as restaurant business. For this purpose, I have considered the dataset “Restaurant_revenue (1).csv”. Then I have prepared different reports to present.

# For Data Science/Programming Team Head:

•	I focussed on the following technical details to analyze restaurant revenue data : 

* i)	Importing pandas, numpy and matplotlib.pyplot Python packages.
* ii)	Loading the csv file.
* iii)	Checking if there are any missing values in the dataset
* iv)	Checking the column head
* v)	Checking the first few rows
* vi)	Checking shape, values, columns and index of the dataset

Python codes:

# Import pandas with alias pd
import pandas as pd

# Import numpy with alias np
import numpy as np

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Use the csv dataset of Restaurant_revenue (1) and read in Python
rest_df = pd.read_csv(r"C:\Users\MR ASIS\Restaurant_revenue (1).csv")

# Check each column for missing values
print(rest_df.isna().any())

# Look at column heads of the dataset
print(rest_df.info())

# Look at first few rows of the dataset
print(rest_df.head())

# Display shape of the dataset
print(rest_df.shape)

# Display values of the dataset
print(rest_df.values)

# Display columns of the dataset
print(rest_df.columns)

# Display index of the dataset
print(rest_df.index)





