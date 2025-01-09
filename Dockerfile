FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED 1
ARG REQUIREMENT_FILE=requirements.txt

# Install any dependencies required for your environment
RUN apt update

# Create the app directory and set the working directory
RUN mkdir /code
WORKDIR /code

# Copy the requirements file into the container and install dependencies
COPY requirements.txt /code/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt

# Copy the rest of the project files into the container
COPY . /code/

# Default command for Django (adjust if you have a different entry point)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
