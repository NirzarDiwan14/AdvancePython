# MULTITHEREADING method-2 = older but different method with loops
import concurrent.futures
import time

def cpu_bound_task(seconds):
    print(f"Sleeping for {seconds} seconds...")
    time.sleep(seconds)
    return f"Done sleeping {seconds} seconds..."


start = time.perf_counter()

with concurrent.futures.ProcessPoolExecutor() as executer:
    seconds = [5,3,4,1,2]

    # it will give the output in order of completion of execution
    # results = [executer.submit(cpu_bound_task,sec) for sec in seconds]

    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())


    # it will give the output in order of given list
    # results = executer.map(cpu_bound_task,seconds)
    # for result in results:
    #     print(result)
    
end = time.perf_counter()
print(f"Program Executed in {round(end - start, 2)} seconds.")