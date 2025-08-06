import pandas as pd

# Load CSV file
df = pd.read_csv('/Users/user/Desktop/zoilas_project/Snippet.csv', encoding='latin1')

# Optional: clean column names (removes any leading/trailing spaces)
df.columns = df.columns.str.strip()

# Convert 'Fecha de revisión' to datetime format
df['Fecha de revisión'] = pd.to_datetime(df['Fecha de revisión'], format='%Y-%m-%d', errors='coerce')

# Print the first few rows and data types
print(df.head())
print(df.dtypes)

