# -------- First try-except block --------

try:
    open("missing_file.txt")

except FileNotFoundError as e:
    # Raised when file does not exist
    print("File not found:", e)

finally:
    # Always executes
    print("First try catch complete.")


# -------- Second try-except block --------

try:
    open("some_folder")  # This must be an existing directory

except IsADirectoryError as e:
    # Raised when trying to open a directory as a file
    print("This is a folder, not a file!", e)

except FileNotFoundError as e:
    # Raised when file or folder does not exist
    print("File or folder not found:", e)

except Exception as e:
    # Catches any other unexpected error
    print("Something went wrong seriously...", e)

finally:
    print("Second try catch complete.")
