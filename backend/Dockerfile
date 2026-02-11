# Dockerfile for Django application

# Use the official Python image from the Docker Hub
FROM python:3.9-slim AS base

# Set the working directory in the Docker container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django application code
COPY . .

# Collect static files (if any)
RUN python manage.py collectstatic --noinput

# Specify the command to run the application
CMD ["gunicorn", "project_jambo.wsgi:application", "--bind", "0.0.0.0:8000"]
