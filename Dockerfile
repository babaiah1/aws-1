# builder stage
FROM python:3.11-slim AS builder
WORKDIR /app
RUN apt-get update && apt-get install -y build-essential gcc --no-install-recommends && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN python -m pip install --upgrade pip wheel
RUN pip wheel --wheel-dir /wheels -r requirements.txt

# final stage - minimal runtime
FROM python:3.11-slim
RUN useradd -m appuser
WORKDIR /app
COPY --from=builder /wheels /wheels
COPY requirements.txt .
RUN pip install --no-index --find-links=/wheels -r requirements.txt
COPY . /app
ENV PYTHONUNBUFFERED=1
USER appuser
EXPOSE 8080
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
