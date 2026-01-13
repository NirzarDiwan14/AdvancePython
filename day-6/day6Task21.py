#  Basic Logging in python  
import logging

logging.basicConfig(filename = "employee.log",
                    level=logging.INFO,
                    format = " %(levelname)s :%(asctime)s: %(message)s"
                    )
class Employee: 
    def __init__(self,first,last):
        self.first = first 
        self.last = last
        logging.error(f"Created employee: {self.fullname} {self.email}")
        
    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"
    
    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    

e1 = Employee("Nirzar","Diwan")
e2 = Employee("Ansh","chaudhari")
e3 = Employee("khushi","Nandaniya")
e4 = Employee("kishan","prajapati")

print("Program Done")       