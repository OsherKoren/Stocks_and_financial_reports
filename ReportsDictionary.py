"""
Income headers = "Ticker;SimFinId;Currency;""Fiscal Year"";""Fiscal Period"";""Report Date"";""Publish Date"";
             ""Shares (Basic)"";""Shares (Diluted)"";Revenue;""Cost of Revenue"";""Gross Profit"";""Operating Expenses"";
             ""Selling, General & Administrative"";""Research & Development"";""Depreciation & Amortization"";
             ""Operating Income (Loss)"";""Non-Operating Income (Loss)"";""Interest Expense, Net"";
             ""Pretax Income (Loss), Adj."";""Abnormal Gains (Losses)"";""Pretax Income (Loss)"";
             ""Income Tax (Expense) Benefit, Net"";""Income (Loss) from Continuing Operations"";
             ""Net Extraordinary Gains (Losses)"";""Net Income"";""Net Income (Common)"
"""

"""
Balance headers = "Ticker;SimFinId;Currency;""Fiscal Year"";""Fiscal Period"";""Report Date"";""Publish Date"";
                    ""Shares (Basic)"";""Shares (Diluted)"";""Cash, Cash Equivalents & Short Term Investments"";
                    ""Accounts & Notes Receivable"";Inventories;""Total Current Assets"";""Property, Plant & Equipment, Net"";
                    ""Long Term Investments & Receivables"";""Other Long Term Assets"";""Total Noncurrent Assets"";
                    ""Total Assets"";""Payables & Accruals"";""Short Term Debt"";""Total Current Liabilities"";
                    ""Long Term Debt"";""Total Noncurrent Liabilities"";""Total Liabilities"";
                    ""Share Capital & Additional Paid-In Capital"";""Treasury Stock"";""Retained Earnings"";
                    ""Total Equity"";""Total Liabilities & Equity"
"""

"""
Cash headers = "Ticker;SimFinId;Currency;""Fiscal Year"";""Fiscal Period"";""Report Date"";""Publish Date"";
                ""Shares (Basic)"";""Shares (Diluted)"";""Net Income/Starting Line"";""Depreciation & Amortization"";
                ""Non-Cash Items"";""Change in Working Capital"";""Change in Accounts Receivable"";
                ""Change in Inventories"";""Change in Accounts Payable"";""Change in Other"";
                ""Net Cash from Operating Activities"";""Change in Fixed Assets & Intangibles"";
                ""Net Change in Long Term Investment"";""Net Cash from Acquisitions & Divestitures"";
                ""Net Cash from Investing Activities"";""Dividends Paid"";""Cash from (Repayment of) Debt"";
                ""Cash from (Repurchase of) Equity"";""Net Cash from Financing Activities"";""Net Change in Cash"
"""

# Reports dictionary
reports_dict = {'income': # report file
                    [[0,3, 5, 8, 9 ,19,25], # report columns
                     ['Ticker', 'Fiscal Year', 'Report Date', 'Shares (Diluted)', 'Revenue', # report columns name
                      'Pretax Income(Loss)', 'Net Income']
                     ],
                'balance':
                [[0, 3, 9,17,20, 21, 23, 26, 27 ],
                ['Ticker', 'Fiscal Year', 'Cash', 'Assets', 'Current Liabilities',
                'Long Term Debt', 'Total Liabilities', 'Retained Earnings', 'Equity']
                 ],
                'cashflow':
                [[0, 3, 14, 17, 22],
                 ['Ticker', 'Fiscal Year', 'Change in Inventories', 'Net Cash from Operating Activities',
                  'Dividends Paid']
                 ]
                }
