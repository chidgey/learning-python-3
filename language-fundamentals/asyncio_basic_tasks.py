#!/usr/bin/env python3

"""When a coroutine is wrapped into a Task with functions like asyncio.create_task()
the coroutine is automatically scheduled to run soon not immediately.

    https://docs.python.org/3/library/asyncio-task.html
"""

import asyncio


async def task_func():
    return 'hello moon'


async def main():
    print('creating task')

    # Wraps the coroutine into a task and schedules it's execution to run as soon as possible.
    task = asyncio.create_task(task_func())

    print('waiting for {!r}'.format(task))

    # "task" can now be used to cancel "task_func()", or
    # can simply be awaited to wait until it is complete:
    return_value = await task
    print('task completed {!r}'.format(task))
    print('return value: {!r}'.format(return_value))


# main execution, Python 3.7+
asyncio.run(main())
