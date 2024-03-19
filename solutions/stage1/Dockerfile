from python:3.10.13-alpine3.19
workdir /app

copy sources sources

run pip install -r sources/requirements.txt
RUN pip install --no-cache-dir -r sources/requirements.txt

run adduser -S appuser
user appuser

expose 7860

cmd ["python", "sources/main.py"]
