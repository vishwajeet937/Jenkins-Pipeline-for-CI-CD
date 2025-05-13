# 1 Base image
FROM python:3.10-slim

# 2 Set working directory
WORKDIR /app

# 3 Copy dependencies
COPY requirements.txt .

# 4 Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5 Copy app code
COPY . .

# 6 Expose the port (optional but good for documentation)
EXPOSE 5000

# 7 Run the app
CMD ["python", "app.py"]
