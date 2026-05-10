import pandas as pd

class DataCleaning:
    def handle_missing_values(self, df, strategy="mean"):
        if strategy == "mean":
            numeric_columns = df.select_dtypes(include="number").columns
            if len(numeric_columns) > 0:
                df.loc[:, numeric_columns] = df.loc[:, numeric_columns].fillna(df.loc[:, numeric_columns].mean())
            return df
        if strategy == "median":
            numeric_columns = df.select_dtypes(include="number").columns
            if len(numeric_columns) > 0:
                df.loc[:, numeric_columns] = df.loc[:, numeric_columns].fillna(df.loc[:, numeric_columns].median())
            return df
        if strategy == "mode":
            return df.fillna(df.mode().iloc[0])
        if strategy == "drop":
            return df.dropna()
        return df

    def remove_duplicates(self, df):
        return df.drop_duplicates()

    def fix_data_types(self, df):
        for col in df.columns:
            converted = pd.to_numeric(df[col], errors="coerce")
            if converted.notna().any():
                df[col] = converted.where(converted.notna(), df[col])
        return df

    def clean_data(self, df):
        df = self.handle_missing_values(df)
        df = self.remove_duplicates(df)
        df = self.fix_data_types(df)
        return df
