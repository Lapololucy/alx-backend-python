#!/usr/bin/env python3


import asyncio
from random import uniform


''' Write an asynchronous coroutine that takes in an integer
    argument (max_delay, with a default value of 10) named
    wait_random that waits for a random delay between 0 and
    max_delay (included and float value) seconds and eventually returns it.
'''


async def wait_random(max_delay: int = 10) -> float:
    '''Generates a random number and returns it after n delay'''
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


if __name__ == '__main__':
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
