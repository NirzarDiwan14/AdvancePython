import sqlite3
from employee import Employee   # Import Employee class (custom module)

# -------------------------------------------------
# DATABASE CONNECTION
# -------------------------------------------------

# Connect to SQLite database (creates file if it does not exist)
conn = sqlite3.connect("employee.db")

# Cursor object is used to execute SQL commands
c = conn.cursor()

# -------------------------------------------------
# TABLE CREATION (RUN ONLY ONCE)
# -------------------------------------------------
# This creates the employees table
# Uncomment and run only the first time

# c.execute("""
#     CREATE TABLE employees (
#         first TEXT,
#         last TEXT,
#         pay INTEGER
#     )
# """)

# -------------------------------------------------
# FUNCTION: SHOW ALL EMPLOYEES
# -------------------------------------------------
def show_all():
    """
    Fetch and return all records from the employees table
    """
    with conn:   # Automatically commits or rolls back
        c.execute("SELECT * FROM employees")
    return c.fetchall()


# -------------------------------------------------
# FUNCTION: INSERT EMPLOYEE
# -------------------------------------------------
def insert_emp(emp):
    """
    Insert an Employee object into the database
    """
    with conn:
        c.execute(
            "INSERT INTO employees VALUES (:first, :last, :pay)",
            {
                "first": emp.first,
                "last": emp.last,
                "pay": emp.pay
            }
        )


# -------------------------------------------------
# FUNCTION: GET EMPLOYEE BY LAST NAME
# -------------------------------------------------
def get_emp_by_name(lastname):
    """
    Fetch employees based on last name
    """
    c.execute(
        "SELECT * FROM employees WHERE last = :last",
        {"last": lastname}
    )
    return c.fetchall()


# -------------------------------------------------
# FUNCTION: UPDATE EMPLOYEE PAY
# -------------------------------------------------
def update_pay(emp, pay):
    """
    Update salary of an employee using first and last name
    """
    with conn:
        c.execute(
            """
            UPDATE employees SET pay = :pay
            WHERE first = :first AND last = :last
            """,
            {
                "first": emp.first,
                "last": emp.last,
                "pay": pay
            }
        )


# -------------------------------------------------
# FUNCTION: REMOVE EMPLOYEE
# -------------------------------------------------
def remove_emp(emp):
    """
    Remove an employee from the database
    """
    with conn:
        c.execute(
            "DELETE FROM employees WHERE first = :first AND last = :last",
            {
                "first": emp.first,
                "last": emp.last
            }
        )


# -------------------------------------------------
# CREATING EMPLOYEE OBJECTS
# -------------------------------------------------
emp_1 = Employee("Nirzar", "Diwan", 8000)
emp_2 = Employee("Shailesh", "Diwan", 10000)
emp_3 = Employee("Ansh", "Chaudhari", 8500)

# -------------------------------------------------
# INSERT EMPLOYEES (RUN ONCE)
# -------------------------------------------------
# insert_emp(emp_1)
# insert_emp(emp_2)
# insert_emp(emp_3)

# -------------------------------------------------
# DISPLAY ALL EMPLOYEES
# -------------------------------------------------
print("All Employees:")
print(show_all())

# -------------------------------------------------
# FETCH EMPLOYEES BY LAST NAME
# -------------------------------------------------
emps = get_emp_by_name("Diwan")
print("Employees with last name 'Diwan':")
print(emps)

# -------------------------------------------------
# UPDATE PAY FOR AN EMPLOYEE
# -------------------------------------------------
update_pay(emp_1, 40000)

# Fetch again to see updated result
emps = get_emp_by_name("Diwan")
print("After salary update:")
print(emps)

# -------------------------------------------------
# REMOVE AN EMPLOYEE
# -------------------------------------------------
remove_emp(emp_2)

# Fetch again after deletion
emps = get_emp_by_name("Diwan")
print("After removing an employee:")
print(emps)

# -------------------------------------------------
# CLOSE DATABASE CONNECTION
# -------------------------------------------------
conn.close()
