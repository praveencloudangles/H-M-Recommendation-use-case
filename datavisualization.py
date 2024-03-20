print("data visualization.............")

import pandas as pd
import plotly.graph_objects as go
from data_analysis import data_analy


def data_vis():
    
    df_article, df_cust, df_trans = data_analy()
    
    temp = df_article.groupby(["index_name"])["article_id"].nunique()
    df = pd.DataFrame({'Index Name': temp.index,
                       'Articles': temp.values
                      })
    df = df.sort_values(['Articles'], ascending=False)
    fig = go.Figure(go.Bar(x=df['Index Name'], y=df['Articles']))
    fig.update_layout(template='plotly_dark', title='Number of Articles per each Index Name', xaxis_tickangle=-45, xaxis_title='Index Name', yaxis_title='Number of Articles')
    fig.write_image("bar.jpg")
    
    #-------------------------------------------------------------------
    
    temp = df_cust.groupby(["club_member_status"])["customer_id"].count()
    df = pd.DataFrame({'Club Member Status': temp.index,
                       'Customers': temp.values
                      })
    df = df.sort_values(['Customers'], ascending=False)
    fig = go.Figure(go.Bar(x=df['Club Member Status'], y=df['Customers']))
    fig.update_layout(template='plotly_dark', title='Number of Customers per each Club Member Status', xaxis_tickangle=-45, xaxis_title='Club Member Status', yaxis_title='Customers')
    fig.write_image("no_of_customers.jpg")
    
    
    #-------------------------------------------------------------------------
    
    temp = df_article.groupby(["product_group_name"])["product_type_name"].nunique()
    df = pd.DataFrame({'Product Group': temp.index,
                       'Product Types': temp.values
                      })
    df = df.sort_values(['Product Types'], ascending=False)
    fig = go.Figure(go.Bar(x=df['Product Group'], y=df['Product Types']))
    fig.update_layout(template='plotly_dark', title='Number of Product Types per each Product Group', xaxis_tickangle=-45, xaxis_title='Product Group', yaxis_title='Product Types')
    fig.write_image("no_of_product_type_for_pr-group.jpg")
    
    #----------------------------------------------------------------------------
       
    top_products = df_article['prod_name'].value_counts().head(10).index.tolist()
    filtered_df = df_article[df_article['prod_name'].isin(top_products)]

    product_counts = filtered_df['prod_name'].value_counts()

    fig = go.Figure(data=[go.Pie(labels=product_counts.index, values=product_counts.values)])
    
    fig.update_layout(
        template='plotly_dark',
        title='Top 10 Products by Occurrences in Transactions'
    )

    fig.write_image("pie_chart.png")   
    
    return df_article, df_cust, df_trans
    
data_vis()
