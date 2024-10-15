# Streamlit Dockerfile
FROM python:3.9

WORKDIR /app
COPY . /app
RUN pip install -r client-requirements.txt

CMD ["streamlit", "run", "client.py"]
