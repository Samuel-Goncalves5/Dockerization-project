FROM python:3.10.13

WORKDIR /app

COPY sources sources

RUN pip install --no-cache-dir -r sources/requirements.txt && pip3 install torch --index-url https://download.pytorch.org/whl/cpu

EXPOSE 7860

CMD ["python", "sources/main.py"]
