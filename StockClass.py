from projectLogger import Mylogger
import yfinance as yf
from yahooquery import Ticker
from datetime import timedelta
import csv

class Stock:
    def __init__(self, df, indx):
        self.df = df
        self.indx = indx

        self.logger = Mylogger('stock_data_logger').log()

    def get_ticker_and_dates(self):
        try:
            self.ticker = self.df.iloc[self.indx]['Ticker']
            self.firstDate = self.df.iloc[self.indx]['first']
            self.lastDate = self.df.iloc[self.indx]['last']

            self.logger.info(f'----Got Data ---- for ticker: {self.ticker}, first date: {self.firstDate}, last date {self.lastDate}')

        except Exception as e:
            self.logger.error(f'xxxx Failed to get ticker and dates for ticker {self.ticker} xxxx {repr(e)}').format(self.ticker, repr(e))
            return False

        return self.ticker

    def get_sector(self):
        print(self.ticker)
        try:
            company = Ticker(self.ticker)
            profileDict = company.asset_profile
            self.sector = profileDict[self.ticker]['sector']

            self.logger.info(f'----Got Sector ---- for ticker: {self.ticker}')

        except Exception as e:
            self.logger.error(f'xxxx Failed to get sector for ticker {self.ticker} xxxx {repr(e)}')

            self.sector = 'Null'

        return self.sector

    def define_start_end_dates(self, aDate):
        self.startDate = aDate.date()
        delta = timedelta(5)
        self.endDate = self.startDate + delta

        return self.startDate, self.endDate

    def dates_to_str(self, startDate, endDate):
        self.start = startDate.strftime('%Y-%m-%d')
        self.end = endDate.strftime('%Y-%m-%d')

        return self.start, self.end

    def get_price_by_date(self):
        try:
            price_df = yf.download(self.ticker, self.start, self.end)
            self.date = price_df.index[0]
            self.price = price_df.iloc[0]['Adj Close']

            self.logger.info(f'----Got Price ---- for ticker: {self.ticker}, first date: {self.firstDate}, last date {self.lastDate}')

        except Exception as e:
            self.logger.error(f'xxxx Failed to get price for ticker {self.ticker} xxxx {repr(e)}')

            self.date = 'Null'
            self.price = 'Null'

        return self.date, self.price

    def write_to_csv(self, indx, ticker, date, price, sector):
        headers = ['Index', 'Ticker', 'Date', 'Price', 'Sector']
        try:
            with open('stock_data.csv', 'a+', newline='') as f:
                csv_file = csv.writer(f, delimiter=',')
                if f.tell() == 0:
                    csv_file.writerow(headers)

                csv_file.writerow([indx, ticker, date, price, sector])

                self.logger.info(f'---- Price data for ticker: {self.ticker} at: {self.date} was added to csv file ----')

        except Exception as e:
            self.logger.error(f'xxxx- Failed to write price for ticker: {self.ticker} at: {self.date} -xxxx {repr(e)}')

        return