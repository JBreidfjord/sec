import pickle

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from helpers import process_data

# Collects data from panda data tables
x, y = process_data("data.csv", outcomes=True)

# Splits the data into training and validation values
x_train, x_val, y_train, y_val = train_test_split(x, y)

# Creates a new model
model = LogisticRegression(C=1.0)

# Fits the model to the data
model.fit(x_train, y_train)

# Exports the model to a file that is called when processing new data
output_model = pickle.dump(model, open("model.pkl", "wb"))
