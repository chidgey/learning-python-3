#!/usr/bin/env python3

import threading
from queue import Queue
import time

# lock to serialize console output, when sharing resources, data etc... threads need to take
# their turn by using locks. Note that locks can cause dead-lock scenarios and are best avoided
# by allowing threads to run entirely on their own, then joining everything back at the end.
console_resource_lock = threading.Lock()

def do_work(item):
    time.sleep(.1) # pretend to do some lengthy work.
    # Make sure the whole print completes or threads can mix up output in one line.
    with console_resource_lock:
        print(threading.current_thread().name,item)

# The worker thread pulls an item from the queue and processes it
def worker():
    while True:
        item = q.get()
        do_work(item)
        q.task_done()

# Create the queue and thread pool of 4 threads
q = Queue()
for i in range(4):
     t = threading.Thread(target=worker)
     t.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
     t.start()

# stuff 20 work items on the queue (in this case, just a number).
start = time.perf_counter()
for item in range(20):
    q.put(item)

q.join() # block until all tasks are done

# "Work" took .1 seconds per task.
# 20 tasks serially would be 2 seconds.
# With 4 threads should be about .5 seconds (contrived because non-CPU intensive "work")
print('time:',time.perf_counter() - start)

# use semaphores when only x number of threads can access a resource at a time. This results in
# better stability, but really it's a throttle to prevent contention.