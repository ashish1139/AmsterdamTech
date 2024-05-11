import numpy as np
import matplotlib.pyplot as plt

# Create numpy arrays x and y with 1000 values ranging from -10 to 10
x = np.linspace(-10, 10, 1000)
y = np.linspace(-10, 10, 1000)

# Define the z_func function
def z_func(x, y):
    z = np.sin(np.sqrt(x**2 + y**2)) / np.sqrt(x**2 + y**2)
    return z

# Calculate the z array using the z_func function
z = z_func(x, y)

# Create Scatter plot
fig, ax = plt.subplots()
sc = ax.scatter(x, y, c=z, cmap='coolwarm')
plt.colorbar(sc, ax=ax, label='Z value')
ax.set_title('Advanced Scatter Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
plt.show()

# Save the plot
fig.savefig('advanced_scatter_plot.png', dpi=300)

