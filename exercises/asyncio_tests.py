import asyncio


async def execute_task(param: int):
    """
    @:param simple integer used as index in the print
    """
    await asyncio.sleep(1)
    print(f"Task {param} done")


async def main():
    """
    Executes 10 tasks in background, storing the task object into a set and deletes them once the task X completed its execution.
    """
    background_task = set()
    for i in range(10):
        task = asyncio.create_task(execute_task(param=i))
        background_task.add(task)
        task.add_done_callback(background_task.discard)
    await asyncio.sleep(2)


if __name__ == "__main__":
    asyncio.run(main())
