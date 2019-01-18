#!/usr/bin/env python3

"""Asyncio requires the application code to handle context changes based on the idea of an
event loop.

The asyncio module provides tools for building concurrent applications using coroutines. While the
threading module implements concurrency through application threads and multiprocessing implements
concurrency using system processes, asyncio uses a single-threaded, single-process approach in
which parts of an application cooperate to switch tasks explicitly at optimal times.

Applications interact with the event loop to register code to run and let the loop call the code
when resources become available. e.g. registration of a network socket then awaits inbound
connections and calls back to application code when the event is fired.

Application code then yields control when no more work is to be done, in the example it could be
after an ack is sent.

https://docs.python.org/3/library/asyncio-task.html#coroutine
"""

import asyncio


async def outer():
    """here we are chaining coroutines together to make a task easier to
    decompose into reusable parts."""
    print('in outer')
    print('waiting for result1')
    # The await keyword is used instead of adding the new coroutines to the loop,
    # because control flow is already inside of a coroutine being managed by the
    # loop so it isn’t necessary to tell the loop to manage the new coroutines.
    result1 = await phase1()
    print('waiting for result2')
    # There are three main types of awaitable objects: coroutines, Tasks, and Futures.
    result2 = await phase2(result1)
    return (result1, result2)


async def phase1():
    print('in phase1')
    return 'result1'


async def phase2(arg):
    print('in phase2')
    return 'result2 derived from {}'.format(arg)


# main execution, Python 3.7+
return_value = asyncio.run(outer())
print('return value: {!r}'.format(return_value))
