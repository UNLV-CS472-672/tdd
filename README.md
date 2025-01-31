# 🧪 Test-Driven Development (TDD) Lab

## 📌 Overview
This lab focuses on **Test-Driven Development (TDD)**—writing test cases first and then implementing the required functionality. Each student will contribute **one test case** and submit a pull request.

📖 **Instructions**: Follow the guidelines provided on the [class website](https://johnxu21.github.io/teaching/CS472/Timetable/dynamic_analysis/?).

---

## 📂 Project Structure

The repository is organized as follows:

```markdown
tdd_lab/
├── 📂 tests/                   # Contains all test cases
│   ├── 📄 test_counter.py       # Test cases for the counter API (each student contributes a test)
├── 📂 src/                      # Source code for the counter service
│   ├── 📄 __init__.py           # Flask app initialization
│   ├── 📄 counter.py            # Counter API implementation
│   ├── 📄 status.py             # HTTP status codes
├── 📄 requirements.txt          # Dependencies for the project
├── 📄 pytest.ini                # Pytest configuration
├── 📄 README.md                 # Project documentation
```

### Python Version (s)
To be able to following the lab, you need at least python `>= 3.8`. The exercise has been testing with the following Python versions: `3.8.1`, `3.9.5`, `3.9.6`, `3.9.7` and `3.10.10` but any version of python `3.8+` work without any configuration issues. **If you are facing any configuration issues, please reach out to the T.A**. 

### 1. Upgrading PIP:
Sometimes it is useful to upgrade `pip` before installing dependencies. If you like, run: `pip install --upgrade pip` and later install the dependencies using: `pip install -r requirements.txt`

### 2. Create a Virtual Environment (Highly Recommended)
 - It is a good practice to configure python virtual environment. Use the commands below to setup python virtual environment on `Linux/MacOS` or `Windows OS`
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```
 ### 3. Install Dependencies  
```bash
pip install -r requirements.txt
```

### 4. Set Flask Environment Variable
```bash
   python3 -m venv venv
  source venv/bin/activate  # macOS/Linux
  venv\Scripts\activate     # Windows
```
### 5. Run Flask Locally to Ensure API Works
```bash
flask run
```

✅ Visit http://127.0.0.1:5000/counters/foo in the browser. If it returns {"error": "Counter not found"}, your API is working!


### 6. 🛠️ Troubleshooting Guide

Below are common errors students may encounter and their solutions:

| **Error** | **Cause** | **Solution** |
|-----------|----------|-------------|
| `ImportError: cannot import name 'app' from 'src'` | Flask app is not detected | Run `export FLASK_APP=src` before running `flask run` |
| `Error: No such command 'db'` | Flask-Migrate missing | Run `pip install flask-migrate` |
| `sqlalchemy.exc.OperationalError: table account has no column named balance` | Database not migrated | Run `flask db upgrade` |
| `ModuleNotFoundError: No module named 'src'` | Missing dependencies | Run `pip install -r requirements.txt` |

If you continue to experience issues, follow these steps:
1. **Check that Flask is running** with `flask run`.
2. **Ensure all dependencies are installed** with `pip install -r requirements.txt`.
3. **Consult your team first before reaching out for help**.
4. **If the issue persists, open a GitHub Issue in your team repository**, including:
   - A clear description of the problem.
   - The exact error message.
   - Steps you have already tried.

🚀 **Debug first, then ask for help!**


