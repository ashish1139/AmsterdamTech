# Import math package
"""Square root of a positive number"""
import math

# Define a square root function and pass the num as an argument
def sqrt_fun(num) :
    if num < 0 : # If num is less than 0 or negative
        return "???Please Enter a positive number!"
    else :
        return num ** 0.5 # Use an exponential operator

num = int(input("Enter a value:")) # Input can be any number

# Call the sqrt_fun() to find the result
result = sqrt_fun(num)

# Print the result
print("Square root is:", result)
