import pandas as pd
from ReportsDictionary import reports_dict
from projectLogger import Mylogger
import warnings
warnings.filterwarnings('ignore')

class Report:
    def __init__(self, file):
        self.file = file

        self.logger = Mylogger('reports_logger').log()

    def get_cols(self):
        dic = reports_dict
        key = str(self.file).split('-')[1]
        self.cols = dic[key][0]
        self.colsNames = dic[key][1]

    def read_report(self):
        if 'Report Date' in self.colsNames:
            try:
                self.report = pd.read_csv(self.file,  sep='\;', header=0 , usecols= self.cols, names=self.colsNames,
                                          parse_dates=['Report Date'], index_col='Ticker')

            except Exception as e:
                self.logger.error(f'xxxxx Failed to read Report {self.file[:-4]} from text file into a dataframe  xxxx {repr(e)}')
                return False

        else:
            try:
                self.report = pd.read_csv(self.file, sep='\;', header=0, usecols=self.cols, names=self.colsNames, index_col='Ticker')

            except Exception as e:
                self.logger.error(f'xxxxx Failed to read Report {self.file[:-4]} from text file into a dataframe  xxxx {repr(e)}')
                return False

        self.logger.info(f'--------- Read Report: {self.file[:-4]} from text file into a dataframes ----------')

        return self.report

    def report_info(self, report):  # Exploring the data

        print(self.file[:-4]+ ':')
        print(report.head(), '\n')

        print(self.file[:-4] + ' columns type:')
        print(report.dtypes, '\n')

        print(self.file[:-4] + ' empty cells:')
        print(report.isnull().sum(), '\n')

        self.report = report.fillna(0) # Handling empty cells
        print(self.report.isnull().sum(), '\n')

        return self.report