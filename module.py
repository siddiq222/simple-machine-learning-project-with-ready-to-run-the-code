import pandas as pd
import numpy as np
import json
import random
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
import argparse
import pickle
from playsound3 import playsound
import warnings
warnings.filterwarnings("ignore")


class data_gen():

    def __init__(self,num_samples,file_path):
        self.num_samples = num_samples
        self.file_path = file_path

    def generate(self):
        n_samples = self.num_samples
        bio_length = np.random.randint(10, 500, n_samples)
        pics_count = np.random.randint(1, 7, n_samples)
        spotify_connected = np.random.choice([0, 1], size=n_samples, p=[0.4, 0.6])
        top_interest = np.random.choice(['Gaming', 'Travel', 'Fitness', 'Food', 'Music'], n_samples)
        matches_per_week = (pics_count * 3) + (bio_length / 100) + np.random.normal(0, 2, n_samples)
        matches_per_week = np.clip(matches_per_week, 0, 30).astype(int)
        prob = (pics_count * 0.1) + (spotify_connected * 0.2) + (bio_length / 1000)
        swiped_right = [1 if x > np.random.random() else 0 for x in prob]
        df = {
            'bio_length': bio_length.tolist(),
            'pics_count': pics_count.tolist(),
            'top_interest': top_interest.tolist(),
            'spotify_connected': spotify_connected.tolist(),
            'swiped_right': swiped_right
            }
        return df

    def save_data(self):
        df = self.generate()
        print(self.file_path)
        with open(self.file_path,"w") as file:
            json.dump(df,file)
            file.close()
        

class pipeline():

    def __init__(self,datapath,model_save_path):
        self.datapath = datapath 
        self.model_save_path = model_save_path

    def load_data(self):
        with open(self.datapath,"r") as file:
            var = json.load(file)
            file.close()
        var = pd.DataFrame(var)
        return var # Dataframe

    def preprocessing(self):
        df = self.load_data()
        le = LabelEncoder()
        df["top_interest"] = le.fit_transform(df["top_interest"])
        independent_cols = df.drop(columns="swiped_right")
        target_col = df["swiped_right"]
        return independent_cols,target_col

    def train(self):
        independent_cols,target_col = self.preprocessing()
        model = LogisticRegression()
        model.fit(independent_cols,target_col)
        print("model has been built successfully")
        return model

        
    def save_model(self):
        model = self.train()
        with open(self.model_save_path,"wb") as file:
            pickle.dump(model,file)
            file.close()
        
        
class inference():

    def __init__(self,model_path):
        self.model_path = model_path

    def load_model(self):
        with open(self.model_path,"rb") as file:
            model = pickle.load(file)
            file.close()
        return model

