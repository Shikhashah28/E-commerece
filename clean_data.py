
import pandas as pd

df = pd.read_csv("books_data.csv")

print("Original dataset shape:", df.shape)

print("\nMissing values before cleaning:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()

df["price"] = (
    df["price"]
    .str.replace("£", "", regex=False)
    .astype(float)
)

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["rating"] = df["rating"].map(rating_map)

df = df.dropna(subset=["title", "price", "rating"])

df = df.reset_index(drop=True)

df.to_csv("books_cleaned.csv", index=False)

print("\nCleaned dataset:")
print(df.head())

print("\nCleaned dataset shape:", df.shape)

print("\nData saved to books_cleaned.csv")
