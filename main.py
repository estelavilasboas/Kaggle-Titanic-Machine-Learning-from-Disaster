import numpy as np
import pandas as pd

# training set
train_dt = pd.read_csv("./titanic/train.csv")
# test set
test_dt = pd.read_csv("./titanic/test.csv")

train_dt.describe()
train_dt.info()

#análise exploratória