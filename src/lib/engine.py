import pandas as pd
import numpy as np

def flag_coerce(df: pd.DataFrame, col):
    o_na = df[col].isna()
    df[col] = pd.to_numeric(df[col], errors='coerce')
    df['inferred_coerce'] = df[col].isna() & ~o_na
    df.loc[df['inferred_coerce'], col] = np.inf
    return df

def type_decision(df: pd.DataFrame, col):
    num_coerce = df['inferred_coerce'].sum() / len(df)