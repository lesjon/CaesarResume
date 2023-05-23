# Use python:3.11-alpine as the base image
FROM python:3.11-alpine

# Set the working directory in the Docker image
WORKDIR /app

# Copy the requirements file into the Docker image
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the Docker image
COPY . .

# Define the command that will be executed when the Docker container is run
CMD ["python", "main.py"]
