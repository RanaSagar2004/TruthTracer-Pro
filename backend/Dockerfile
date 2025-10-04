# backend/Dockerfile  (use when docker-compose.yml has `build: ./backend`)
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# copy requirements from build context (./backend/requirements.txt)
COPY requirements.txt /app/requirements.txt

# install python deps
RUN pip install --no-cache-dir -r /app/requirements.txt

# copy rest of app from build context (./backend/* -> /app/*)
COPY . /app

# ensure HF cache dir exists (matches your docker volume)
RUN mkdir -p /root/.cache/huggingface

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
