import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from app.config import config, FEATURES

def load_data():
    df = pd.read_csv(config.data_path)
    df = df.drop_duplicates().dropna(subset=FEATURES + ["Exited"])
    logging.info("Loaded %s rows", len(df))

    X = df[FEATURES]
    y = df["Exited"]
    return train_test_split(
        X, y,
        test_size=config.test_size,
        random_state=config.random_state,
        stratify=y,
    )
