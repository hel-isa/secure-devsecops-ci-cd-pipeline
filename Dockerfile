FROM python:3.12-slim

# Create non-root user
RUN useradd -m -u 10001 appuser

WORKDIR /app
COPY app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY app /app/app

USER 10001
EXPOSE 8080
CMD ["python", "app/app.py"]
