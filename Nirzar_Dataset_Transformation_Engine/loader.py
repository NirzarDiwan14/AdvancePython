import pandas as pd 


REQUIRED_COLUMNS = [
    "user_id",
    "order_id",
    "order_date",
    "order_amount",
    "city",
    "payment_mode",
    # "check1",
    # "check2"
]

def load_data(file_path: str) -> pd.DataFrame:
    #loading
    df = pd.read_csv(file_path)
    
    #checking for missing columns
    missing_cols = []
    for col in REQUIRED_COLUMNS:
        if col not in df.columns:
            missing_cols.append(col)
    if missing_cols:
        raise ValueError(f"Missing required cols: {missing_cols}")
    
    # convert datatypes  
    
    df['order_date'] = pd.to_datetime(df['order_date'],errors = "coerce")
    df['order_amount'] = pd.to_numeric(df['order_amount'],errors = "coerce")

    #handling missing values

    #drop columns missing critical info
    # print(df.shape)
    df = df.dropna(subset=["user_id","order_date"])

    #fill  string missing values
    df['city'] = df["city"].fillna(("Unknown"))
    df['payment_mode'] = df["payment_mode"].fillna(("Unknown"))

    # print(df.head())
    #fill numeric missing values
    df["order_amount"] = df["order_amount"].fillna(df["order_amount"].median())
    # print(df.head())

    
    return df



if __name__ == "__main__":
    print("Hello from loader.py")
    df = load_data("raw_data.csv")
    print(df.head())
    print(df.info())

    


