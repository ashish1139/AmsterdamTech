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

# Print the result and time of execution
print("Square root is:", result)
print("Execution time:", end_time - start_time, "seconds")



