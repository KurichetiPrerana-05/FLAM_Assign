import json
import numpy as np
import pandas as pd
# csv file reading
df=pd.read_csv("data/xy_data.csv")

def data_load():
     # convert the x and y columns into a numpy array
     points=df[["x","y"]].to_numpy()
     return points
    
