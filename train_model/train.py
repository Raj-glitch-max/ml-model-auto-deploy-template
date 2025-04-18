import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
import os

# Correct dataset path
dataset_path = os.path.join(os.path.dirname(__file__), '..', 'dataset.csv')

df = pd.read_csv(dataset_path)

X = df.drop('medv', axis=1)
y = df['medv']

X_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Correct model save path inside the Docker container
model_path = os.path.join(os.path.dirname(__file__), '..', 'deploy_app', 'model.pkl')

# Save the model
joblib.dump(model, model_path)

print(f"Model trained and saved to {model_path}")

