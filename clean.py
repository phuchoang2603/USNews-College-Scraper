import pandas as pd

# Load the CSV file
csv_path = 'data.csv'
df = pd.read_csv(csv_path)

# Drop rows with all NaN values (empty rows)
df_cleaned = df.dropna(how='all')

# Define a dictionary with column name changes
column_name_changes = {
    'institution.displayName': 'Institution',
    'institution.schoolType': 'School Type',
    'ranking.sortRank' : 'Rank',
    'searchData.enrollment.rawValue' : 'Enrollment',
    'searchData.acceptanceRate.rawValue' : 'Acceptance Rate',
    'searchData.hsGpaAvg.rawValue' : 'Average HS GPA',
    'searchData.satAvg.displayValue' : 'Average SAT Score',
    'searchData.engineeringRepScore.rawValue' : 'Engineering Rep Score',
    'searchData.businessRepScore.rawValue' : 'Business Rep Score',
    'searchData.computerScienceRepScore.rawValue' : 'Computer Science Rep Score',
}

# Rename the columns
df_cleaned.rename(columns=column_name_changes, inplace=True)

# Save the cleaned data back to the CSV file
df_cleaned.to_csv(csv_path, index=False)

print("Empty rows deleted from CSV:", csv_path)
