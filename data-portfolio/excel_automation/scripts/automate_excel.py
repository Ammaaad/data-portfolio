import pandas as pd
import matplotlib.pyplot as plt
import os

# Paths
data_path = '../data/sales_data.xlsx'
visuals_path = '../visuals'
output_path = '../output'

# Create folders if not exist
os.makedirs(visuals_path, exist_ok=True)
os.makedirs(output_path, exist_ok=True)

# Load the data
df = pd.read_excel(data_path)
df.columns = df.columns.str.strip()

# Total spend and quantity
total_spend = df['Total'].sum()
total_quantity = df['Quantity'].sum()

# Top 5 products by revenue
top_products = df.groupby('Product')['Total'].sum().sort_values(ascending=False).head(5)

# Save summary
with open(f'{output_path}/summary.txt', 'w', encoding='utf-8') as f:
    f.write(f'Total Revenue: ${total_spend:.2f}\n\n')
    f.write('Top 5 Products by Revenue:\n')
    f.write(top_products.to_string())
    f.write(f'\n\nTotal Quantity Sold: {total_quantity}\n')

# Visual - Top 5 Products by Revenue
plt.figure(figsize=(8, 6))
top_products.plot(kind='bar', color='green')
plt.title('Top 5 Products by Revenue')
plt.xlabel('Product')
plt.ylabel('Revenue')
plt.tight_layout()
plt.savefig(f'{visuals_path}/top_products.png')
plt.close()
