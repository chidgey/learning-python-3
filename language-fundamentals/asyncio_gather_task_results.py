#!/usr/bin/env python3

"""Collecting results that run in parallel.
    If the background phases are well-defined, and only the results of those 
    phases matter, then gather() may be more useful for waiting for multiple operations.

    Note that all this code runs in a single thread as async, however we control when to 
    pause execution in our coroutines and pass control to the next event in the loop.

    https://docs.python.org/3/library/asyncio-task.html#coroutine
"""

import asyncio

async def phase1():
    print('in phase1')
    # async wait the current routine and pass control to asyncio.sleep(2) immediately
    await asyncio.sleep(2)
    print('done with phase1')
    return 'phase1 result'


async def phase2():
    print('in phase2')
    await asyncio.sleep(1)
    print('done with phase2')
    return 'phase2 result'


async def main():
    print('starting main')
    print('waiting for phases to complete')

    # runs coroutines concurrently.
    results = await asyncio.gather(
        phase1(),
        phase2(),
    )
    print('results: {!r}'.format(results))

# main execution, Python 3.7+
asyncio.run(main())