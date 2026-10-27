from bs4 import BeautifulSoup
import pandas as pd
import os

folder = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(folder, "reviews.html")

if not os.path.exists(html_path):
    print("Error: reviews.html not found at:", html_path)
    raise SystemExit(1)

with open(html_path, "r", encoding="utf-8-sig") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")
review_blocks = soup.select(".review")

records = []

for block in review_blocks:
    review_element = block.select_one(".review-text")
    rating_element = block.select_one(".rating")

    review = review_element.get_text(strip=True) if review_element else ""
    rating = rating_element.get_text(strip=True) if rating_element else ""

    records.append({
        "Review": review,
        "Rating": rating
    })

df = pd.DataFrame(records)

if df.empty:
    print("No reviews found.")
else:
    print("Product Reviews:")
    print(df.to_string(index=False))