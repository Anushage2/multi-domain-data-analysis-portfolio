import pandas as pd

def data_quality_report(df):
    report = {}

    report["shape"] = df.shape
    report["missing_values"] = df.isnull().sum()
    report["duplicate_rows"] = df.duplicated().sum()
    report["data_types"] = df.dtypes

    print("📋 DATA QUALITY REPORT")
    print("======================")
    print(f"Shape: {report['shape']}")
    print("\nMissing Values:")
    print(report["missing_values"])
    print(f"\nDuplicate Rows: {report['duplicate_rows']}")
    print("\nData Types:")
    print(report["data_types"])

    return report


