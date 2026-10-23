
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("books_cleaned.csv")

plt.figure(figsize=(8, 5))
plt.hist(df["price"], bins=10, edgecolor="black")
plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("price_distribution.png")
plt.show()

rating_counts = df["rating"].value_counts().sort_index()

plt.figure(figsize=(8, 5))
plt.bar(rating_counts.index, rating_counts.values, edgecolor="black")
plt.title("Number of Books by Rating")
plt.xlabel("Rating (Stars)")
plt.ylabel("Number of Books")
plt.xticks([1, 2, 3, 4, 5])
plt.tight_layout()
plt.savefig("rating_distribution.png")
plt.show()

average_price = df.groupby("rating")["price"].mean()

plt.figure(figsize=(8, 5))
plt.bar(average_price.index, average_price.values, edgecolor="black")
plt.title("Average Book Price by Rating")
plt.xlabel("Rating (Stars)")
plt.ylabel("Average Price (£)")
plt.xticks([1, 2, 3, 4, 5])
plt.tight_layout()
plt.savefig("average_price_by_rating.png")
plt.show()

print("All visualizations created and saved!")
