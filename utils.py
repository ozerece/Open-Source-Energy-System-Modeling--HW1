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

data=pd.read_csv(r'C:\Users\Özer\Desktop\Projects\Invert\Calibration of the base year\Subtract_CookCool.csv', index_col=0)
country=["BE"]

fuel=["coal", "fuel oil", "gas" ,"Electricity", "District heating", "biomass"]
years_interp=[2000,2005,2010,2015,2020,2025,2030,2035,2040,2045]

def interpolate(data, country, fuel, years_interp):
    first_index = data.index.max() + 1 # determine the index to add calculated row to end of dataframe
    for i in country:
        for f in fuel:
            for y in years_interp:
                base_value_cook=float(data[(data.Country==i) & (data.Fuel==f) & (data.Year==y)]['FED_cooking(KTOE)'])
                base_value_cool=float(data[(data.Country==i) & (data.Fuel==f) & (data.Year==y)]['FED_cooling(KTOE)'])
                dif_cook=float(data[(data.Country==i) & (data.Fuel==f) & (data.Year==y+5)]['FED_cooking(KTOE)'])-float(data[(data.Country==i) & (data.Fuel==f) & (data.Year==y)]['FED_cooking(KTOE)'])
                dif_cool=float(data[(data.Country==i) & (data.Fuel==f) & (data.Year==y+5)]['FED_cooling(KTOE)'])-float(data[(data.Country==i) & (data.Fuel==f) & (data.Year==y)]['FED_cooling(KTOE)'])
                dif_cook=dif_cook/5
                dif_cool=dif_cool/5
                for r in range(1,5):
                    data.loc[first_index] = [i, y+r, f, base_value_cook+dif_cook*r, base_value_cool+dif_cool*r, 0]
                    first_index=first_index+1
    data["Total(KTOE)"]=data["FED_cooking(KTOE)"]+data["FED_cooling(KTOE)"]
    return data

interpolate(data, country, fuel, years_interp)