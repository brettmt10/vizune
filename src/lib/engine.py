import pandas as pd
import numpy as np

def flag_coerce(df: pd.DataFrame, col):
    df = df.copy()
    o_na = df[col].isna()
    df[col] = pd.to_numeric(df[col], errors='coerce')
    df['inferred_coerce'] = df[col].isna() & ~o_na
    return df[[col, 'inferred_coerce']]

def type_decision(df: pd.DataFrame):
    return 'float' if df['inferred_coerce'].sum() / len(df) < 0.3 else 'string'