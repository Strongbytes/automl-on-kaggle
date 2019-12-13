import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib

import os
import argparse
from azureml.core.run import Run

parser = argparse.ArgumentParser()
parser.add_argument('--data-folder', type=str, dest='data_folder')

args = parser.parse_args()
data_folder = args.data_folder
train_file = os.path.join(data_folder, 'train.csv')
print('='*50)
print('Data folder:', data_folder)
print('Train file location:', train_file)

# Load training data

# Select columns

# Split data into train/test datasets

# Train the classifier

# Evaluate the classifier
accuracy = 4.2

# Log evaluation results
print('Accuracy is', accuracy)
run = Run.get_context()
run.log('accuracy', accuracy)

# Log model
os.makedirs('./outputs', exist_ok=True)
joblib.dump(value=classifier, filename='outputs/model.pkl')