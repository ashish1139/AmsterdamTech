# Import time package to create decorator to measure time execution of a function
import time

def measure_execution_time(func):
    """
    Decorator to measure the execution time of a function.

    Args:
        func: The function to be decorated. We use *args and **kwargs in the decoration.

        Returns:
        A wrapper function that measures the execution time of the decorated function.
        
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print("Execution time: " + str(round(execution_time, 4)) + " seconds")
        return result
    return wrapper

@measure_execution_time
def my_function(n):
    return sum(range(n))

my_function(100000)
