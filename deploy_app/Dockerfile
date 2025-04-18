FROM python:3.9-slim

WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the app and model files
COPY app.py .
COPY model.pkl .

COPY templates/ ./templates/

# Command to run the Flask app
CMD ["python", "app.py"]

