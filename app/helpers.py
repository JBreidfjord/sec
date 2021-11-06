from __future__ import annotations

from tempfile import SpooledTemporaryFile

import pandas as pd
from sklearn.linear_model import LogisticRegression


def process_data(filename: str | SpooledTemporaryFile, outcomes: bool = False):
    """Parse and format .csv file into a DataFrame

    Args:
        filename (str | SpooledTemporaryFile): .csv file to upload
        outcomes (bool): Bool that represents if the outcomes should be returned. Defaults to False.
    """

    df = pd.read_csv(filename)  # Store the uploaded .csv file in a DataFrame
    patients = df["Patient"]
    # Drop unnecessary columns
    if "Unnamed: 9" in df.columns:
        df = df.drop(columns="Unnamed: 9")
    if "Patient" in df.columns:
        df = df.drop(columns="Patient")

    x = df.drop(columns="Outcome")  # Store x data without labels
    if outcomes:
        y = df["Outcome"]  # Store outcome column labels
    x = (x - x.mean()) / x.std()  # Normalizes the values of x

    # Return data with labels if outcomes is True
    if outcomes:
        return x, y
    # Otherwise return data and patient numbers
    return x, patients


def get_predictions(x: pd.DataFrame, model: LogisticRegression) -> pd.Series:
    """
    Uses given model to classify patients using given data

    Args:
        x (pd.DataFrame): Input data
        model (LogisticRegression): Inference LogisticRegression model trained on patient data

    Returns:
        pd.Series: Series containing the predicted outcome for each patient
    """
    return model.predict(x)
