import pickle

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from helpers import process_data

x, y = process_data("data.csv", outcomes=True) #collects data from panda data tables

x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2) #splits the data into training and validation values

model = LogisticRegression(C=1.0) #creates a new model

model.fit(x_train, y_train) #fits the model to the data

output_model = pickle.dump(model, open("model.pkl", "wb")) #exports the model to a file that is called when processing new data
