# Use python:alpine
FROM python:alpine

# Set working directory for API
WORKDIR /usr/src/api

# Install requests and docopt python modules
RUN pip install --no-cache-dir requests docopt

# Copy API source to working directory
COPY ./api .

# Set entry to run api code
ENTRYPOINT [ "python", "./weather.py" ]
