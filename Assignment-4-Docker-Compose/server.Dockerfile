# Flask Dockerfile
FROM python:3.9

WORKDIR /app
COPY . /app
RUN pip install -r server-requirements.txt

CMD ["python", "serve.py"]
