from __future__ import annotations

from tempfile import SpooledTemporaryFile

import pandas as pd


def process_data(filename: str | SpooledTemporaryFile) -> tuple[pd.DataFrame, pd.Series]:
    df = pd.read_csv(filename, na_values="")

    df = df.drop(columns=["Unnamed: 9", "Patient"])
    df = df[df["Outcome"].notna()]

    X = df.drop(columns="Outcome")
    y = df["Outcome"]
    X = (X - X.mean()) / X.std()
    return X, y
