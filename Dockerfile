FROM python:3.12-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY bot/ ./bot/
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser
CMD ["python", "bot/main.py"]
