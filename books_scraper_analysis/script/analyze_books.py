import pandas as pd
import matplotlib.pyplot as plt
import os

# Load dataset
data_path = '../data/books.csv'
df = pd.read_csv(data_path)

# Clean Price column (remove £ sign and convert to float)
df['Price'] = df['Price'].replace('£', '', regex=True).astype(float)

# Calculate summary stats
average_price = df['Price'].mean()
max_price = df['Price'].max()
min_price = df['Price'].min()
most_expensive_book = df.loc[df['Price'].idxmax(), 'Title']
cheapest_book = df.loc[df['Price'].idxmin(), 'Title']

# Save summary
summary_path = '../summary/summary.txt'
os.makedirs(os.path.dirname(summary_path), exist_ok=True)

with open(summary_path, 'w', encoding='utf-8') as f:
    f.write(f"📊 Book Price Summary\n")
    f.write(f"----------------------\n")
    f.write(f"Average Price: £{average_price:.2f}\n")
    f.write(f"Most Expensive Book: {most_expensive_book} - £{max_price:.2f}\n")
    f.write(f"Cheapest Book: {cheapest_book} - £{min_price:.2f}\n")

# 🔹 Plot 1: Price Distribution
plt.figure(figsize=(10, 6))
plt.hist(df['Price'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Book Prices')
plt.xlabel('Price (£)')
plt.ylabel('Number of Books')
plt.grid(True)

visual_path = '../visuals/price_distribution.png'
os.makedirs(os.path.dirname(visual_path), exist_ok=True)
plt.savefig(visual_path)

# 🔹 Plot 2: Top 10 Most Expensive Books
top_10 = df.sort_values(by='Price', ascending=False).head(10)

plt.figure(figsize=(12, 6))
plt.barh(top_10['Title'], top_10['Price'], color='salmon')
plt.title('Top 10 Most Expensive Books')
plt.xlabel('Price (£)')
plt.gca().invert_yaxis()
plt.tight_layout()

top10_path = '../visuals/top_10_expensive_books.png'
plt.savefig(top10_path)

# Confirm
print(f"\nSummary saved to {summary_path}")
print(f"Chart saved to {visual_path}")
print(f"Chart saved to {top10_path}")
