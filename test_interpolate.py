from utils import interpolate
import pandas as pd

data = pd.read_csv("func2_BE_fed.csv", index_col=0)
country = ["BE"]

fuel = ["Electricity"]
years_interp = [2000,2005,2010,2015,2020,2025,2030,2035,2040,2045]

def test_interpolate():
    df = interpolate(data, country, fuel, years_interp)
    for y in years_interp:
        diffs = []
        for r in range(1,6):
            dif = data.loc[data.Year==y+r, 'Total(KTOE)'].values[0] - data.loc[data.Year==y+r-1, 'Total(KTOE)'].values[0]
            diffs.append(dif)
        assert (sum(diffs) + data.loc[data.Year==y, 'Total(KTOE)'].values[0]) == (data.loc[data.Year==y+5, 'Total(KTOE)']).values[0]






