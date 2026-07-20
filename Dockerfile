FROM python:3.12-slim

WORKDIR /app

# Copy dependencies first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

EXPOSE 8000

CMD ["uvicorn","section4_deployment.api:app","--host","0.0.0.0","--port","8000"]