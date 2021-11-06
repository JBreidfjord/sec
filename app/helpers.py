import pandas as pd

def processed_data(filename: str):
    df = pd.read_csv(filename, na_values='')

    df = df.drop(columns=['Unnamed: 9', 'Patient'])
    df = df[df['Outcome'].notna()]

    X = df.drop(columns="Outcome")
    y = df["Outcome"]
    X = (X - X.mean()) / X.std()
    return X, y