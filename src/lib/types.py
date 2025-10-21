import pandas as pd

class TypeInference:
    def _flag_coerce(self, df_c: pd.Series):
        o_na = df_c.isna()
        ic = pd.to_numeric(df_c, errors='coerce')
        return ic.isna() & ~o_na

    def _type_decision(self, df_ic: pd.Series):
        return 'float' if df_ic.sum() / len(df_ic) < 0.3 else 'string'

    def _coerce_vals(self, df_c, type_d):
        if type_d == 'float':
            return pd.to_numeric(df_c, errors='coerce')
        return df_c.astype(str) 
    
    def infer(self, df: pd.DataFrame):
        metadata = {}
        for col in df.columns:
            df_c = df[col]
            df_ic = self._flag_coerce(df_c)
            type_d = self._type_decision(df_ic)
            df[col] = self._coerce_vals(df_c, type_d)
            metadata[col] = type_d
        return df, metadata