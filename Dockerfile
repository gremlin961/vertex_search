# Use the official Python image as the base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the application code to the working directory
COPY . .

# Install the necessary dependencies
RUN pip install -r requirements.txt

# Expose the port that the application will listen on
EXPOSE 80

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]