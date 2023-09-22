import numpy as np
import pandas as pd
import streamlit
from sklearn.tree import DecisionTreeClassifier

train_fields = ['clientId', 'loan','deposits','pension','credit','mortage','report','asset','investment','plan','consulting']
@streamlit.cache_data
def get_data():
    return pd.read_csv("./train_data.csv")

#print(df_train)
def popularity_recommend(df):
    top_col = {}
    for col in df.columns[9:]:
        top_col[col] = df[col].value_counts()[1]

    for k, v in top_col.items():
        top_col[k] = np.around(v / df.shape[0], decimals=4)

    return top_col

def model_recommend(clientId, df, model=DecisionTreeClassifier(max_depth=10)):
    modelrs = {}
    new_df = df[df.columns.intersection(train_fields)]
    for item in new_df.columns:
        y_train = new_df[item].astype('int')
        x_train = new_df.drop([item], axis=1)
        model.fit(x_train, y_train)
        p_train = model.predict_proba(x_train[x_train.index == clientId])[:, 1]

        modelrs[item] = p_train[0]
    return modelrs

def df_mb(df):
    df_mb = df.copy()
    df_mb = df_mb.set_index('clientId')
    return df_mb

#print(model_recommend('C100', df_mb(get_data())))

def mixed_recommend(clientId, df_p, df_m):
    pb = popularity_recommend(df_p)
    mb = model_recommend(clientId, df_m)
    mixed = {}
    for k, v in pb.items():
        mixed[k] = v * 0.5 + mb[k] * 0.5

    return mixed

#print(mixed_recommend('C100', get_data(), df_mb(get_data())))
def recommend(clientId, df, prediction):
    client_row = df[df.index == clientId]

    client_services = list(filter(lambda product: client_row[product].to_numpy()[0] == 1, client_row))

    rec_result = {key: prediction[key] for key in prediction if key not in client_services}

    rec_result_sort = dict(sorted(rec_result.items(), key=lambda item: item[1], reverse=True))

    return rec_result_sort.keys()

#print(recommend('C001', df_mb(get_data()), popularity_based(get_data())))


