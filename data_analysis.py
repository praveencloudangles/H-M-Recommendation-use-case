print("data anlysis...............")
from data_loading import data_load

def data_analy():
    df_article, df_cust, df_trans = data_load()

    return df_article, df_cust, df_trans

data_analy()