import pandas as pd

class TypeInference:
    def _flag_coerce(self, df, col):
        n_df = df.copy()
        o_na = n_df[col].isna()
        n_df[col] = pd.to_numeric(n_df[col], errors='coerce')
        n_df['_inferred_coerce'] = n_df[col].isna() & ~o_na
        return n_df['_inferred_coerce']

    def _type_decision(self, df_ic: pd.Series):
        return 'float' if df_ic.sum() / len(df_ic) < 0.3 else 'string'

    def _coerce_vals(self, df, col, type_d):
        n_df = df.copy()
        if type_d == 'float':
            n_df[col] = pd.to_numeric(n_df[col], errors='coerce')
        else:
            n_df[col] = n_df[col].astype(str)
        return n_df 
    
    def infer(self, df: pd.DataFrame, col):
        df_ic = self._flag_coerce(df, col)
        type_d = self._type_decision(df_ic)
        return self._coerce_vals(df, col, type_d)