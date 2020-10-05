import pandas as pd
from getReportData import reports

stockData = pd.read_csv('stock_data.csv')

basePrice = pd.DataFrame(stockData, columns=['Ticker', 'Date', 'Price']).set_index('Ticker')
basePrice = basePrice[basePrice['Price'] != 'Null']
basePrice = basePrice.loc[~basePrice.index.duplicated(keep='first')]

print('Base Price: \n', basePrice)

stockData = pd.DataFrame(stockData, columns = ['Ticker', 'Date', 'Price', 'Sector'])

print('Stock Data Rows count with Null: ', len(stockData))
stockData = stockData[stockData['Price'] != 'Null']
print('Stock Data Rows count with no Nulls values: ', len(stockData))

stockData['Price'] = stockData['Price'].astype(float)
stockData['Date'] = pd.to_datetime(stockData['Date'])
stockData['Return'] = stockData.groupby('Ticker')['Price'].pct_change()
stockData = stockData.dropna().set_index('Ticker')
print('\n Stock Data: \n', stockData.head())
print('\n Reports Data: \n', reports.head())
print(reports.columns)

reportsData = reports.merge(basePrice['Price'], how='right', left_index=True, right_index=True)
reportsData = reportsData.loc[~reportsData.index.duplicated(keep='first')]

financeData = reportsData.merge(stockData[['Return', 'Sector']], how='right', left_index=True, right_index=True)
financeData = financeData.loc[~financeData.index.duplicated(keep='first')]
financeData = financeData.rename(columns={'Return': 'Yield until 2018'})

print('\n')
print(financeData.isnull().sum(), '\n')
financeData = financeData.dropna()

financeData[['Shares (Diluted)', 'Revenue', 'Pretax Income(Loss)', 'Net Income', 'Cash', 'Assets',
       'Current Liabilities', 'Long Term Debt', 'Total Liabilities', 'Retained Earnings', 'Equity', 'Change in Inventories',
       'Net Cash from Operating Activities', 'Dividends Paid', 'Price','Yield until 2018']]\
       = financeData[['Shares (Diluted)', 'Revenue','Pretax Income(Loss)', 'Net Income', 'Cash', 'Assets',
       'Current Liabilities', 'Long Term Debt', 'Total Liabilities','Retained Earnings', 'Equity', 'Change in Inventories',
       'Net Cash from Operating Activities', 'Dividends Paid', 'Price','Yield until 2018']].astype(float)

financeData['Ten Baggers'] = financeData['Yield until 2018'] >= 10

def color(val):
    if val < 0:
        color = 'red'
    elif val >= 5:
        color = 'blue'
    elif val >= 10:
        color = 'green'
    return f'color: {color}'

financeData.style.applymap(color, subset=['Yield until 2018'])

print('Merdged Data: \n', financeData)
print('Data Columns: \n', financeData.columns)

target = financeData['Ten Baggers'].value_counts()
print(target)

ten_baggers = financeData[financeData['Yield until 2018'] >= 10]
print('Ten Baggers: \n' , ten_baggers)


financialRatios = financeData
financialRatios['PreTax E/R'] = financeData['Pretax Income(Loss)']/financeData['Revenue']
financialRatios['Trailing P/E'] = financeData['Price']/ (financeData['Net Income']/financeData['Shares (Diluted)'])
financialRatios['P/(E+D)'] =  financeData['Price']/((financeData['Pretax Income(Loss)']-financeData['Dividends Paid'])/financeData['Shares (Diluted)'])
financialRatios['P/(E+C)'] = financeData['Price']/((financeData['Pretax Income(Loss)']+financeData['Cash'])/financeData['Shares (Diluted)'])
financialRatios['P/OperatingCash'] = financeData['Price']/ (financeData['Net Cash from Operating Activities']/financeData['Shares (Diluted)'])
financialRatios['D/E'] = financialRatios['Total Liabilities']/financialRatios['Equity']
financialRatios['C/CD'] = financialRatios['Cash']/financialRatios['Current Liabilities']
financialRatios['LD/E'] = financialRatios['Cash']/financialRatios['Equity']
financialRatios = financialRatios.drop(['Shares (Diluted)','Pretax Income(Loss)', 'Net Income', 'Cash', 'Assets',
                                        'Current Liabilities', 'Long Term Debt', 'Total Liabilities','Equity',
                                        'Change in Inventories','Net Cash from Operating Activities', 'Dividends Paid'], axis=1)

print(financialRatios)