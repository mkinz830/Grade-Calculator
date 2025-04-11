# 🧮 Grade Calculator

## 🧠 Project Overview
This is a simple Python function that calculates a letter grade based on a numeric score input. It's designed to demonstrate basic use of functions, conditional logic, and input validation.

## 💡 How It Works
The `computegrade()` function takes a score between 0.0 and 1.0 and returns a letter grade (A–F) based on standard grading criteria.

## 🔤 Grading Scale
- 0.9 and above → A  
- 0.8 to < 0.9 → B  
- 0.7 to < 0.8 → C  
- 0.6 to < 0.7 → D  
- Below 0.6 → F  

If the score is out of range or not a number, it returns `"Error"`.

## 🛠 Technologies Used
- Python

## 🚀 How to Run
1. Clone or download the repository.
2. Open the Python file in your editor or run it in a Python environment.
3. Call `computegrade(score)` where `score` is a float between 0.0 and 1.0.

Example:
```python
computegrade(0.85)  # Output: B
