# Advanced Logging in Python
import logging

# Create custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create file handler
file_handler = logging.FileHandler("custom-logger.log")
file_handler.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter(
    "%(levelname)s : %(name)s : %(asctime)s : %(message)s"
)

file_handler.setFormatter(formatter)

# Avoid duplicate handlers
if not logger.handlers:
    logger.addHandler(file_handler)

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

        # INFO is appropriate for successful creation
        logger.info(
            f"Created employee: {self.fullname} | {self.email}"
        )

    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

# Creating employees
e1 = Employee("Nirzar", "Diwan")
e2 = Employee("Ansh", "Chaudhari")
e3 = Employee("Khushi", "Nandaniya")
e4 = Employee("Kishan", "Prajapati")

print("Program Done")
