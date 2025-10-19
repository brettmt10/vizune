import pandas as pd

def flag_coerce(df: pd.DataFrame, col):
    n_df = df.copy()
    o_na = n_df[col].isna()
    n_df[col] = pd.to_numeric(n_df[col], errors='coerce')
    n_df['_inferred_coerce'] = n_df[col].isna() & ~o_na
    return n_df[[col, '_inferred_coerce']]

def type_decision(df_ic: pd.DataFrame):
    return 'float' if df_ic.sum() / len(df_ic) < 0.3 else 'string'

def coerce_vals(df: pd.Series, col, type_d):
    n_df = df.copy()
    if type_d == 'float':
        n_df[col] = pd.to_numeric(n_df[col], errors='coerce')
    else:
        n_df[col] = n_df[col].astype(str)
    return n_df 