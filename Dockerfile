# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy everything first
COPY . .

# Then install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]