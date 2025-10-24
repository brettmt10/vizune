import pandas as pd

class TypeInference:
    def _flag_coerce_float(self, df_c: pd.Series):
        o_na = df_c.isna()
        ic = pd.to_numeric(df_c, errors='coerce')
        return ic.isna() & ~o_na
    
    def _flag_coerce_dtm(self, df_c: pd.Series):
        o_na = df_c.isna()
        ic = pd.to_datetime(df_c, errors='coerce', format='mixed')
        return ic.isna() & ~o_na

    def _type_decision(self, df_ics: pd.DataFrame):
        # prioritize floats
        if df_ics['ic_float'].sum() / len(df_ics['ic_float']) < 0.3: return 'float'
        elif df_ics['ic_dtm'].sum() / len(df_ics['ic_dtm']) < 0.3: return 'datetime'
        else: return 'string'

    def _coerce_vals(self, df_c, type_d):
        if type_d == 'float':
            return pd.to_numeric(df_c, errors='coerce')
        elif type_d == 'datetime':
            return pd.to_datetime(df_c, errors='coerce', format='mixed')
        return df_c.astype(str)
    
    def infer(self, df: pd.DataFrame):
        metadata = {}
        df_ics = pd.DataFrame()
        for col in df.columns:
            df_c = df[col]
            df_ics['ic_float'] = self._flag_coerce_float(df_c)
            df_ics['ic_dtm'] = self._flag_coerce_dtm(df_c)
            type_d = self._type_decision(df_ics)
            df[col] = self._coerce_vals(df_c, type_d)
            metadata[col] = type_d
        return df, metadata