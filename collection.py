from bs4 import BeautifulSoup
import os
import pandas as pd

# Example dictionary
d = {'title': [], 'price': []}

# Directory containing HTML files
directory = "data"

# Iterate through files in the directory
for file in os.listdir(directory):
    try:
        with open(f"{directory}/{file}", encoding="utf-8") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, "html.parser")

        # Fix: Find the element correctly (assuming it's a 'span' or 'div' with a class)
        t = soup.find(attrs={"style": "max-height: 32px; line-height: 16px; -webkit-line-clamp: 2;"})
        p = soup.find(attrs={"class":"css-146c3p1 r-1h7g6bg r-1vgyyaa r-1rsjblm r-142tt33 r-11wrixw"})
        
        # If both title and price are found, append them
        if t and p:
            title = t.get_text(strip=True)
            price = p.get_text(strip=True)
            print(f"Title: {title}, Price: {price}")
            d['title'].append(title)
            d['price'].append(price)
        else:
            # If title or price is missing, append None for each
            d['title'].append(None)
            d['price'].append(None)

    except Exception as e:
        print(e)

# Create DataFrame and save to CSV
df = pd.DataFrame(data=d)
df.to_csv("data.csv", index=False)
