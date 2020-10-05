from ReportClass import Report
import pandas as pd

def getReportData(fileName):
        report = Report(fileName)
        report.get_cols()
        df = report.read_report()
        modifiedDf = report.report_info(df)
        return modifiedDf

# Set the reports by file names
income = getReportData('us-income-annual.txt')
balance = getReportData('us-balance-annual.txt')
cashflow = getReportData('us-cashflow-annual.txt')

# Join data frames of income , balance and cash into one dataframe by Ticker
def join_reports(report1, report2, report3):
    print(report1.shape[0] == report2.shape[0])
    print(report2.shape[0] == report3.shape[0])
    print(report1.shape[0] == report3.shape[0])

    report2 = report2.drop('Fiscal Year', axis=1)
    report3 = report3.drop('Fiscal Year', axis=1)

    reports_df = pd.concat([report1, report2, report3], axis=1, join='inner')

    print(reports_df, '\n')
    return reports_df

reports = join_reports(income, balance, cashflow)

dates_df = pd.DataFrame(reports['Report Date'])
print(dates_df.head(), '\n')

groupedTicker = dates_df.groupby('Ticker')['Report Date'].agg(['first','last']).apply(list).reset_index()
print(groupedTicker)
