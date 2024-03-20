print("data cleaning............")

from data_analysis import data_analy
import pandas as pd


def data_cleaning():

    df_articles, df_customer, df_transaction = data_analy()
    df_articles.drop(['product_code','product_type_no','graphical_appearance_no', 'graphical_appearance_name', 'colour_group_code', 'colour_group_name',
                        'perceived_colour_value_id', 'perceived_colour_value_name', 'perceived_colour_master_id', 'perceived_colour_master_name',
                        'department_no', 'department_name', 'index_code', 'index_name', 'index_group_no', 'index_group_name', 'section_no',
                        'section_name', 'garment_group_no', 'garment_group_name', 'detail_desc'], axis=1, inplace=True)
    

    merged_df = pd.merge(df_articles, df_transaction, on='article_id', how='left')
    merged_df.dropna(inplace=True)
    merged_df.drop_duplicates(inplace=True)
    print("merged_df------------", merged_df)
            
    return df

data_cleaning()
