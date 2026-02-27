from dbo import get_engine
from sqlalchemy import text

def load_monthly(df_monthly):
    engine = get_engine()

    with engine.begin() as conn:
        conn.execute(text("TRUNCATE TABLE dbo.mart_product_monthly"))

    df_monthly.to_sql(
        "mart_product_monthly",
        engine,
        schema="dbo",
        if_exists="append",
        index=False
    )