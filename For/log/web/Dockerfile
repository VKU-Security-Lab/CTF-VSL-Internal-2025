FROM postgres:9.6-bullseye AS build

# Install the required packages
RUN apt-get update \
    && apt-get install -y postgresql-server-dev-9.6 \
        postgresql-server-dev-all \
        python3 \
        python3-pip \
        python3-setuptools \
        python3-wheel \
        wget \
    && rm -rf /var/lib/apt/lists/*

# Install the required Python packages
RUN pip3 install --no-cache-dir \
        psycopg2 \
        requests

WORKDIR /app

COPY ./app /app
COPY ./requirements.txt /requirements.txt

# Install the required Python packages
RUN pip3 install --no-cache-dir -r /requirements.txt

# Build the application
CMD ["python3", "app.py"]
