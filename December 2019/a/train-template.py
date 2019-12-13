import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib

import os
from azureml.core.run import Run


# Load training data
train = pd.read_csv('./data/train.csv')

# Select columns

# Split data into train/test datasets

# Train the classifier

# Evaluate the classifier
accuracy = 4.2

# Log evaluation results
print('='*50)
print('Accuracy is', accuracy)
run = Run.get_context()
run.log('accuracy', accuracy)

# Log model
os.makedirs('./outputs', exist_ok=True)
joblib.dump(value=classifier, filename='outputs/model.pkl')