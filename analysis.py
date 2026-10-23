
import pandas as pd

df = pd.read_csv("books_cleaned.csv")

print("Dataset Overview")
print(df.head())

print("\nDataset Information")
print(df.info())

print("\nPrice Statistics")
print(df["price"].describe())

print("\nAverage Book Price:")
print(df["price"].mean())

print("\nMost Expensive Book:")
print(df.loc[df["price"].idxmax(), ["title", "price"]])

print("\nCheapest Book:")
print(df.loc[df["price"].idxmin(), ["title", "price"]])

print("\nNumber of Books by Rating:")
print(df["rating"].value_counts().sort_index())

print("\nBook Availability:")
print(df["availability"].value_counts())
