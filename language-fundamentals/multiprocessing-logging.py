#!/usr/bin/env python3

"""Use logging to capture work occurring across processes"""

import multiprocessing
import logging
import sys


def worker():
    print('Doing some work')
    sys.stdout.flush()


if __name__ == '__main__':
    #multiprocessing.log_to_stderr(logging.DEBUG)
    # or to manipulate the logger
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()