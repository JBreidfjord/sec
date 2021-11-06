from __future__ import annotations

from tempfile import SpooledTemporaryFile

import pandas as pd
from sklearn.linear_model import LogisticRegression


def process_data(filename: str | SpooledTemporaryFile, outcomes: bool = False) -> pd.DataFrame:
    """Parse and format .csv file into a panda DataFrame

    Args:
        filename (str | SpooledTemporaryFile): .csv file to upload
        outcomes (bool): Bool that represents if the outcomes should be returned. Defaults to False.

    Returns:
        pd.DataFrame: All data in the uploaded .csv file that contibutes to
                        potential diabetes
    """
   
    
    df = pd.read_csv(filename, na_values="") #Store the uploaded .csv file in a DataFrame

    df = df.drop(columns=["Unnamed: 9", "Patient"]) #Drop the empty data column and the patient number column from the DataFrame
    df = df[df["Outcome"].notna()] #Drop the rows when the outcome is NaN 

    x = df.drop(columns="Outcome") #Store all the factors that affect diabetes chance in x
    y = df["Outcome"] #Store the outcome column in y
    x = (x - x.mean()) / x.std() #Normalizes the values of x

    return x, y if outcomes else x  #return either both the contributing factors and the outcomes if outcomes == True
                                                #else, return the contributing factors  


def get_predictions(x: pd.DataFrame, model: LogisticRegression) -> pd.Series:
    """The function uses the data from the panda tables that doesn't contain outcomes
        and uses the model that was exported from data_model to predict whether or not 
        a patient has diabetes or not

    Args:
        x (pd.DataFrame): Inputted framework of data obtained form the .csv file
        model (LogisticRegression): Model obtained from a test set of data, which was run through a logistics regression

    Returns:
        pd.Series: Outputs the panda array of the prediction of whether the patient has diabetes or not
    """
    return model.predict(x)
