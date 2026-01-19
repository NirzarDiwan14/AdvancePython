from loader import load_data
from feature_engineering import add_time_features, add_aggregation_features
from encoder import encode_features

def run_pipeline(input_path:str,output_path:str) -> None:
    """
    Full data transformation pipeline.
    """

    print("Loading data")
    df = load_data(input_path)

    print("Adding time-based features")
    df = add_time_features(df)

    print("Adding aggregation features")
    df = add_aggregation_features(df)

    print("Encoding categorical features")
    df = encode_features(df)

    print("Saving dataset")
    df.to_csv(output_path, index=False)

    print(f"Pipeline completed successfully!")
    print(f"Output is in: {output_path}")

if __name__ == "__main__":
    INPUT_PATH = "raw_data.csv"
    OUTPUT_PATH = "features_dataset.csv"

    run_pipeline(INPUT_PATH, OUTPUT_PATH)