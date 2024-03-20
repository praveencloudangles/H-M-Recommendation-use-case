print("feature engineering.........")
import pandas as pd
import numpy as np


def add_true_randomly(row):

    # Choose the number of columns to add True values randomly
    num_columns = np.random.randint(3, 10)  # Choose randomly between 2 and 3 columns

    # Randomly select num_columns columns from the DataFrame
    chosen_columns = np.random.choice(df.columns, size=num_columns, replace=False)

    # Add two or more True values to the chosen columns in the current row
    for column in chosen_columns:
        row[column] = True

    return row

path = "https://stock-market-usecase.s3.amazonaws.com/Retail_suggetion.csv"
df = pd.read_csv(path)
# Apply the function to each row of the DataFrame
df_modified = df.apply(add_true_randomly, axis=1)

print(df_modified)
df_modified.drop(columns=df_modified.columns[0], axis=1, inplace=True)

df_updated=df_modified.iloc[:12]


df_updated.to_csv("final.csv", index=False)
