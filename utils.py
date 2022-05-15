#Function 1 (Normalize the hourly demand)

import pandas as pd

def norm_df(df):
    sum_s = df.sum()
    for col in df.columns:
        if col == "Time" or col == "_date":
            continue
        df[col] /= sum_s[col]
    return df


#Function 2 ()