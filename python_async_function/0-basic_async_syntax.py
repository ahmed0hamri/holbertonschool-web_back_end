#!/usr/bin/env python3
import asyncio
import random

# Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds
async def wait_random(max_delay: int = 10) -> float:
    # Generate a random float between 0 and max_delay (inclusive)
    delay = random.uniform(0, max_delay)
    
    # Asynchronously sleep for the duration of 'delay'
    await asyncio.sleep(delay)
    
    # Return the actual delay that was waited
    return delay