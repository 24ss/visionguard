FROM python:3.10-slim

WORKDIR /app
COPY backend/ .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
