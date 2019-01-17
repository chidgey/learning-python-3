#!/usr/bin/env python3

"""Use of a class to hold the method for running the process.

    This could result in cleaner code, by bundling the processing runner inside a class.


    https://pymotw.com/3/multiprocessing/basics.html

"""

import multiprocessing


class Worker(multiprocessing.Process):

    def run(self):
        print('In {}'.format(self.name))
        return


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = Worker()
        jobs.append(p)
        p.start()
    for j in jobs:
        j.join()
