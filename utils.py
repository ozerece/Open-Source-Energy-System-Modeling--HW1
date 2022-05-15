#Function 1 (Normalize the hourly demand)

import pandas as pd

def norm_df(df):
    sum_s = df.sum()
    for col in df.columns:
        if col == "Time" or col == "_date":
            continue
        df[col] /= sum_s[col]
    return df


#Function 2 (Interpolate the final energy consumption for BE between 2000-2050 )

def interpolate(data, country, fuel, years_interp):
    first_index = data.index.max() + 1 # determine the index to add calculated row to end of dataframe
    for i in country:
        for f in fuel:
            for y in years_interp:
                base_value = float(data[(data.Country==i) & (data.Fuel==f) & (data.Year==y)]['Total(KTOE)'])
                dif = float(data[(data.Country==i) & (data.Fuel==f) & (data.Year==y+5)]['Total(KTOE)'])-float(data[(data.Country==i) & (data.Fuel==f) & (data.Year==y)]['Total(KTOE)'])
                dif = dif/5
                for r in range(1,5):
                    data.loc[first_index] = [i, y+r, f, base_value + dif*r]
                    first_index = first_index + 1
    return data