import json
import pandas as pd
import matplotlib.pyplot as plt

with open("output.json", "r", encoding="utf-8") as file:
    data = json.load(file)

df = pd.DataFrame(data)

df["price"] = df["price"].astype(str).str.replace("£", "", regex=False).astype(float)

print("Total books:", len(df))
print("Average price:", round(df["price"].mean(), 2))

# 🎨 COLOR PALETTES
colors1 = ["#ff6b6b", "#feca57", "#48dbfb", "#1dd1a1", "#5f27cd"]
colors2 = ["#ff9ff3", "#54a0ff", "#00d2d3", "#f368e0", "#ff9f43"]
colors3 = ["#ee5253", "#0abde3", "#10ac84", "#222f3e", "#ff9f43"]

# 1) Price Distribution
plt.figure(figsize=(8,5))
plt.hist(df["price"], bins=15, color="#ff6b6b", edgecolor="black")
plt.title("Book Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("price_distribution.png")
plt.close()

# 2) Top 10 Most Expensive Books
top10 = df.sort_values("price", ascending=False).head(10)

plt.figure(figsize=(10,6))
plt.barh(top10["title"], top10["price"], color=colors2)
plt.title("Top 10 Most Expensive Books")
plt.xlabel("Price (£)")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("top10_expensive_books.png")
plt.close()
plt.style.use("ggplot")
# 3) Rating Distribution
if "rating" in df.columns:
    plt.figure(figsize=(6,4))
    df["rating"].value_counts().plot(kind="bar", color=colors3)
    plt.title("Rating Distribution")
    plt.xlabel("Rating")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("rating_distribution.png")
    plt.close()

# 4) Average Price by Rating
if "rating" in df.columns:
    plt.figure(figsize=(6,4))
    df.groupby("rating")["price"].mean().plot(kind="bar", color=colors1)
    plt.title("Average Price by Rating")
    plt.xlabel("Rating")
    plt.ylabel("Average Price (£)")
    plt.tight_layout()
    plt.savefig("average_price_by_rating.png")
    plt.close()

print("🎉 All colorful charts saved!")
