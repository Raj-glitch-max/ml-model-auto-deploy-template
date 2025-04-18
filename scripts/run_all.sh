#!/bin/bash

echo "Step 1: Building model training Docker image..."
docker build -t model-trainer ../train_model

echo "Step 2: Running training container to generate model.pkl..."
docker run --rm -v "$(pwd)/../deploy_app:/output" model-trainer

echo "model.pkl should now be in deploy_app/"

echo "Step 3: Building deployment app Docker image..."
docker build -t model-api ../deploy_app

echo "Step 4: Running the app container..."
docker eun -p 5000:5000 model-api
