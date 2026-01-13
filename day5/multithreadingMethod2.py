# MULTITHEREADING method-2 = older but different method with loops
import threading 
import time 

start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping for {seconds} seconds...")
    time.sleep(seconds)
    print("Done sleeping...")


threads = []
for _ in range(10):
    t = threading.Thread(target=do_something,args=[1.5])
    t.start()
    threads.append(t)

for _ in range(10):
    t.join()

end = time.perf_counter()

print(f"Program executed in {end - start} time.")
