FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

# Install build dependencies: compiler, PostgreSQL headers, Python headers
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade build tools
RUN pip install --upgrade pip setuptools wheel

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src

EXPOSE 5000

CMD ["python", "src/app.py"]   