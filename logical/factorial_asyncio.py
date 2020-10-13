import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        f *= i
        if i > 3:
            print(f"Task {name}: is sleeping for 1ms")
            await asyncio.sleep(0.001)
    print(f"Task {name}: factorial({number}) = {f}")

async def main():
    # Schedule three calls *concurrently*:
    await asyncio.gather(
        factorial("A", 10),
        factorial("B", 4),
        factorial("C", 8),
    )

asyncio.run(main())