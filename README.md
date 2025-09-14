# 📘 Asynchronous Task Logger

## Description  
This project demonstrates how to run multiple asynchronous tasks in Python using `asyncio`, log their results to a file using `aiofiles`, and coordinate task execution with asynchronous generators and context managers.

Each task simulates a delay, completes independently, and writes a timestamped message to a log file.

---

## 🚀 Features
- Runs 10 asynchronous tasks in parallel  
- Each task waits for a random delay (1–3 seconds)  
- Results are printed to the console and logged to `task_log.txt`  
- Uses:
  - `asyncio.create_task()` for parallel execution  
  - Asynchronous generator for task numbering  
  - Asynchronous file writing with `aiofiles`  
  - Timestamps for each log entry

---

## 📦 Requirements
- Python 3.7+
- `aiofiles` library

Install with:

```bash
pip install aiofiles