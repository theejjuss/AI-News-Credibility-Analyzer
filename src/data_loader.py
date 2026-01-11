import pandas as pd
from preprocessing import clean_text

def load_data():
    fake = pd.read_csv("data/raw/Fake.csv")
    real = pd.read_csv("data/raw/True.csv")

    fake["label"] = 0
    real["label"] = 1

    df = pd.concat([fake, real], axis=0)
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    df["clean_text"] = df["text"].apply(clean_text)

    print("Dataset loaded:", df.shape)
    return df

if __name__ == "__main__":
    load_data()
