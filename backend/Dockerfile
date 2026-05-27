# Base Python image
FROM python:3.10-slim


# Set working directory inside container
WORKDIR /app


# Copy requirements file
COPY requirements.txt .


# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Copy all backend files into container
COPY . .


# Expose FastAPI port
EXPOSE 8000


# Start FastAPI server
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]