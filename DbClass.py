from sqlalchemy import create_engine
import pandas as pd

class Db:
    def __init__(self, df, tableName):
        self.df = df
        self.tableName = tableName

        # define the connection
        self.driver = 'SQL Server'
        self.server = 'LAPTOP-CQVMAKEL'
        self.database = 'TenBaggersProject'

        self.engine = create_engine("mssql+pyodbc://" + self.server + '/' + self.database + '?Trusted_Connection=yes&driver=' + self.driver)

    def df_to_sql(self): # load pandas dataframe into sql table
        self.df.to_sql(self.tableName, con=self.engine, if_exists='append', schema='dbo')

    def sql_to_df(self):
        query = f'select * from {self.tableName}'
        dfName = pd.read_sql(query, self.engine)

        return dfName




