# MULTIPROCCESSING method-1 = older and simple method
import multiprocessing
import time

def cpu_bound_task(seconds):
    print(f"Sleeping for {seconds} seconds...")
    time.sleep(seconds)
    return f"Done sleeping {seconds} seconds..."


start = time.perf_counter()
processes = []

for _ in range(10):
    p = multiprocessing.Process(target=cpu_bound_task, args=[1.5])
    p.start()
    processes.append(p)

for process in processes:
        process.join()
end = time.perf_counter()
print(f"Program Executed in {round(end - start, 2)} seconds.")