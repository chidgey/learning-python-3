#!/usr/bin/env python3

"""Multiprocessing spins up a new process to execute the code.

    Wrapping the main part of the application in a check for 
    __main__ ensures that it is not run recursively in each child as the module is imported.
    It's possible to split these into seperate modules to avoid this.

    Make sure you read the Programming Guidelines at: 
    https://docs.python.org/3.7/library/multiprocessing.html
    
    https://pymotw.com/3/multiprocessing/basics.html

"""

import multiprocessing
import time


def worker(num):
    """thread worker function"""
    name = multiprocessing.current_process().name
    print(name, 'Starting')
    time.sleep(0.5)
    print(name, 'Exiting')


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(
            name='worker ' + str(i),
            target=worker,
            args=(i,)
        )
        jobs.append(p)
        p.start()

    for j in jobs:
        # wait for the process to finish the job
        j.join() 
        # it's possible to add a timeout here for join(timeout), to give the process
        # a chance to complete before continuing anyway.
        print('{:>15}.exitcode = {}'.format(j.name, j.exitcode))