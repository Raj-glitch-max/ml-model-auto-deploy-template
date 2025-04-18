FROM python:3.9-slim

WORKDIR /app

COPY train.py .
COPY dataset.csv .

RUN pip install pandas scikit-learn joblib

CMD ["python", "train.py"]
