# Packages
import pandas as pd
import numpy as np

# Read in data from zip file
zip_file_path = "/workspaces/IDS721_FInal_Team_Project_SP23_Du_Wang/00_source_data/heart_2020_cleaned.csv.zip"
# unzip the file and save it to the same directory as a csv
df = pd.read_csv(zip_file_path, compression='zip')
df.head()