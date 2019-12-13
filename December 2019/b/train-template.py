import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import RidgeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib
from azureml.core.run import Run


# Load training data

# Select columns

# Split data into train/test datasets

# Pick classifiers

run = Run.get_context()
os.makedirs('./outputs', exist_ok=True)

# Train and evaluate classifiers
# Serialize each classifier
# Log evaluation results

# Log best model & accuracy
run.log('best_accuracy', best_accuracy)
run.log('best_model', type(best_model).__name__)
