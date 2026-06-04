# AllAtomic - Dockerfile
Dev: @GhostMarshal | Channel: @ComputeCode
(૨๑•̀ㅁ•́ฅा) Purple Anime Theme (#9A8CFF)

FROM python:3.11-slim

LABEL maintainer="GhostMarshal"
LABEL description="AllAtomic Telegram Userbot"
LABEL version="2.0.0"

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Create data directory
RUN mkdir -p /app/data /app/logs

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Expose port (if needed)
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import AllAtomic; print('OK')"

# Run the application
CMD ["python", "-m", "AllAtomic"]
