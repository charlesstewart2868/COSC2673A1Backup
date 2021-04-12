import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

bostonHouseFrame = pd.read_csv('./housing.data.csv', delimiter='\s+')

# print(bostonHouseFrame)
print(bostonHouseFrame.head(3))
bostonHouseFrame.shape
bostonHouseFrame.info()
bostonHouseFrame.describe()