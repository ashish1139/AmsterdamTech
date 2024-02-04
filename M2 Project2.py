# Import pandas with alias pd
# Import numpy with alias np
# Import seaborn with alias sns
# Import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
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

# Calculate basic statistics (mean, median, standard deviation, min, max, etc.) for each numerical columns
descriptive_stats = round(rest_df.describe(), 2)
print(descriptive_stats)


# Group by Cuisine_Type and calculate Monthly_Revenue of each type
sales_by_type = round(rest_df.groupby("Cuisine_Type")["Monthly_Revenue"].sum(), 2)
print(sales_by_type)

# Creating lists
l1 = ["American", "Italian", "Japanese", "Mexican"]
l2 = [69018.84, 61178.37, 71185.45, 67341.52]

# Creating DataFrame
sales = pd.DataFrame(list(zip(l1, l2)))
sales.columns = ["Type of Cuisine", "Monthly Revenue"]
print(sales)

# Group by Cuisine_Type and calculate Number_of_Customers of each type
customers_by_type = round(rest_df.groupby("Cuisine_Type")["Number_of_Customers"].sum(), 2)
print(customers_by_type)

# Creating lists
l1 = ["American", "Italian", "Japanese", "Mexican"]
l3 = [13682, 12243, 14141, 13205]

# Creating DataFrame
customers = pd.DataFrame(list(zip(l1, l3)))
customers.columns = ["Type of Cuisine", "Number of Customers"]
print(customers)

# Get the propotion for each Cuisine Type
rest_df_props = round(sales_by_type / sum(sales_by_type), 2) 
print(rest_df_props)

# Creating lists
l1 = ["American", "Italian", "Japanese", "Mexican"]
l4 = [0.26, 0.23, 0.26, 0.25]

# Creating DataFrame
proportion = pd.DataFrame(list(zip(l1, l4)))
proportion.columns = ["Type of Cuisine", "Proportion of Revenue"]
print(proportion)

# Pivot for mean Monthly_Revenue for each Cuisine Type
mean_sales_by_type = round(rest_df.pivot_table(values="Monthly_Revenue", index="Cuisine_Type"), 2)
print(mean_sales_by_type)

# Creating lists
l1 = ["American", "Italian", "Japanese", "Mexican"]
l5 = [269.60, 263.70, 271.70, 269.37]

# Creating DataFrame
avg_revenue = pd.DataFrame(list(zip(l1, l5)))
avg_revenue.columns = ["Type of Cuisine", "Average Monthly Revenue"]
print(avg_revenue)

# Sorting of Monthly_Revenue column
print(rest_df.sort_values("Monthly_Revenue"))
print(rest_df.sort_values("Monthly_Revenue", ascending=False))

# Subsetting based on Monthly_Revenue
sub_month_revenue = round(rest_df[rest_df["Monthly_Revenue"] <= 0 ], 2)
print(sub_month_revenue)

# Visualize the relationship between Number of Customers and Monthly Revenue
customers = rest_df["Number_of_Customers"]
revenue =rest_df["Monthly_Revenue"]
plt.plot(customers, revenue, "o", alpha=0.5)
plt.xlabel("Number of Customers")
plt.ylabel("Monthly Revenue")
plt.title("Number of Customers vs. Monthly Income")
plt.show()

plt.plot(revenue, color="red")
plt.xlabel("Monthly Revenue")
plt.title("Monthly Revenue")
plt.show()

# Pivot for mean Monthly_Revenue for each Cuisine Type with indexing Average_Customer_Spending
mean_sales_by_average_spending = rest_df.pivot_table(values="Monthly_Revenue", index="Average_Customer_Spending", columns="Cuisine_Type", fill_value=0, margins=True)
print(mean_sales_by_average_spending)

mean_sales_by_average_spending.plot(kind="line")

# Visualize Menu_Price using histogram
rest_df.plot(x="Menu_Price", y="Number_of_Customers", kind="hist", bins=20, title="Number of Customers vs. Manu Price")

# Show the plot
plt.show()
             
