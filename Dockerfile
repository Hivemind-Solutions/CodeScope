FROM python:3.9-buster as builder

# Install the last version of Docker
RUN curl -sSL https://get.docker.com/ | sh

WORKDIR /app
COPY requirements.txt requirements.txt

#install pip
RUN pip install --upgrade --no-cache-dir pip && pip install --no-cache-dir -r requirements.txt

#install NPM
RUN pip install --upgrade --no-cache-dir pip && pip install --no-cache-dir -r requirements.txt

#install how2
RUN pip install how2

ENV PYTHONPATH $PYTHONPATH:/app/src
ENV PYTHONUNBUFFERED=1
COPY config.yaml /app
COPY src/* /app/src/

CMD ["python", "src/codescope.py"]
