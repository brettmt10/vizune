import pandas as pd
import numpy as np

def flag_coerce(df: pd.DataFrame, col):
    n_df = df.copy()
    o_na = n_df[col].isna()
    n_df[col] = pd.to_numeric(n_df[col], errors='coerce')
    n_df['inferred_coerce'] = n_df[col].isna() & ~o_na
    return n_df[[col, 'inferred_coerce']]

def type_decision(df: pd.DataFrame):
    return 'float' if df['inferred_coerce'].sum() / len(df) < 0.3 else 'string'

def coerce_vals(df: pd.DataFrame, col, type_d):
    if type_d == 'float':
        df[col] = pd.to_numeric(df[col], errors='coerce')
    else:
        df[col] = df[col].astype(str)
    return df