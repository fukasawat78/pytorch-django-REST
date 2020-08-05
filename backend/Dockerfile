FROM python:3.7
ENV PYTHONBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN apt-get update && apt-get install -y \
    libblas-dev \
    liblapack-dev \
    libatlas-base-dev \
    libsm6 \
    libxext6 \
    libxrender-dev

ADD requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt