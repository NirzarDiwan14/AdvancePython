# DAY-3 TASK-1
class Employee:
    def __init__(self,name):
        self.name = name 
        self.address = None

    def show(self):
        print(self.name)
        if self.address:
            self.address.show()
    class Address:
        def __init__(self,city,state):
            self.city = city 
            self.state = state 

        def show(self):
            print(self.city, self.state)
    
e1 = Employee("Nirzar")
e1.address = Employee.Address("Ahmedabad","Gujarat")
e1.show()


# DAY-3 TASK-2
class Calculator:
    a = 0
    b= 0 
    @classmethod
    def set_values(cls,x,y):
        cls.a = x
        cls.b = y
        print(f"a = {cls.a} b = {cls.b}")
    
    @classmethod
    def add(cls):
        return cls.a + cls.b 
    @classmethod
    def sub(cls):
        return cls.a - cls.b 
    @classmethod

    def mul(cls):
        return cls.a * cls.b 
    @classmethod
    def divide(cls):
        return cls.a / cls.b 
    
Calculator.set_values(14,7)
print(Calculator.add())
print(Calculator.sub())
print(Calculator.mul())
print(Calculator.divide())

        

            