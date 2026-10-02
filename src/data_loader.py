"""
src/data_loader.py
------------------
Hàm tiện ích để load và validate dữ liệu Steam Games.
"""

import pandas as pd
import os

# Đường dẫn mặc định tới file dữ liệu gốc
DEFAULT_DATA_PATH = os.path.join(
    os.path.dirname(__file__), "..", "data", "raw", "games_march2025_cleaned.csv"
)


def load_data(filepath: str = DEFAULT_DATA_PATH) -> pd.DataFrame:
    """
    Load dữ liệu Steam Games từ file CSV.

    Args:
        filepath: Đường dẫn tới file CSV. Mặc định là data/raw/games_march2025_cleaned.csv

    Returns:
        pd.DataFrame: DataFrame chứa toàn bộ dữ liệu.

    Raises:
        FileNotFoundError: Nếu file không tồn tại.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(
            f"Không tìm thấy file dữ liệu tại: {filepath}\n"
            "Vui lòng tải file CSV từ Kaggle và đặt vào thư mục data/raw/"
        )

    print(f"📂 Đang load dữ liệu từ: {filepath}")
    df = pd.read_csv(filepath)
    print(f"✅ Đã load xong! Shape: {df.shape} (rows x cols)")
    return df


def get_basic_info(df: pd.DataFrame) -> None:
    """In thông tin cơ bản về DataFrame."""
    print("=" * 50)
    print(f"📊 Số hàng     : {df.shape[0]:,}")
    print(f"📊 Số cột      : {df.shape[1]}")
    print(f"📊 Bộ nhớ      : {df.memory_usage(deep=True).sum() / 1024**2:.1f} MB")
    print(f"📊 Duplicate   : {df.duplicated().sum():,} hàng")
    print("=" * 50)
    print("\n📋 Kiểu dữ liệu từng cột:")
    print(df.dtypes)
    print("\n📋 Missing values (%):")
    missing = (df.isnull().sum() / len(df) * 100).round(2)
    print(missing[missing > 0].sort_values(ascending=False))
