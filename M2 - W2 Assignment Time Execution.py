# Import math package
"""Square root of a positive number"""
import math
import time

# Define a square root function and pass the num as an argument
def sqrt_fun(num) :
    if num < 0 : # If num is less than 0 or negative
        return "???Please Enter a positive number!"
    else :
        return num ** 0.5 # Use an exponential operator

num = int(input("Enter a value:")) # Input can be any number

# Calculate start time
start_time = time.time()

# Call the sqrt_fun() to find the result
result = sqrt_fun(num)

# Calculate end time
end_time = time.time()

# Print the result and time of execution
print("Square root is:", result)
print("Execution time:", end_time - start_time, "seconds")
