# MULTITHEREADING method-3 = newer method with pools 
import concurrent.futures
import time 

start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping for {seconds} seconds...")
    time.sleep(seconds)
    return f"Done sleeping {seconds} seconds..."


with concurrent.futures.ThreadPoolExecutor() as executer:
    secs = [5,4,2,1,3]
    # it will give the output in order of given list
    # results  = executer.map(do_something,secs)
    # for result in results:
    #     print(result)

    # it will give the output in order of completion of execution
    # results = [executer.submit(do_something,sec) for sec in secs]
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())


end = time.perf_counter()

print(f"Program executed in {end - start} time.")
