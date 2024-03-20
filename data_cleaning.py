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
    top_n_unique_values = merged_df['prod_name'].value_counts().head(120).index.tolist()

    filtered_df = merged_df[merged_df['prod_name'].isin(top_n_unique_values)]

    pivot_table = pd.pivot_table(filtered_df, index=['customer_id', 'article_id','product_type_name', 'product_group_name','t_dat'], columns='prod_name', values='price', aggfunc=lambda x: True, fill_value=False)

    pivot_table.reset_index(inplace=True)
    
    columns_to_drop = ['customer_id', 'article_id', 'product_type_name', 'product_group_name', 't_dat']

    for column in columns_to_drop:
        if column in pivot_table.columns:
            pivot_table.drop(columns=[column], inplace=True)
            
    return pivot_table

data_cleaning()