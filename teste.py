import polars as pl
import pandas as pd


dataframe_pandas = pd.DataFrame({"id": [1], "saldo": 0})
dataframe_polars = pl.DataFrame({"id": [1], "saldo": 0})

print(dataframe_pandas)
print(dataframe_polars)
