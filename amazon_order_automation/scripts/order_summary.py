import pandas as pd
import matplotlib.pyplot as plt
import os

# Paths
data_path = '../data/amazon_orders_sample.xlsx'
visuals_path = '../visuals'
output_path = '../output'

# Create folders if not exist
os.makedirs(visuals_path, exist_ok=True)
os.makedirs(output_path, exist_ok=True)

# Load the data
df = pd.read_excel(data_path)

# Convert column names to standard form (if needed)
df.columns = df.columns.str.strip()

# Calculate total spend
total_spend = df['Total'].sum()

# Total quantity
total_quantity = df['Quantity'].sum()

# Top 5 categories by spend
top_categories = df.groupby('Category')['Total'].sum().sort_values(ascending=False).head(5)

# Save summary to text file
with open(f'{output_path}/summary.txt', 'w', encoding='utf-8') as f:
    f.write(f'Total Amount Spent: ${total_spend:.2f}\n\n')
    f.write('Top 5 Categories by Spend:\n')
    f.write(top_categories.to_string())
    f.write(f'\n\nTotal Quantity Ordered: {total_quantity}\n')

# Visual - Top Categories by Spend
plt.figure(figsize=(8, 6))
top_categories.plot(kind='bar', color='green')
plt.title('Top 5 Categories by Spend')
plt.xlabel('Category')
plt.ylabel('Total Spend')
plt.tight_layout()
plt.savefig(f'{visuals_path}/top_categories.png')
plt.close()
