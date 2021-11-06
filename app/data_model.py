from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from helpers import process_data
from sklearn.linear_model import LogisticRegression
import numpy as np
import pickle
x, y = process_data("data.csv")

x_train, x_val, y_train, y_val = train_test_split(x, y, test_size = 0.2)
model = LogisticRegression(1.0)
model.fit(x_train, y_train)
output_model = pickle.dump(model)
        