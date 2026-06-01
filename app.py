import pandas as pd

# Read Data from CSV file into a dataframe
"""
utf-8 encoding is used to read the file, if there is an error 
in reading the file, then we can use Latin1 encoding
"""
# gcsfs is a library that allows us to read and write files from Google Cloud storage
# df = pd.read_csv("Basic/sales_data_sample.csv", encoding="Latin1")

#df = pd.read_excel("Basic/SampleSuperstore.xlsx")
df = pd.read_json("Basic/sample_Data.json")

print(df)