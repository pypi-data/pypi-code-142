import sqlalchemy

def get_mssql_connection_local():
    """creates sqlalchemy connection engine to mssql database
    as defined by the MSSQL environment variables"""

    driver='ODBC Driver 17 for SQL Server'
    driver_str = '+'.join(driver.strip("\'").split(' '))
    db_name = 'MotoPfoheForecasting'

    con_str = f'mssql+pyodbc://localhost/{db_name}?driver={driver_str}'
    client = sqlalchemy.create_engine(con_str)
    return(client)