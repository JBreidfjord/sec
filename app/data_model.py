import pickle

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from helpers import process_data

x, y = process_data("data.csv", outcomes=True)
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2)
model = LogisticRegression(C=1.0)
model.fit(x_train, y_train)
output_model = pickle.dump(model, open("model.pkl", "wb"))
