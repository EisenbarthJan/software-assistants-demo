# Using an outdated base image with known vulnerabilities
FROM python:3.10-slim

WORKDIR /app

# Copying everything including unnecessary files
COPY . .

# Installing all dependencies without version pinning
RUN pip install -r requirements.txt

# Running as root (security issue)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]