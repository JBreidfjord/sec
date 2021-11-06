import pandas as pd

def data_with_outcomes(filename: str):
    df = pd.read_csv(filename, na_values='')

    df = df.drop(columns=['Unnamed: 9', 'Patient'])
    df = df[df['Outcome'].notna()]

    X = df.drop(columns="Outcome")
    y = df["Outcome"]
    
    return X, y
    