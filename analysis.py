import pandas as pd

# Load data
df = pd.read_csv('Sample - Superstore.csv', encoding='latin-1')

# Fix dates
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.month
df['Year'] = df['Order Date'].dt.year

# Check duplicates
print("Duplicates found:", df.duplicated().sum())
df = df.drop_duplicates()
print("After removing duplicates:", df.shape)

# Check data types
print("\nData types:")
print(df[['Sales', 'Profit', 'Quantity']].dtypes)

# Save clean data
df.to_csv('clean_superstore.csv', index=False)
print("\nClean data saved!")