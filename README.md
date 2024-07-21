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

### 3. Installing dependancies and running the app

With the virtual environment activated, use docker to install the required dependencies using pip and build the app containers.

Note that both development and staging environment starts databases within the container network and production uses seperately hosted DBs

development environment:

```bash
docker-compose --env-file .env.development -f docker-compose.yml up --build -d
```

staging/test environment:

```bash
docker-compose --env-file .env.staging -f docker-compose.staging.yml up --build -d
```

production environment:

```bash
docker-compose --env-file .env.production -f docker-compose.production.yml up --build -d
```

## Additional Notes

Make sure to deactivate the virtual environment when you're done working on the project. You can do this whilst in a virtual environment by running:

```bash
deactivate
```
