import pandas as pd
import os

def main(file_name: str):
    # Read the Parquet file
    df = pd.read_parquet(file_name)
    split_file_name = file_name.split("/")

    # Save the DataFrame as a CSV file
    print(f"Saving {split_file_name[-1].split(".")[0]} as a CSV file...")
    # df.to_csv(f'./darshan_share/darshan_detail_csvs/application_{split_file_name[-2]}/{split_file_name[-3]}/{split_file_name[-1].split(".")[0]}.csv', index=False)
    df.to_csv(f'./darshan_share/darshan_total_csvs/{split_file_name[-1].split(".")[0]}.csv', index=False)


if __name__ == "__main__":
    path = "./darshan_share/darshan_total/"
    # path = "./darshan_share/darshan_detail/2021/6/21/"
    [main(f"{path}{file}") for file in os.listdir(path) if file]
    