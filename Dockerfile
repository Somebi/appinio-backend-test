# Use an official Python runtime as a parent image, based on Alpine
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /usr/src/app

# Install pipenv and other dependencies
RUN apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev \
    && pip install --no-cache-dir pipenv \
    && apk del .build-deps

COPY Pipfile .
COPY Pipfile.lock .

# Install project dependencies using pipenv
RUN pipenv install --system --deploy

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Make sure your start.sh script is executable
RUN chmod +x start.sh

# Remove .env file is there is any
RUN rm .env

# Use start.sh as the entrypoint
ENTRYPOINT ["./start.sh"]
