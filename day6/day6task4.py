import os
from contextlib import contextmanager

# -------------------------------------------------------
# PART 1: WITHOUT CONTEXT MANAGER
# -------------------------------------------------------
# Problem:
# - We manually change directories using os.chdir()
# - We MUST remember the original directory
# - We MUST manually switch back every time
# - Error-prone if an exception occurs
# -------------------------------------------------------

print("-" * 32, "without context manager...")

# Save current working directory
cwd = os.getcwd()

# Change directory to "day4"
os.chdir("day4")

# List files in "day4"
print(os.listdir())

# Manually switch back to original directory
os.chdir(cwd)

# Repeat the same steps again for another directory
cwd = os.getcwd()
os.chdir("day5")
print(os.listdir())
os.chdir(cwd)

# ❌ Drawbacks:
# - Code repetition
# - Easy to forget os.chdir(cwd)
# - Unsafe if an exception happens before switching back
# - Not scalable or clean


# -------------------------------------------------------
# PART 2: WITH CONTEXT MANAGER
# -------------------------------------------------------
# Solution:
# - Use a context manager to AUTOMATICALLY
#   1. Save current directory
#   2. Change directory
#   3. Restore directory (even if error occurs)
# -------------------------------------------------------

@contextmanager
def change_dir(destination):
    """
    A custom context manager for safely changing directories.

    destination : str
        Directory path to switch into temporarily.
    """

    # Save the current working directory BEFORE change
    cwd = os.getcwd()

    try:
        # Change to the target directory
        os.chdir(destination)

        # yield pauses execution here and
        # hands control back to the 'with' block
        yield

    finally:
        # This ALWAYS executes:
        # - even if an exception occurs
        # - ensures we return to original directory
        os.chdir(cwd)


print("-" * 32, "with context manager...")

# Using the context manager
# Directory changes are temporary and safe
with change_dir("day1"):
    # We are inside "day1" directory here
    print(os.listdir())

# Automatically back to original directory here

with change_dir("day2"):
    # We are inside "day2" directory here
    print(os.listdir())

# Automatically back to original directory again


# -------------------------------------------------------
# KEY TAKEAWAYS (VERY IMPORTANT FOR REVISION)
# -------------------------------------------------------

# 1. contextmanager decorator converts a generator into a context manager
# 2. yield marks the point where control enters the 'with' block
# 3. Code BEFORE yield  -> setup logic
# 4. Code AFTER yield   -> cleanup logic
# 5. finally ensures cleanup ALWAYS happens
# 6. This pattern is commonly used for:
#    - File handling
#    - Directory switching
#    - Database connections
#    - Locks and resource management
