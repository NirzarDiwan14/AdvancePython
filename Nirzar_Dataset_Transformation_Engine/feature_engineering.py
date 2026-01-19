import pandas as pd
from datetime import datetime

def add_time_features(df : pd.DataFrame) -> pd.DataFrame:
    """
    Create time-based new features from order_date.
    """
    df = df.copy()

    df["order_month"] = df['order_date'].dt.month
    df["order_day"] = df['order_date'].dt.day
    df["order_weekday"] = df['order_date'].dt.weekday
    df["is_weekend"] = df['order_weekday'].isin([5,6]).astype(int)

    return df


def add_aggregation_features(df : pd.DataFrame) -> pd.DataFrame:
    """
    Generate per-user aggregation features and merge them back.
    """
    df = df.copy()
    today = pd.Timestamp(datetime.today().date())

    user_agg = (
        df.groupby("user_id").agg(
            total_orders = ("order_id","count"),
            total_spend = ("order_amount","sum"),
            avg_order_value = ("order_amount","mean"),
            max_order_value = ("order_amount","max"),
            last_order_date = ("order_date","max")
            ).reset_index()
    )

    user_agg['days_since_last_order'] = (today - user_agg['last_order_date']).dt.days

    user_agg = user_agg.drop(columns = ["last_order_date"])


    df = df.merge(user_agg, on="user_id",how="left")

    return df 


if __name__ == "__main__":

    from loader import load_data
    df = load_data("raw_data.csv")
    df = add_time_features(df)
    df = add_aggregation_features(df)

    print(df.head())
    # print(df.info())