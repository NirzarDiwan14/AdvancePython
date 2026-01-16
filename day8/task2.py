"""
EXCEPTION HANDLING DEMO – PRODUCTION-STYLE EXAMPLES

This script demonstrates:
- Arithmetic exceptions
- Type & value exceptions
- Index & key exceptions
- Name & attribute exceptions
- File & import exceptions
- Runtime & custom exceptions
- Proper try / except / else / finally usage
"""

# -------------------------------------------------
# 1. ARITHMETIC EXCEPTIONS
# -------------------------------------------------

try:
    x = 10 / 0
except ZeroDivisionError:
    # Raised when dividing by zero
    print("ZeroDivisionError: Cannot divide by zero")


# -------------------------------------------------
# 2. VALUE ERROR
# -------------------------------------------------

try:
    num = int("abc")
except ValueError:
    # Raised when the type is correct but value is invalid
    print("ValueError: Invalid literal for int()")


# -------------------------------------------------
# 3. TYPE ERROR
# -------------------------------------------------

try:
    result = "10" + 5
except TypeError:
    # Raised when an operation is applied to incompatible types
    print("TypeError: Cannot add str and int")


# -------------------------------------------------
# 4. NAME ERROR
# -------------------------------------------------

try:
    print(undefined_variable)
except NameError:
    # Raised when a variable is not defined
    print("NameError: Variable not defined")


# -------------------------------------------------
# 5. ATTRIBUTE ERROR
# -------------------------------------------------

try:
    num = 10
    num.append(5)
except AttributeError:
    # Raised when an attribute does not exist for an object
    print("AttributeError: 'int' object has no attribute 'append'")


# -------------------------------------------------
# 6. INDEX ERROR
# -------------------------------------------------

try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    # Raised when accessing an index outside valid range
    print("IndexError: List index out of range")


# -------------------------------------------------
# 7. KEY ERROR
# -------------------------------------------------

try:
    data = {"id": 1}
    print(data["name"])
except KeyError:
    # Raised when dictionary key is missing
    print("KeyError: Dictionary key not found")


# -------------------------------------------------
# 8. FILE NOT FOUND ERROR
# -------------------------------------------------

try:
    open("missing_file.txt")
except FileNotFoundError:
    # Raised when file does not exist
    print("FileNotFoundError: File not found")


# -------------------------------------------------
# 9. PERMISSION ERROR
# -------------------------------------------------

try:
    open("/root/secret.txt")
except PermissionError:
    # Raised when access permissions are insufficient
    print("PermissionError: Permission denied")
except FileNotFoundError:
    # For systems where the file path doesn't exist
    print("File not found instead of permission issue")


# -------------------------------------------------
# 10. IMPORT ERROR / MODULE NOT FOUND ERROR
# -------------------------------------------------

try:
    import imaginary_module
except ModuleNotFoundError:
    # Raised when a module cannot be imported
    print("ModuleNotFoundError: Module not found")


# -------------------------------------------------
# 11. RUNTIME ERROR
# -------------------------------------------------

try:
    raise RuntimeError("Something went wrong at runtime")
except RuntimeError as e:
    # Raised when an error doesn't fit other categories
    print(f"RuntimeError: {e}")


# -------------------------------------------------
# 12. CUSTOM (USER-DEFINED) EXCEPTION
# -------------------------------------------------

class InsufficientBalanceError(Exception):
    """Raised when withdrawal amount exceeds balance"""
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance")
    return balance - amount

try:
    withdraw(1000, 5000)
except InsufficientBalanceError as e:
    print(f"Custom Exception: {e}")


# -------------------------------------------------
# 13. MULTIPLE EXCEPT BLOCKS
# -------------------------------------------------

try:
    value = int(None)
except TypeError:
    print("TypeError: int() argument must be a string or number")
except ValueError:
    print("ValueError: Conversion failed")


# -------------------------------------------------
# 14. MULTIPLE EXCEPTIONS IN ONE BLOCK
# -------------------------------------------------

try:
    value = int("abc")
except (ValueError, TypeError):
    print("Multiple Exception Catch: Conversion failed")


# -------------------------------------------------
# 15. ELSE BLOCK
# -------------------------------------------------

try:
    x = int("10")
except ValueError:
    print("Conversion error")
else:
    # Executes only if no exception occurs
    print("Else Block: Conversion successful")


# -------------------------------------------------
# 16. FINALLY BLOCK
# -------------------------------------------------

try:
    file = open("sample.txt", "w")
    file.write("Hello")
except IOError:
    print("IOError: File write error")
finally:
    # Always executes, used for cleanup
    file.close()
    print("Finally Block: File closed")


# -------------------------------------------------
# 17. EXCEPTION CHAINING
# -------------------------------------------------

try:
    int("xyz")
except ValueError as e:
    # Preserve original exception context
    raise RuntimeError("Failed to convert string to int") from e
