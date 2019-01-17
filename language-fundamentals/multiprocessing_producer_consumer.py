#!/usr/bin/env python3

"""Multiple processes can work on a job and co-ordinate using message queues.

    When using multiple processes, one generally uses message passing for communication 
    between processes and avoids having to use any synchronization primitives like locks.

    For passing messages one can use Pipe() (for a connection between two processes) or a 
    queue (which allows multiple producers and consumers) as this example illustrates.
"""

import multiprocessing
import time

# each consumer is a process, we saw this in multiprocessing-subclassing
class Consumer(multiprocessing.Process):

    '''Consumers pull from one queue, process and then place the result into another queue'''
    def __init__(self, task_queue, result_queue):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        proc_name = self.name
        while True:
        
            next_task = self.task_queue.get()
            
            # only executes this block after all messages are done, as these
            # poison pills were added at the end of the queue in setup.
            if next_task is None:
                # Poison pill means shutdown
                print('{}: Exiting'.format(proc_name))
                self.task_queue.task_done()
                break
            
            print('{}: {}'.format(proc_name, next_task))
            answer = next_task()

            # you must call JoinableQueue.task_done() for each task removed from the queue or 
            # else the semaphore used to count the number of unfinished tasks may eventually overflow
            self.task_queue.task_done()
            self.result_queue.put(answer)


class Task:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Implementing the __call__ magic method in a class causes its instances to 
    # become callables -- in other words, those instances now behave like functions
    def __call__(self):
        time.sleep(0.1)  # pretend to take time to do the work
        return '{self.a} * {self.b} = {product}'.format(
            self=self, product=self.a * self.b)

    def __str__(self):
        return '{self.a} * {self.b}'.format(self=self)


# Main module processing starts here...
if __name__ == '__main__':
    # Establish communication queues
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()

    # Start consumers
    num_consumers = multiprocessing.cpu_count() * 2
    print('Creating {} consumers'.format(num_consumers))
    consumers = [
        Consumer(tasks, results)
        for i in range(num_consumers)
    ]
    for w in consumers:
        w.start()

    # Enqueue jobs
    num_jobs = 10
    for i in range(num_jobs):
        tasks.put(Task(i, i))

    # Add a poison pill for each consumer
    for i in range(num_consumers):
        tasks.put(None)

    # Wait for all of the tasks to finish
    tasks.join()

    # Start printing results
    while num_jobs:
        result = results.get()
        print('Result:', result)
        num_jobs -= 1
