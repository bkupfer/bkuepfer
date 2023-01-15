# Use the official Python image as the base image
FROM python:3.10-slim

RUN echo "Dockerfile - "
# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN echo "Dockerfile - installing requirements"
RUN pip install --no-cache-dir -r requirements.txt
RUN echo "Dockerfile - success installing requirements"


# Copy the rest of the application code into the container
COPY . .

RUN echo "Dockerfile - all done; running CMD"

# Run the server on port 8880
CMD ["python", "manage.py", "runserver", "0.0.0.0:8880"]
