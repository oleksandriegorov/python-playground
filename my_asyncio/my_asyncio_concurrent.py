import asyncio
import time
import random
from tabulate import tabulate


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
    return what


async def make_ssh_connection(destination_server: str) -> str:
    conn_time = random.randrange(0, 3)
    conn_outcomes = ["\033[0;32mOK\033[0m", "\033[0;31mERROR\033[0m"]
    await asyncio.sleep(conn_time)
    msg = f"connected to {destination_server} in {conn_time}"
    conn_result: str = random.choice(conn_outcomes)
    conn_details = "Connection refused by remote host" if "ERROR" in conn_result else "OK"
    print(msg)
    return (destination_server, conn_result, conn_details)


async def main():
    # task1 = asyncio.create_task(say_after(3, "hello"))

    # task2 = asyncio.create_task(say_after(2, "world"))

    print(f"started at {time.strftime('%X')}")

    # # Wait until both tasks are completed (should take
    # # around 2 seconds.)
    # await task1
    # await task2

    servers = ["192.168.1.1", "192.168.1.2", "192.168.200.40"]
    my_tasks = [make_ssh_connection(destination_server=i) for i in servers]
    headers = ("server", "connection results", "connection details")
    results = await asyncio.gather(*my_tasks)
    print(
        tabulate(
            results,
            headers=headers,
            tablefmt="fancy_grid",
            colalign=("center",) * len(headers),
            maxheadercolwidths=[10] * len(headers),
            showindex="always",
        )
    )

    # Simultaneous running and getting a result
    # results = await asyncio.gather(say_after(3, "Hello"), say_after(2, "World"))
    # print(results)

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
