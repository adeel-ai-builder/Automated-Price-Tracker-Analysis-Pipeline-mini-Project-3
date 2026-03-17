import pandas as pd
from sqlalchemy import create_engine

engine=create_engine("sqlite:///price_tracker.db")
df = pd.read_sql("SELECT * FROM prices", engine)

price_change = df.groupby("title")["price"].agg(["min", "max"])
print(price_change.head())