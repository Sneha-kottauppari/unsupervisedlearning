# Import libraries necessary for this project
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import matplotlib.cm as cm
from IPython.display import display 
# Allows the use of display() for DataFrames

# Pretty display for notebooks
# %matplotlib inline

data=pd.read_csv("customers.csv")
# print(data)
# display(data.describe())
# data.head()

df=data.iloc[:,[2,4,5]]
df.columns=['fresh','grocery','frozen']
# print(df)

pd.plotting.scatter_matrix(data, alpha = 0.3, figsize = (14,8), diagonal = 'kde');