# Use an official Python runtime as the base image
FROM python:3.11-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Set the environment variable for Flask
ENV FLASK_APP=main.py

EXPOSE 5000
# Set the command to run the app when the container starts
CMD ["flask", "run", "--host=0.0.0.0"]
