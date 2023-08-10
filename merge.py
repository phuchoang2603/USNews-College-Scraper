import pandas as pd

# Load the CSV files
df1 = pd.read_csv('1.csv')
df2 = pd.read_csv('2.csv')

# Remove leading and trailing white spaces from all cells
df1 = df1.applymap(lambda x: x.strip() if isinstance(x, str) else x)
df2 = df2.applymap(lambda x: x.strip() if isinstance(x, str) else x)
# df3 = df3.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Merge dataframes based on the "institution" column
merged_df = pd.merge(df1, df2, on='Institution', how='outer')  
# merged_df2 = pd.merge(merged_df, df3, on='Institution', how='outer')  

# Save the merged dataframe to a new CSV file
merged_csv_path = 'merged.csv'
merged_df.to_csv(merged_csv_path, index=False)

print("Merged data saved as CSV:", merged_csv_path)