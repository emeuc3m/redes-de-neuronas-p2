import pandas as pd
from sklearn.model_selection import train_test_split

FILE_PATH = './data_files/normalized-data.csv'
df = pd.read_csv(FILE_PATH)

y = pd.DataFrame(list(df.columns))
X = df

X_train, X_test, y_train, y_test = train_test_split(
        X, y,stratify=y, test_size=(1/3))