from alpine:3.10
workdir /app

copy requirements.txt requirements.txt

run pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

run adduser -S appuser
user appuser

expose 7860

cmd["python3", "main.py"]
