import pandas as pd
import sqlite3

# Load clean data
df = pd.read_csv('clean_superstore.csv')

# Create SQL database
conn = sqlite3.connect('superstore.db')
df.to_sql('sales', conn, if_exists='replace', index=False)
print("Data loaded into SQL!")

# Q1: Sales and Profit by Category
q1 = pd.read_sql("""
    SELECT Category,
        ROUND(SUM(Sales),2) as Total_Sales,
        ROUND(SUM(Profit),2) as Total_Profit
    FROM sales
    GROUP BY Category
    ORDER BY Total_Sales DESC
""", conn)
print("\n--- Sales by Category ---")
print(q1)

# Q2: Top 5 Profitable Products
q2 = pd.read_sql("""
    SELECT [Product Name],
        ROUND(SUM(Profit),2) as Total_Profit
    FROM sales
    GROUP BY [Product Name]
    ORDER BY Total_Profit DESC
    LIMIT 5
""", conn)
print("\n--- Top 5 Products ---")
print(q2)

# Q3: Sales by Region
q3 = pd.read_sql("""
    SELECT Region,
        ROUND(SUM(Sales),2) as Total_Sales,
        ROUND(AVG(Profit),2) as Avg_Profit
    FROM sales
    GROUP BY Region
    ORDER BY Total_Sales DESC
""", conn)
print("\n--- Sales by Region ---")
print(q3)
# Q4: Monthly Sales Trend
q4 = pd.read_sql("""
    SELECT Year, Month,
        ROUND(SUM(Sales),2) as Monthly_Sales
    FROM sales
    GROUP BY Year, Month
    ORDER BY Year, Month
""", conn)
print("\n--- Monthly Trend ---")
print(q4)

# Q5: Bottom 5 Loss Making Products
q5 = pd.read_sql("""
    SELECT [Product Name],
        ROUND(SUM(Profit),2) as Total_Profit
    FROM sales
    GROUP BY [Product Name]
    ORDER BY Total_Profit ASC
    LIMIT 5
""", conn)
print("\n--- Loss Making Products ---")
print(q5)