#!/usr/bin/env python3

# pylint: disable=missing-docstring

"""A great example of how to spin up multiple threads that service a queue of jobs
to be done.

It always makes sense to scope all code into function defintions to stop trashing
global space. You'll also reduce linting errors."""

import threading
from queue import Queue
import time


def run_demo():
    # lock to serialize console output, when sharing resources, data etc... threads need to take
    # their turn by using locks. Note that locks can cause dead-lock scenarios and are best avoided
    # by allowing threads to run entirely on their own, then joining everything back at the end.
    console_resource_lock = threading.Lock()

    def do_work(item):
        time.sleep(.1)  # pretend to do some lengthy work.
        # Make sure the whole print completes or threads can mix up output in one line.
        with console_resource_lock:
            print(threading.current_thread().name, item)

    # The worker thread pulls an item from the queue and processes it
    def worker():
        while True:
            item = my_queue.get()
            do_work(item)
            my_queue.task_done()

    # Create the queue and thread pool of 4 threads
    my_queue = Queue()
    for _ in range(4):
        my_thread = threading.Thread(target=worker)
        # thread dies when main thread (only non-daemon thread) exits.
        my_thread.daemon = True
        my_thread.start()

    # stuff 20 work items on the queue (in this case, just a number).
    start = time.perf_counter()
    for i in range(20):
        my_queue.put(i)

    my_queue.join()  # block until all tasks are done

    # "Work" took .1 seconds per task.
    # 20 tasks serially would be 2 seconds.
    # With 4 threads should be about .5 seconds (contrived because non-CPU intensive "work")
    print('time:', time.perf_counter() - start)

    # use semaphores when only x number of threads can access a resource at a time. This results in
    # better stability, but really it's a throttle to prevent contention.


run_demo()
