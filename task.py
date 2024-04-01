import pandas as pd
from datetime import datetime

# Process the input data
def process_data(df, load_timestamp):
    df['load_timestamp'] = load_timestamp.strftime('%Y-%m-%d %H:%M:%S')
    return df

# Extract the load_timestamp from the zip file
def extract_load_timestamp(zip_file_path):
    timestamp_str = zip_file_path.split('/')[-1].split('_')[0]
    load_timestamp = datetime.strptime(timestamp_str, '%Y%m%d%H%M%S%f')
    return load_timestamp

# Specify the path to the zip file
zip_file_path = '/home/nineleaps/Downloads/20240305124003123456_Extract 2.zip'

# Extract the load_timestamp
load_timestamp = extract_load_timestamp(zip_file_path)

# Read input data from sample2.csv
sample2_csv_file = '/home/nineleaps/Downloads/sample2.csv'
df = pd.read_csv(sample2_csv_file, sep='\t')

# Process the data
df = process_data(df, load_timestamp)

# Print the modified dataframe
print(df.to_string(index=False, justify='left', col_space=15))

# Save the modified dataframe back to a CSV file
df.to_csv('output.csv', index=False)
