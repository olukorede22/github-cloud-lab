FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src ./src
COPY hello.py .

CMD ["python", "hello.py"]
