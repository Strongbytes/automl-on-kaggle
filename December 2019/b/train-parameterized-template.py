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

import argparse
import importlib

parser = argparse.ArgumentParser()
parser.add_argument('--algorithm', type=str, dest='algorithm')

args = parser.parse_args()
algorithm = args.algorithm
print('Using algorithm:', algorithm)

# Load & split training data

partition = algorithm.rpartition('.')
algorithm_class = getattr(importlib.import_module(partition[0]), partition[2])
classifier = algorithm_class()
print(classifier)

run = Run.get_context()
os.makedirs('./outputs', exist_ok=True)

# Train & evaluate classifier
# Log metrics
# Log classifier