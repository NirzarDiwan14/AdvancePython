from threading import Thread, Event
import time 


event = Event()
 
def worker():
    print("Worker waiting for the event...")
    event.wait()
    print("worker received event!")

def trigger():
    time.sleep(2)
    print("Triggering event")
    event.set()

Thread(target=worker).start()
Thread(target=trigger).start()


stopevent = Event()
def background_worker():
    while not stopevent.is_set():
        print("Working...")
        time.sleep(1)
    print("Worker Stopped")

worker_thread = Thread(target=background_worker)
worker_thread.start()

time.sleep(10)
stopevent.set()
worker_thread.join()