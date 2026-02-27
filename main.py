from extract import extract_SalesOrderHeader, extract_SalesOrderDetail, extract_Production
from transform import transform, aggregation
from load import  load_monthly
#issue with load to db
def test():
    df_transform = transform(extract_SalesOrderHeader(), extract_SalesOrderDetail(), extract_Production())
    df_agg = aggregation(df_transform)
    df_load = load_monthly(df_agg)
    print('test')
    return df_load


if __name__ == '__main__':
    test()