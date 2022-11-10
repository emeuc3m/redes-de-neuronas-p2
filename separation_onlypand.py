import pandas as pd

FILE_PATH = './data_files/normalized-data.csv'
df = pd.read_csv(FILE_PATH)

print(df.groupby('NSP', group_keys=False).apply(lambda x: x.sample(frac=(2/3))))
