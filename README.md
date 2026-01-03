# AI Automation System

> A Flask-based automation system for executing predefined Python file automation tasks through a web interface.

---

## 🚀 Overview
This project provides a simple backend-driven approach to automate common file management tasks such as organizing files by type and bulk renaming files.

The main focus of this project is **backend architecture**, **Python automation**, and **clean separation of concerns** between:
- automation logic (pure Python)
- control logic (Flask routes)

---

## ✨ Features
- Organize files in a folder by file type (based on extensions)
- Bulk rename files by adding a prefix
- Flask backend to trigger automation tasks
- Simple HTML interface for user input

---

## 🛠 Tech Stack
- Python 3.7+
- Flask
- Standard Python libraries (`os`, `shutil`)

---

## ⚙️ How It Works
1. User opens the web interface.
2. User submits a folder path and selects an automation task.
3. Flask validates the input.
4. The corresponding automation function is executed.
5. A success or error response is returned.

Install dependencies
pip install -r requirements.txt

Run the application
python app.py

