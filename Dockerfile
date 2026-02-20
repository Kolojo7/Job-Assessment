# Start your image with a node base imageF
FROM python:3.10-slim

# The /app directory should act as the main application directory
WORKDIR /app

# Prevent Python from writing .pyc files 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
COPY backend/requirements.txt backend/requirements.txt
RUN pip install --no-cache-dir -r backend/requirements.txt

COPY backend backend
COPY frontend frontend

EXPOSE 5000

# Start the app using python command
CMD ["python", "backend/app.py"]
