import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('clean_superstore.csv')
conn = sqlite3.connect('superstore.db')
df.to_sql('sales', conn, if_exists='replace', index=False)

# Run queries
q1 = pd.read_sql("SELECT Category, ROUND(SUM(Sales),2) as Total_Sales FROM sales GROUP BY Category ORDER BY Total_Sales DESC", conn)

q2 = pd.read_sql("SELECT Region, ROUND(SUM(Sales),2) as Total_Sales FROM sales GROUP BY Region ORDER BY Total_Sales DESC", conn)

# Build chart
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle('Superstore Sales Dashboard', fontsize=16, fontweight='bold')

# Chart 1
axes[0].bar(q1['Category'], q1['Total_Sales'], color=['#2563EB','#1D9E75','#D85A30'])
axes[0].set_title('Sales by Category')
axes[0].set_ylabel('Total Sales ($)')

# Chart 2
axes[1].pie(q2['Total_Sales'], labels=q2['Region'], autopct='%1.1f%%')
axes[1].set_title('Sales by Region')

plt.tight_layout()
plt.savefig('sales_dashboard.png', dpi=150, bbox_inches='tight')
print("Dashboard saved!")