FROM python:3.10.13-alpine3.19

WORKDIR /app

COPY sources sources

RUN pip install --no-cache-dir -r sources/requirements.txt && pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

EXPOSE 7860

CMD ["python", "sources/main.py"]
