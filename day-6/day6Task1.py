# ------------------------------
# TRY - EXCEPT - ELSE - FINALLY
# ------------------------------

# 'a' is a constant value used for division
a = 6

try:
    # Code inside 'try' block:
    # This block contains code that may raise an exception

    print("resource open.")
    # Imagine opening a file, database connection, or network resource here

    # Taking user input
    # input() returns a string, so we convert it to int
    b = int(input("Enter b: "))

    # Risky operation:
    # This can raise ZeroDivisionError if b == 0
    print(a / b)

# ------------------------------
# SPECIFIC EXCEPTION HANDLING
# ------------------------------

except ZeroDivisionError as e:
    # This block executes ONLY if division by zero occurs

    print("Cannot divide by zero", e)

    # Re-raising the exception:
    # This sends the error back to the caller or stops the program
    # Useful when you want to log the error but not silently ignore it
    raise ZeroDivisionError

except ValueError as e:
    # This block executes if input cannot be converted to an integer
    # Example: user enters 'abc'

    print("Please enter a number", e)

except Exception as e:
    # This is a GENERIC exception handler
    # It catches any exception not handled above

    print("Something went wrong", e)

# ------------------------------
# ELSE BLOCK
# ------------------------------

else:
    # Executes ONLY if:
    # - No exception occurred in the try block
    # - try block completed successfully

    print("I will execute when no exception occurs")

# ------------------------------
# FINALLY BLOCK
# ------------------------------

finally:
    # Executes ALWAYS:
    # - Exception occurs or not
    # - Even if exception is re-raised
    # - Even if return or break is used

    # Used for cleanup operations:
    # - Closing files
    # - Closing database connections
    # - Releasing locks or resources

    print("resource closed.")

# ------------------------------
# PROGRAM CONTINUES (if not crashed)
# ------------------------------

print("Bye Bye Program")
