import asyncio
import random
import aiofiles
from datetime import datetime

# Асинхронная задача: ждет случайное время и возвращает сообщение

async def run_task(n):
    delay = random.randint(1, 3)
    await asyncio.sleep(delay)
    return f"Task {n} done after {delay} seconds"

# Асинхронный генератор номеров задач

async def task_numbers():
    for i in range(1, 11): # от 1 до 10

        await asyncio.sleep(0.1) # Небольшая задержка для реализации

        yield i

# Асинхронная функция для логирования результатов задачи в файл

async def log_result(message):
    async with aiofiles.open("task_log.txt", mode="a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%H:%M:%S")
        await file.write(f"[{timestamp}] {message}\n")

# Основная корутина, запускающая задачи и логирующая их результаты

async def main():
    tasks = []

    async for number in task_numbers():
        task = asyncio.create_task(run_task(number))
        tasks.append((number, task))

    for number, task in tasks:
        result = await task
        print(result)
        await log_result(result)

# Запуск событийного цикла

if __name__ == "__main__":
    asyncio.run(main())