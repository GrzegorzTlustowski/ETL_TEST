from sqlalchemy import create_engine
def get_engine():
    connection_string = (
        "mssql+pyodbc://@localhost\\SQLEXPRESS/AdventureWorks2022"
        "?driver=ODBC+Driver+17+for+SQL+Server"
        "&trusted_connection=yes"
    )
    return create_engine(connection_string)