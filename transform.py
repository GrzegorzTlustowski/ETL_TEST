import pandas as pd

def transform(df_header, df_detail, df_product):
    df = df_header[df_header["Status"] == 5]
    df = df_detail.merge(df_header, on="SalesOrderID", how="inner")
    df = df.merge(df_product, on="ProductID", how="left")
    df["revenue"] = df["OrderQty"] * df["UnitPrice"]
    df["Month"] = df["OrderDate"].dt.month
    df["Year"] = df["OrderDate"].dt.year
    return df

def aggregation(df):
    df_monthly = (df.groupby(["Month","Year"]).agg(total_revenue=("revenue", "sum"),total_quantity=("OrderQty", "sum")))
    return df_monthly




