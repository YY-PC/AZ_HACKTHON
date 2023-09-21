import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import pairwise_distances

train_fields = ['clientId', 'loan','deposits','pension','credit','mortage','report','asset','investment','plan','consulting']

def get_data():
    return pd.read_csv("./train_data.csv")

#print(df_train)
def popularity_based(df):
    top_col = {}
    for col in df.columns[9:]:
        top_col[col] = df[col].value_counts()[1]

    for k, v in top_col.items():
        top_col[k] = np.around(v / df.shape[0], decimals=4)

    return top_col

#print(cos_relation(df_clientIndex(df_train)))

def df_mb(df):
    df_mb = df.copy()
    df_mb = df_mb.set_index('clientId')
    return df_mb
def recommend(clientId, df, prediction):
    client_row = df[df.index == clientId]
    client_services = list(filter(lambda product: client_row[product].to_numpy()[0] == 1, client_row))

    recom = {key: prediction[key] for key in prediction if key not in client_services}

    recom_sort = dict(sorted(recom.items(), key=lambda item: item[1], reverse=True))

    return recom_sort


