from __future__ import annotations

from tempfile import SpooledTemporaryFile

import pandas as pd
from sklearn.linear_model import LogisticRegression


def process_data(filename: str | SpooledTemporaryFile, outcomes: bool = False) -> pd.DataFrame:
    """[summary]

    Args:
        filename (str): [description]
        outcomes (bool, optional): [description]. Defaults to False.

    Returns:
        pd.DataFrame: [description]
    """
    df = pd.read_csv(filename, na_values="")

    df = df.drop(columns=["Unnamed: 9", "Patient"])
    df = df[df["Outcome"].notna()]

    x = df.drop(columns="Outcome")
    y = df["Outcome"]
    x = (x - x.mean()) / x.std()

    return x, y if outcomes else x


def get_predictions(x: pd.DataFrame, model: LogisticRegression) -> pd.Series:
    """[summary]

    Args:
        x (pd.DataFrame): [description]
        model (LogisticRegression): [description]

    Returns:
        pd.Series: [description]
    """
    ...
