# Factory Scheduling using Linear Programming

This project solves a classic factory job assignment problem using **Linear Programming** with Python’s `PuLP` library.

## 🧩 Problem Statement

Given 5 jobs and 2 machines with varying processing times, assign each job to **exactly one machine** such that the **total processing time is minimized**.

## ✅ Tools Used
- Python
- PuLP (for LP modeling)
- Pandas (for clean output and CSV export)

## ⚙️ How It Works
- Decision Variables: `assign[Job][Machine]` (binary)
- Objective: Minimize total processing time
- Constraint: Each job must be assigned to exactly one machine

## 📊 Output

Example result:

| Job  | Machine   | Processing Time |
|------|-----------|-----------------|
| Job1 | Machine1  | 2               |
| Job2 | Machine2  | 1               |
| Job3 | Machine2  | 2               |
| Job4 | Machine2  | 4               |
| Job5 | Machine1  | 2               |

**Total Time**: 11 units

## 📁 Run It
```bash
pip install -r requirements.txt
python factory_scheduler.py
