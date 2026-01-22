import pandas as pd


def load_csv(file_path):
    """
    Load CSV file into pandas DataFrame
    """
    try:
        df = pd.read_csv(file_path)
        print(f"✅ Data loaded successfully: {df.shape}")
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"❌ File not found: {file_path}")
    except Exception as e:
        raise Exception(f"❌ Error loading file: {e}")
