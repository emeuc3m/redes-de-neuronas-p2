import pandas as pd

FILE_PATH = './data_files/normalized-data.csv'
TRAIN_PATH = './data_files/train-data-spl.csv'
TEST_PATH = './data_files/test-data-spl.csv'
df = pd.read_csv(FILE_PATH)

train = df.groupby('NSP', group_keys=False).apply(lambda x: x.sample(frac=(2/3)))
test = df.drop(train.index)

train.to_csv(TRAIN_PATH, index=False)
test.to_csv(TEST_PATH , index=False)