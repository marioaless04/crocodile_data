import pandas as pd

def load_dataset(path: str) -> pd.DataFrame:
    """Carga el dataset desde un archivo CSV."""
    return pd.read_csv(path)

def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia el dataset:
    - Elimina duplicados
    - Rellena valores nulos en columnas numéricas con la media
    """
    df = df.drop_duplicates()
    df = df.fillna(df.mean(numeric_only=True))
    return df

def save_cleaned_dataset(df: pd.DataFrame, path: str):
    """Guarda el dataset limpio en un nuevo archivo CSV."""
    df.to_csv(path, index=False)
