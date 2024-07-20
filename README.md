# Python Auth Service

This repository contains my first attempt at a Python application that uses Flask, PostgreSQL, and JWT for authentication.

## Setup Instructions

Follow these steps to set up and run the application:

### 1. Create a Virtual Environment

First, create a virtual environment to manage dependencies. This keeps the project dependencies isolated from your system Python installation.

```bash
python3 -m venv venv
```

### 2. Activate the Virtual Environemnt

Next, activate the virtual environment. This step will differ based on your operating system.

On macOS:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

With the virtual environment activated, install the required dependencies using pip.

```bash
pip install flask psycopg2-binary pyjwt python-dotenv
```

### 4. Run the Application

Finally, run the application using Python.

```bash
python3 wsgi.py
```

## Additional Notes

Make sure to deactivate the virtual environment when you're done working on the project. You can do this whilst in a virtual environment by running:

```bash
deactivate
```
