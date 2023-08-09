import pandas as pd

# Load the CSV file
csv_path = 'data.csv'
df = pd.read_csv(csv_path)

# Drop rows with all NaN values (empty rows)
df.dropna(how='all')

# Rename the columns
column_name_changes = {
    'institution.displayName': 'Institution',
    'institution.schoolType': 'School Type',
    'ranking.displayRank' : 'Rank',
    'searchData.enrollment.rawValue' : 'Enrollment',
    'searchData.acceptanceRate.rawValue' : 'Acceptance Rate',
    'searchData.hsGpaAvg.rawValue' : 'Average HS GPA',
    'searchData.satAvg.displayValue' : 'Average SAT Score',
    'searchData.engineeringRepScore.rawValue' : 'Engineering Rep Score',
    'searchData.businessRepScore.rawValue' : 'Business Rep Score',
    'searchData.computerScienceRepScore.rawValue' : 'Computer Science Rep Score',
}

df.rename(columns=column_name_changes, inplace=True)

# Split the "Average SAT Score" column into two columns
df[['25th Percentile SAT Score', '75th Percentile SAT Score']] = df["Average SAT Score"].str.split('-', expand=True)

df.drop(columns=["Average SAT Score"], inplace=True)

# Update three major Rep Scores columns to be numeric
columns_to_update = ['Engineering Rep Score', 'Business Rep Score', 'Computer Science Rep Score']

for column in columns_to_update:
    df[column] = df[column].apply(lambda x: 1 if x == '< 2.0' else x)

# Remove rows where "Rank" is "Unranked", and remove the "#" from the "Rank" column
df_unranked = df[df['Rank'] != 'Unranked']
df_unranked['Rank'] = df_unranked['Rank'].str.replace('#', '')

def process_rank(rank):
    if '-' in rank:
        ranks = rank.split('-')
        median = (int(ranks[0]) + int(ranks[1])) / 2
        return int(median)
    else:
        return int(rank)

df_unranked['Rank'] = df_unranked['Rank'].apply(process_rank)

# Save the cleaned data back to the CSV file
df_unranked.to_csv(csv_path, index=False)

print("Cleaned data: ", csv_path)
