from utils import norm_df
import pandas as pd

_df = pd.read_csv("func1_BE_load.csv")

def test_norm_df():
    df = norm_df(_df)
    assert df["Load - Residential - hot water"].sum() == 1
    assert df["Load - Tertiary - hot water"].sum() == 1