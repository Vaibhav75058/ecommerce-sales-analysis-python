
# Load the cleaned e-commerce sales dataset.

import pandas as pd
from pathlib import Path


def load_data():
    """Load the cleaned retail sales dataset."""

    project_root = Path(__file__).resolve().parent.parent

    file_path = (
        project_root
        / "data"
        / "processed"
        / "retail_sales_cleaned.csv"
    )

    df = pd.read_csv(file_path)

    df["order_date"] = pd.to_datetime(
        df["order_date"], errors="coerce"
    )

    return df


if __name__ == "__main__":
    data = load_data()

    print("Dataset loaded successfully!")
    print("Shape:", data.shape)
    print(data.head())
