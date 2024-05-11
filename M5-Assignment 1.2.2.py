import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
from scipy.stats import linregress

# Import the data from a csv file save it as a DataFrame called "brexit.csv"
brexit_df = pd.read_csv(r"C:\Users\ASUS\Ashish\brexit.csv")
print(brexit_df.head())

print(brexit_df.info())
print(brexit_df.columns)
print(brexit_df.iloc[:, 1])
print(brexit_df.iloc[:, 2])
print(brexit_df['Question: In hindsight, do you think Britain was right or wrong to vote to leave the EU?'])

brexit_df = brexit_df.rename(columns={'Unnamed: 1': 'Right',
                                      'Unnamed: 2': 'Wrong',
                                      'Question: In hindsight, do you think Britain was right or wrong to vote to leave the EU?': 'Date'})
print(brexit_df.columns)
print(brexit_df.head())

brexit_df = brexit_df.iloc[3:]
print(brexit_df.head())

# Check if 'Date' is datetime format
if not pd.api.types.is_datetime64_dtype(brexit_df['Date']):
  # Convert 'Date' column to datetime format (assuming format is '%d/%m/%y')
  brexit_df['Date'] = pd.to_datetime(brexit_df['Date'], format='%d/%m/%y')

# Drop rows with NaN values
brexit_df.dropna(inplace=True)

# Convert 'Right' and 'Wrong' columns to numeric types
brexit_df['Right'] = pd.to_numeric(brexit_df['Right'])
brexit_df['Wrong'] = pd.to_numeric(brexit_df['Wrong'])

# Plot the scatter plot
fig, ax1 = plt.subplots()
ax1.scatter(brexit_df['Date'], brexit_df['Right'], color='b')
ax1.set_xticks(['2016-08-02', '2017', '2018'])
ax1.set_xticklabels(['2016', '17', '18'])
ax1.set_yticks([40, 42, 44, 46, 48, 50])
ax1.set_xlabel('Date')
ax1.tick_params(axis='y', labelleft=None)
# Add annotation for 'Right'
ax1.text(0.6, 0.1, 'Right', transform=ax1.transAxes, fontsize=10, weight='bold')

# Smooth the best fit line for 'Right' column
right_poly_coeffs = np.polyfit(range(len(brexit_df)), brexit_df['Right'], 5)  # Adjust the degree of the polynomial as needed
right_poly = np.poly1d(right_poly_coeffs)
plt.plot(brexit_df['Date'], right_poly(range(len(brexit_df))), color='blue', linestyle='-', linewidth=2)

# Create a twin axis for 'Wrong'
ax2 = ax1.twinx()
ax2.scatter(brexit_df['Date'], brexit_df['Wrong'], color='r')
ax2.set_xticks(['2016-08-02', '2017', '2018'])
ax2.set_xticklabels(['2016', '17', '18'])
ax2.set_yticks([40, 42, 44, 46, 48, 50])
ax2.set_yticklabels([40, 42, 44, 46, 48, 50])
ax2.tick_params(axis='y')
# Add annotation for 'Wrong'
ax2.text(0.65, 0.75, 'Wrong', transform=ax2.transAxes, fontsize=10, weight='bold')

# Smooth the best fit line for 'Wrong' column
wrong_poly_coeffs = np.polyfit(range(len(brexit_df)), brexit_df['Wrong'], 5)  # Adjust the degree of the polynomial as needed
wrong_poly = np.poly1d(wrong_poly_coeffs)
plt.plot(brexit_df['Date'], wrong_poly(range(len(brexit_df))), color='red', linestyle='-', linewidth=2)

# Draw horizontal grid lines for y-ticks on ax1
yticks = ax1.get_yticks()
for y in yticks:
  ax1.axhline(y, color='gray', alpha=0.7)  # Adjust line style and opacity

# Remove top, right, and left spines (borders)
ax1.spines['top'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_visible(True)
ax2.spines['top'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['bottom'].set_visible(True)
plt.title('$\mathbf{Bremorse}$\n"In hindsight, do you think Britain was right or wrong"\nto vote to leave the EU?\n% responding', loc='left', fontsize=10)
plt.show()


