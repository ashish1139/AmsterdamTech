# Import math package
import math

# Define a square root function using lambda
sqrt_fun = lambda num: "???Please Enter a positive number!" if num < 0 else num ** 0.5

num = int(input("Enter a value:"))  # Input can be any number

# Call the sqrt_fun() to find the result
result = sqrt_fun(num)

# Print the result
print("Square root is:", result)
