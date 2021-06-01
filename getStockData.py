from StockClass import Stock
import pandas as pd
from getReportData import groupedTicker
from projectLogger import Mylogger

def get_stock_data(stocks_df, stock_index):
    flowLogger = Mylogger('flow_logger').log()
    flowLogger.info(f' --------------------------------- Flow Process Started------------------------------------')

    stockFlow = pd.read_csv('stock_flow.csv', sep="-").set_index('steps')['functions'].to_dict()
    stock = Stock(stocks_df, stock_index)
    for step in stockFlow:
        eval(stockFlow[step])

    flowLogger.info(f' ---------------------------------  Process Completed ------------------------------------')

def start_flow(df):
    flowLogger = Mylogger('flow_logger').log()
    try:
        for i in range(30, len(df.index)):
            get_stock_data(df, df.index[i])

        flowLogger.info(f' ---------------------------------  Process Completed ------------------------------------')

    except Exception as e:
        flowLogger.error(f'xxxxxxxxxxxxxxxxxxxxxxxxxxx Flow Program Stopped xxxxxxxxxxxxxxxxxxxxxxxxxxx {repr(e)}')

    return True

start_flow(groupedTicker)
