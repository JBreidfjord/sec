from __future__ import annotations

from tempfile import SpooledTemporaryFile

import pandas as pd
from sklearn.linear_model import LogisticRegression


def process_data(filename: str | SpooledTemporaryFile) -> pd.DataFrame:
    """[summary]

    Args:
        filename (str | SpooledTemporaryFile): [description]

    Returns:
        tuple[pd.DataFrame, pd.Series]: [description]
    """
    df = pd.read_csv(filename, na_values="")

    df = df.drop(columns=["Unnamed: 9", "Patient"])
    df = df[df["Outcome"].notna()]

    x = df.drop(columns="Outcome")
    x = (x - x.mean()) / x.std()
    return x


def get_predictions(x: pd.DataFrame, model: LogisticRegression) -> pd.Series:
    """[summary]

    Args:
        x (pd.DataFrame): [description]
        model (LogisticRegression): [description]

    Returns:
        pd.Series: [description]
    """
    ...
