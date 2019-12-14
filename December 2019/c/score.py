import json
import numpy as np
import os
import pickle
from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegression

from azureml.core.model import Model
import pandas as pd

def init():
    global model

    model_path = Model.get_model_path('best_model')
    model = joblib.load(model_path)
    #model =  pickle.load(open(model_path, "rb"))

def run(raw_data):
    data = json.loads(raw_data)
    values = data['Inputs']['input1']['Values']

    try:
        df = pd.DataFrame(values,
            columns=['Type', 'Name', 'Age', 'Breed1', 'Breed2', 'Gender', 'Color1', 'Color2',
                'Color3', 'MaturitySize', 'FurLength', 'Vaccinated', 'Dewormed',
                'Sterilized', 'Health', 'Quantity', 'Fee', 'State', 'RescuerID',
                'VideoAmt', 'Description', 'PetID', 'PhotoAmt'])

        df['IsFree'] = df['Fee'] == 0
        df['IsMulticolor'] = (df['Color2'] != 0) | (df['Color3'] != 0)
        df['IsPurebreed'] = df['Breed2'] == 0

        df.drop(['Name', 'RescuerID', 'PetID', 'Description'], axis=1, inplace=True)

        y = model.predict(df)
        output = np.column_stack([df, y]).tolist()
        return {
                "Results": {
                    "output1": {
                         "type": "ML Service",
                         "value": { 
                             "Values" : output
                            }
                        }
                    }
                }
    except Exception as e:
        return json.dumps({"error": str(e)})
