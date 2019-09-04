#%%
import os
import csv
import pandas as pd
import glob

path = r'C:\DRO\DCL_rawdata_files'                     # use your path
# advisable to use os.path.join as this makes concatenation OS independent
all_files = glob.glob(os.path.join(path, "*.csv"))

df_from_each_file = (pd.read_csv(f) for f in all_files)
concatenated_df = pd.concat(df_from_each_file, ignore_index=True)

# minn_csv = os.path.join('../DataFiles', 'Indianapolis_IMPD_UCR_2015_Data.csv')
# row_count = 0

# with open(minn_csv, 'r') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=',')
#     # header = next(csvreader)

#     # Loop through the rows ...     
#     for row in csvreader:
#         row_count += 1
# print(row_count)


#%%
