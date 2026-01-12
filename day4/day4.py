# day-4 task 1
import module
from math import sqrt
import time 

module.say_hello("nirzar")
module.say_bye("nirzar")
print(sqrt(36))

print(module.square(2))

# day-4 task 2 
def logtime(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        return time.time()- start,result 
    return wrapper
 
@logtime
def complex_function():
    time.sleep(3)
    return "Done"

print(complex_function())



