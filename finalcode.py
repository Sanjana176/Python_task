import zipfile
import pandas as pd
from datetime import datetime

# Extract the load_timestamp from the zip file
def extract_load_timestamp(zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        timestamp_str = zip_ref.filename.split('/')[-1].split('_')[0]
        load_timestamp = datetime.strptime(timestamp_str, '%Y%m%d%H%M%S%f')
        return load_timestamp

# Read and process sample.csv
def process_csv(csv_file, load_timestamp):
    df = pd.read_csv(csv_file)
    df['load_timestamp'] = load_timestamp
    return df

# Specify the path to the zip file
zip_file_path = '/home/nineleaps/Downloads/20240305124003123456_Extract 2.zip'

# Extract the load_timestamp
load_timestamp = extract_load_timestamp(zip_file_path)

# Process sample.csv
sample_csv_file = '/home/nineleaps/Downloads/sample.csv'
df_sample = process_csv(sample_csv_file, load_timestamp)

# Process sample2.csv
sample2_csv_file = '/home/nineleaps/Downloads/sample2.csv'
df_sample2 = process_csv(sample2_csv_file, load_timestamp)

# Print the modified dataframes
print("Output for sample.csv:")
print(df_sample)
print("\nOutput for sample2.csv:")
print(df_sample2)

# Save the modified dataframes back to CSV files
df_sample.to_csv('sample_modified.csv', index=False)
df_sample2.to_csv('sample2_modified.csv', index=False)
