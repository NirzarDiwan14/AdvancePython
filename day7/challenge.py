import time
from functools import wraps

# -------------------------------------------------------
# RULE OF THUMB FOR DECORATOR ORDER (IMPORTANT)
# -------------------------------------------------------
# Authentication  -> OUTERMOST (runs first)
# Validation      -> Outside
# Logging         -> Outside
# Timing          -> Inside
# Caching         -> Inside
# Business Logic  -> Innermost (actual function)
#
# Reason:
# - We should block unauthorized access early
# - Avoid unnecessary logging/timing for invalid calls
# - Measure only meaningful business logic
# -------------------------------------------------------


# -------------------------------------------------------
# TIMER DECORATOR
# -------------------------------------------------------
# Purpose:
# - Measure how long a function takes to execute
# - Commonly used for performance monitoring
#
# NOTE:
# - Uses *args and **kwargs to support any function signature
# - Returns the original function's return value
# - Uses functools.wraps to preserve metadata
# -------------------------------------------------------

def timer(func):
    @wraps(func)  # Preserves function name, docstring, etc.
    def wrapper(*args, **kwargs):
        # Record start time before function execution
        start = time.time()

        # Execute the original function
        val = func(*args, **kwargs)

        # Record end time after execution
        end = time.time()

        # Print execution time
        print(f"Function {func.__name__} executed in {end - start} seconds.")

        # Return original function's return value
        return val

    return wrapper


# -------------------------------------------------------
# LOGGER DECORATOR
# -------------------------------------------------------
# Purpose:
# - Log when a function starts and ends
# - Used for debugging and tracing execution flow
#
# NOTE:
# - wrap is required to keep original function metadata
# - Should ideally RETURN the function result
# -------------------------------------------------------

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Log before function execution
        print(f"{func.__name__} started.")

        # Call the wrapped function
        result = func(*args, **kwargs)

        # Log after function execution
        print(f"{func.__name__} ended.")

        # Return the function's result (best practice)
        return result

    return wrapper


# -------------------------------------------------------
# FUNCTION WITH MULTIPLE DECORATORS
# -------------------------------------------------------
# Execution order:
# do_something1 = logger(timer(do_something1))
#
# Runtime flow:
# 1. logger.wrapper starts
# 2. timer.wrapper starts
# 3. do_something1 executes
# 4. timer prints execution time
# 5. logger prints end
# -------------------------------------------------------

@logger
@timer
def do_something1():
    # Simulate a 1-second task
    time.sleep(1)


@logger
@timer
def do_something2():
    # Simulate a 2-second task
    time.sleep(2)


# -------------------------------------------------------
# FUNCTION WITH ONLY TIMER DECORATOR
# -------------------------------------------------------

@timer
def do_something3():
    # Simulate a 3-second task
    time.sleep(3)


@timer
def do_something4():
    # Simulate a 4-second task
    time.sleep(4)


# -------------------------------------------------------
# FUNCTION CALLS
# -------------------------------------------------------
# Decorators are triggered ONLY when the function is called
# -------------------------------------------------------

do_something1()
do_something2()
do_something3()
do_something4()

print("All is done.")
