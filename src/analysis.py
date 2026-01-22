import pandas as pd


def descriptive_stats(df):
    stats = {
        "mean": df.mean(numeric_only=True),
        "median": df.median(numeric_only=True),
        "std": df.std(numeric_only=True),
        "min": df.min(numeric_only=True),
        "max": df.max(numeric_only=True),
        "correlation": df.corr(numeric_only=True)
    }

    print("📊 DESCRIPTIVE STATISTICS")
    print("========================")
    print("Mean:\n", stats["mean"])
    print("\nMedian:\n", stats["median"])
    print("\nStd:\n", stats["std"])

    return stats
