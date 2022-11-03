
import pandas as pd

FILE_PATH = './data_files/datos.csv'
OUTPUT_PATH = "./data_files/normalized-data.csv"
df_all_data = pd.read_csv(FILE_PATH)

max_values = df_all_data.max()
min_values = df_all_data.min()

normalized_data = ((df_all_data-min_values)/(max_values-min_values))

normalized_data.to_csv(OUTPUT_PATH, header=None, index=False)
