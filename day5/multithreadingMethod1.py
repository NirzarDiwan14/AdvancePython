# MULTITHEREADING method-1 = older and simple method
from threading import *
import time

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            time.sleep(1)
class Hie(Thread):
    def run(self):
        for i in range(5):
            print("Hie")
            time.sleep(1)


t1 = Hello()
t2 = Hie()

t1.start()
time.sleep(0.1)
t2.start()

t1.join()
t2.join()

print("End of all threads")



