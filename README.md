# M2 Project: 

I am creating this project at the end of Module 2.

# 1. Creation of time decorator:

# Import math package
import math

# Import time package
import time

# Define a square root function using lambda
sqrt_fun = lambda num: "???Please Enter a positive number!" if num < 0 else num ** 0.5

# Input any number
num = int(input("Enter a value:"))  

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

* For presenting CEO
# Calculate basic statistics (mean, median, standard deviation, min, max, etc.) for each numerical columns
descriptive_stats = round(rest_df.describe(), 2)

# Display basic statistics
print(descriptive_stats)

# Group sales by Cuisine_Type 
sales_by_type = round(rest_df.groupby("Cuisine_Type")["Monthly_Revenue"].sum(), 2)

# Display sales by type
print(sales_by_type)

# Creating lists
# List 1: l1
l1 = ["American", "Italian", "Japanese", "Mexican"]
# List 2: l2
l2 = [69018.84, 61178.37, 71185.45, 67341.52]

# Creating sales as dDataframe
sales = pd.DataFrame(list(zip(l1, l2)))

# Calculate sales by group
sales.columns = ["Type of Cuisine", "Monthly Revenue"]

# Display sales by Cuisine_Type
print(sales)

# Group number of customers by Cuisine_Type
customers_by_type = round(rest_df.groupby("Cuisine_Type")["Number_of_Customers"].sum(), 2)

# Display customers by type
print(customers_by_type)

# List 3: l3
l3 = [13682, 12243, 14141, 13205]

# Creating customers dataframe
customers = pd.DataFrame(list(zip(l1, l3)))

# Calculate number of customers by cuisine type
customers.columns = ["Type of Cuisine", "Number of Customers"]

# Display number of customers
print(customers)

# Get the propotion for each Cuisine Type
rest_df_props = round(sales_by_type / sum(sales_by_type), 2)

# Display the proportion 
print(rest_df_props)

# List 4: l4
l4 = [0.26, 0.23, 0.26, 0.25]

# Creating DataFrame
proportion = pd.DataFrame(list(zip(l1, l4)))

# Calculate proportion of revenue by cuisine type
proportion.columns = ["Type of Cuisine", "Proportion of Revenue"]

# Display proportion of revenue
print(proportion)

# Pivot for mean Monthly_Revenue for each Cuisine Type
mean_sales_by_type = round(rest_df.pivot_table(values="Monthly_Revenue", index="Cuisine_Type"), 2)

# Display monthly revenue
print(mean_sales_by_type)

# Create List 5: l5
l5 = [269.60, 263.70, 271.70, 269.37]

# Creating average revenue dataframe
avg_revenue = pd.DataFrame(list(zip(l1, l5)))

# Calculate monthly average revenue
avg_revenue.columns = ["Type of Cuisine", "Average Monthly Revenue"]

# Display average revenue
print(avg_revenue)

# Sorting of Monthly_Revenue column
# Display sorted data
print(rest_df.sort_values("Monthly_Revenue"))

# Display sorted date on decending
print(rest_df.sort_values("Monthly_Revenue", ascending=False))

# As found –ve revenue, subset based on Monthly_Revenue
sub_month_revenue = round(rest_df[rest_df["Monthly_Revenue"] <= 0 ], 2)

# Display subsetting revenue
print(sub_month_revenue)  

# Visualize the relationship between Number of Customers and Monthly Revenue
# Number of customers
customers = rest_df["Number_of_Customers"]
# Revenues
revenue =rest_df["Monthly_Revenue"]
# Show a scatter plot
plt.plot(customers, revenue, "o", alpha=0.5)
# Label of x-axis
plt.xlabel("Number of Customers")
# Label of y-axis
plt.ylabel("Monthly Revenue")
# Title of the plot
plt.title("Number of Customers vs. Monthly Income")
# Show the plot
plt.show()

# Line plot of monthly revenue
plt.plot(revenue, color="red")
# Label of x-axis
plt.xlabel("Monthly Revenue")
# Title of the plot
plt.title("Monthly Revenue")
# Show the plot
plt.show()

# Pivot for mean Monthly_Revenue for each Cuisine Type with indexing Average_Customer_Spending
mean_sales_by_average_spending = rest_df.pivot_table(values="Monthly_Revenue", index="Average_Customer_Spending", columns="Cuisine_Type", fill_value=0, margins=True)

# Display mean sales by average spending
print(mean_sales_by_average_spending)

# Draw a line plot
mean_sales_by_average_spending.plot(kind="line")

# Visualize Menu_Price using histogram
rest_df.plot(x="Menu_Price", y="Number_of_Customers", kind="hist", bins=20, title="Number of Customers vs. Manu Price")

# Show the plot
plt.show()

![image](https://github.com/ashish1139/AmsterdamTech/assets/153742869/3fdcd8f1-f569-4eae-9086-529529f6c379)
![image](https://github.com/ashish1139/AmsterdamTech/assets/153742869/0e2f6140-3ad6-40f6-b8bf-bd3c4c80971c)
# Comments: Our target is to raise revenue. Though some –ve revenue and many ups-downs, but mean revenue looks good which is 268.72.

![image](https://github.com/ashish1139/AmsterdamTech/assets/153742869/1725a443-fc5c-4bd9-bd99-ac0ede23e012)
# Comments:	We see from the graph that the number of customers and revenue are high positively correlated, we should more focus on customer satisfaction.

![image](https://github.com/ashish1139/AmsterdamTech/assets/153742869/558ececa-992f-45f8-a70e-09894421d21a)
![image](https://github.com/ashish1139/AmsterdamTech/assets/153742869/2ab4a00a-3456-46d4-aa30-74dee3144047)
![image](https://github.com/ashish1139/AmsterdamTech/assets/153742869/e170fc38-0ff8-4704-b61f-28b2172fc1a5)
# The compelling story: More customers like Japanese Cuisine, but proportion of American and Japanese are same.
There is no strong appeal regarding menu price.
![image](https://github.com/ashish1139/AmsterdamTech/assets/153742869/a054c7c7-2d7e-4f45-a08b-824ee1c841ad)
![image](https://github.com/ashish1139/AmsterdamTech/assets/153742869/ad5a1e10-b868-490f-b10c-470ab7335e04)










