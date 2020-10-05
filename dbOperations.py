from DbClass import Db
from mergedData import stockData
from mergedData import financeData
import pandas as pd

# Insert DataFrame into sql table
stockDataDb = Db(stockData, 'stockData').df_to_sql()
dataDb = Db(financeData, 'financeData').df_to_sql()
data = Db(None, 'data').sql_to_df()
data.to_pickle('data.pkl')