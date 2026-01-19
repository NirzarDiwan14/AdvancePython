import pandas as pd



def one_hot_encode(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Apply one-hot encoding to specified categorical columns.
    """
    df = df.copy()
    df = pd.get_dummies(df,columns=columns,drop_first= False)
    return df 

def frequency_encode(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Apply frequency encoding to a single categorical column.
    """

    df = df.copy()
    freq_map = df[column].value_counts(normalize=True)
    df[f"{column}_frequency"] = df[column].map(freq_map)
    return df

def encode_features(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()
    df = frequency_encode(df,"city")
    df = one_hot_encode(df,["city","payment_mode"])
    return df

if __name__ == "__main__":
    from loader import load_data
    from feature_engineering import add_time_features, add_aggregation_features

    df = load_data("raw_data.csv")
    df = add_time_features(df)
    df = add_aggregation_features(df)
    df = encode_features(df)

    print(df.head())
    print(df.info())