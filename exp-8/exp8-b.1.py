
import os
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

folder = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(folder, "product_reviews.csv")

reviews = [
    "This product is excellent and amazing",
    "I love this product and its quality",
    "Very good product and great service",
    "The product is bad and disappointing",
    "Poor quality and terrible experience",
    "The product is okay and average",
    "Excellent value for money",
    "I am unhappy with this purchase"
]

if not os.path.exists(csv_path) or os.path.getsize(csv_path) == 0:
    pd.DataFrame({"review": reviews}).to_csv(csv_path, index=False)

df = pd.read_csv(csv_path)

if df.empty or "review" not in df.columns:
    df = pd.DataFrame({"review": reviews})
    df.to_csv(csv_path, index=False)

analyzer = SentimentIntensityAnalyzer()

df["sentiment_score"] = df["review"].fillna("").astype(str).apply(
    lambda text: analyzer.polarity_scores(text)["compound"]
)

df["sentiment"] = df["sentiment_score"].apply(
    lambda score: "Positive" if score >= 0.05
    else "Negative" if score <= -0.05
    else "Neutral"
)

print("Product Reviews and Sentiment Analysis:")
print(df.to_string(index=False))

text = " ".join(df["review"].dropna().astype(str))

if text.strip():
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color="white"
    ).generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Product Reviews Word Cloud")
    plt.show()

print("\nSentiment Summary:")
print(df["sentiment"].value_counts())
