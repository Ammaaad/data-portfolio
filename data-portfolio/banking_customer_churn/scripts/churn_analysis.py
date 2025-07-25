import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('../data/bank.csv')

# Clean data
df.dropna(inplace=True)

# Churn by Age
sns.histplot(data=df, x='Age', hue='Exited', kde=True)
plt.title('Churn Distribution by Age')
plt.savefig('../visuals/churn_by_age.png')

# Product Usage vs Churn
sns.countplot(data=df, x='NumOfProducts', hue='Exited')
plt.title('Churn by Product Count')
plt.savefig('../visuals/products_vs_churn.png')

