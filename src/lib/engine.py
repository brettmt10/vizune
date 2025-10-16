import pandas as pd
import numpy as np

def infer(df: pd.DataFrame):
    o_na = df['accuracy'].isna()
    df['accuracy'] = pd.to_numeric(df['accuracy'], errors='coerce')
    df['inferred_coerce'] = df['accuracy'].isna() & ~o_na
    df.loc[df['inferred_coerce'], 'accuracy'] = np.inf
    return df