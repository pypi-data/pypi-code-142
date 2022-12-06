from __future__ import annotations

import asyncio
import os
import time
from contextlib import asynccontextmanager, suppress
from typing import TYPE_CHECKING

from redis import asyncio as redis
from redis.asyncio.lock import Lock
from redis.exceptions import LockError

if TYPE_CHECKING:
    from typing import AsyncIterator

# Number of seconds where a lock without a heartbeat is considered stale.
INITIAL_LOCK_HOLD_SECONDS = 15

# Maximum number of seconds a lock can be held.
MAX_LOCK_HOLD_SECONDS = 60

# Maximum time to sleep for a lock. If there are 2 concurrent
# operations where each one takes 30 seconds, 30 + 1 should be
# enough for the ask. But what if there are 20 concurrent operations
# where ours is the last one? Then we have to wait for 20 * 30 seconds
# and then expect to get the lock (which is not guaranteed, due to some
# other process taking the lock before us). This is a problem that will
# be solved when we have a priority queue based system.
#
# Current approach is simply waiting indefinitely, which might lead obscure
# problems (nothing we can do until the priority queue is implemented).
MAX_LOCK_ASK_SECONDS = None


async def send_heartbeat(
    lock: Lock,
    refresh_for: float,
    refresh_delay: float,
) -> None:
    loop = asyncio.get_event_loop()

    # When the lock is released, the task will be cancelled
    # immediately. We don't want to keep refreshing the lock
    # in that case.
    with suppress(asyncio.CancelledError):
        while refresh_for >= 0:
            refresh_for -= refresh_delay

            # We might have released the lock by now, so ensure
            # heartbeat won't fail (the task will also be cancelled
            # soon).
            request_time = loop.time()
            with suppress(LockError):
                await lock.extend(additional_time=refresh_delay)

            # Consider the time spent in the lock.extend() call.
            refresh_for += loop.time() - request_time
            await asyncio.sleep(refresh_delay)


@asynccontextmanager
async def resource_lock(
    client: redis.Redis,
    resource_type: str,
) -> AsyncIterator[None]:
    from isolate_controller.scheduler import SchedulerError

    lock = client.lock(
        f"resource-lock:{resource_type}",
        timeout=INITIAL_LOCK_HOLD_SECONDS,
        blocking_timeout=MAX_LOCK_ASK_SECONDS,
    )

    lock_ask_time = time.perf_counter()
    try:
        async with lock:
            lock_acq_time = time.perf_counter()
            print(f"Acquired lock in: {lock_acq_time - lock_ask_time:.2f}s")
            refresh_for = MAX_LOCK_HOLD_SECONDS - INITIAL_LOCK_HOLD_SECONDS
            heartbeat_task = asyncio.create_task(
                send_heartbeat(
                    lock,
                    refresh_for=refresh_for,
                    refresh_delay=1,
                )
            )
            yield

        heartbeat_task.cancel()
        await heartbeat_task
        print(f"Released lock in: {time.perf_counter() - lock_acq_time:.2f}s")
    except LockError:
        raise SchedulerError(f"Failed to acquire the lock for {resource_type}!")


def get_redis_client() -> redis.Redis:
    redis_host = os.environ.get("REDISHOST", "localhost")
    redis_port = int(os.environ.get("REDISPORT", 6379))
    return redis.Redis(host=redis_host, port=redis_port)
