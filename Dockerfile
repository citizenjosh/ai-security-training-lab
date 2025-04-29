# Dockerfile for AI Security Training Lab
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy lab files into container
COPY owasp/ ./owasp/

# Default command
CMD ["bash"]
