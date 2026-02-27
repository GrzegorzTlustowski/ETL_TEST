from dbo import get_engine
import pandas as pd

def extract_SalesOrderHeader():
    engine = get_engine()
    query = """select SalesOrderID,OrderDate,Status from Sales.SalesOrderHeader"""
    return pd.read_sql_query(query, engine)

def extract_SalesOrderDetail():
    engine = get_engine()
    query = """select SalesOrderID,ProductID, OrderQty, UnitPrice from Sales.SalesOrderDetail"""
    return pd.read_sql_query(query, engine)

def extract_Production():
    engine = get_engine()
    query = """select ProductID, Name from Production.Product"""
    return pd.read_sql_query(query, engine)