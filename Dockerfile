# Use the Python 3.9 slim image as the base
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED True

# Set the working directory in the container
ENV APP_HOME /app
WORKDIR $APP_HOME

# Copy the local code to the container
COPY . ./

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Specify the command to run on container start
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 30 main:app
