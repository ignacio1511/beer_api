# Use the official Python image as the base image
FROM --platform=linux/amd64 python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy the Django project into the container
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Run the Django application using Gunicorn
CMD ["gunicorn", "beer_api.wsgi:application", "--bind", "0.0.0.0:8000"]
