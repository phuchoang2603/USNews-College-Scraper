import fuzzywuzzy
import pandas as pd
from fuzzywuzzy import process
import json

# Load and clean the dataframes
df1 = pd.read_csv('./csv/data.csv')
df2 = pd.read_csv('./csv/3.csv')
df1['Institution'] = df1['Institution'].str.lower().str.replace('[^a-z\s]', '').str.strip()
df2['Institution'] = df2['Institution'].str.lower().str.replace('[^a-z\s]', '').str.strip()

# Manual mapping for known discrepancies
with open('manual.json') as f:
    manual_mapping = json.load(f)

# Map similar names using fuzzywuzzy
auto_mapping = {}
for name1 in df1['Institution']:
    if name1 not in manual_mapping:
        closest_match = process.extractOne(name1, df2['Institution'])
        if 92 < closest_match[1] < 100:  # Set an appropriate similarity threshold
            auto_mapping[name1] = closest_match[0]
            #write to .txt file
            with open('./csv/log.txt', 'a') as f:
                f.write("Mapped {} to {}".format(name1, closest_match[0]))
                f.write("\n")
        
        else:
            auto_mapping[name1] = name1  # Keep the original name if no close match or the same with original name
            print ("No match or keep the same for: ", name1)

# Update the manual mapping
name_mapping = {**manual_mapping, **auto_mapping}

# Apply the mapping to the "Institution" column in df1
df1['Institution'] = df1['Institution'].map(name_mapping)

# Merge using the mapped column
merged_df = pd.merge(df1, df2, on='Institution', how='outer')

# Save the merged dataframe
merged_df.to_csv('./csv/4.csv', index=False)