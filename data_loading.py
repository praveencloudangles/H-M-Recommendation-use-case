print("data loading..............")
import pandas as pd


def data_load():
    path_art = "https://stock-market-usecase.s3.amazonaws.com/articles.csv"
    df_article = pd.read_csv(path_art)
    
    path_cust = "https://stock-market-usecase.s3.amazonaws.com/customers.csv"
    df_cust = pd.read_csv(path_cust)
    
    path_trans = "https://stock-market-usecase.s3.amazonaws.com/transactions_train.csv"
    df_trans = pd.read_csv(path_trans)
    
    return df_article, df_cust, df_trans
    
data_load()