print("feature engineering.........")
from data_cleaning import data_cleaning
import pandas as pd

def feat_eng():
    final_df = data_cleaning()
    print(final_df)
    
    df = final_df.iloc[:50000]
    
    df.to_csv("Retail_suggetion.csv", index=False)
    
    return final_df
    
feat_eng()
