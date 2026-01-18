# BtC Python Workshop!

Welcome to the Northeaster Bridge to Calculus Python Workshop!


# Python Workshop Setup Guide

This project uses **Python virtual environments (`venv`)** to keep dependencies isolated and easy to manage.
Follow the steps below to get set up before (or during) the workshop.

---

## Prerequisites

- **Python 3.9 or newer**

Check your Python version:

```bash
python3 --version
````

If Python is not installed, download it from:
[https://www.python.org/downloads/](https://www.python.org/downloads/)

---

## Step 1: Create a Virtual Environment

From the project root directory, run:

```bash
python3 -m venv venv
```
This creates a folder called `venv/` that contains your isolated Python environment.

---

## Step 2: Activate the Virtual Environment

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows (PowerShell)

```powershell
venv\Scripts\Activate.ps1
```

You should see `(venv)` at the beginning of your terminal prompt.

---

## Step 3: Upgrade pip (Recommended)

```bash
pip install --upgrade pip
```

---

## Step 4: Install Project Dependencies

Install all required packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```
---

## Step 5: Running a Stremalit App
Example (Streamlit app):

```bash
streamlit run day1/streamlit_app/app.py
```
