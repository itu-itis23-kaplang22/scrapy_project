import json
import pandas as pd
import matplotlib.pyplot as plt

with open("output.json", "r", encoding="utf-8") as file:
    data = json.load(file)

df = pd.DataFrame(data)

# price temizleme
df["price"] = df["price"].astype(str).str.replace("£", "", regex=False).astype(float)

print("Total books:", len(df))
print("Average price:", round(df["price"].mean(), 2))
print("Most expensive book:")
print(df.loc[df["price"].idxmax()])

# Grafik 1: Price distribution
plt.figure(figsize=(8, 5))
plt.hist(df["price"], bins=15)
plt.title("Book Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("price_distribution.png")
plt.show()

# Grafik 2: Top 10 expensive books
top10 = df.sort_values("price", ascending=False).head(10)

plt.figure(figsize=(10, 6))
plt.barh(top10["title"], top10["price"])
plt.title("Top 10 Most Expensive Books")
plt.xlabel("Price (£)")
plt.ylabel("Book Title")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("top_10_expensive_books.png")
plt.show()
