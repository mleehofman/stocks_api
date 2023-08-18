# stocks_api
stock_api
A python program to get information about stocks

***This program makes use of the fmpsdk library and the 
financial modeling prep: https://site.financialmodelingprep.com/***

Important indicators that use the fmpsdk library:

##stock indicators

### Access data for a company such as 52 week high, 52 week low, market capitalization, and key stats to understand a company finance.
fmpsdk.company(apikey=self.api_key,symbol='MSFT')

### revenue and actual Earnings Per Share. The value can be 0 for the upcoming report.
fmpsdk.historical_earning_calendar(apikey=self.api_key, symbol='LLAP')

### Splits are often a bullish sign since valuations get so high that the stock may be out of reach for smaller investors trying to stay diversified.
fmpsdk.historical_stock_split(apikey=self.api_key, symbol='AAPL')


### Annual statements show business activities, results and financial health by providing financial values. All traded companies include key metrics such as revenue in their reports; however, the other metrics may differ for each specific company.
fmpsdk.financial_statement_full_as_reported(apikey=self.api_key,symbol='MSFT')

### financial reports that summarize the inflows and outflows of cash and cash equivalents for a business over a period.
fmpsdk.cash_flow_statement_as_reported(apikey=self.api_key,symbol='LLAP')

### how the company has grown since its initial public offering
fmpsdk.financial_growth(apikey=self.api_key,symbol='LLAP')
fmpsdk.income_statement_growth(apikey=self.api_key,symbol='LLAP')
fmpsdk.balance_sheet_statement_growth(apikey=self.api_key,symbol='LLAP')


### computes ratios for each financial statement presented by the company - annually or by quarter
***IMPORTANT RATIOS FOR ANALYSIS***

fmpsdk.financial_ratios(apikey=self.api_key,symbol='LLAP')

###  ttm is a measure of data over a 12-month period in the past.
fmpsdk.financial_ratios_ttm(apikey=self.api_key,symbol='LLAP')

### Key Metrics such as Market capitalization, PE ratio, Price to Sales Ratio, POCF ratio, Graham Net-Net
_The key metrics are calculated quarter by quarter, year by year. The change in company metrics is essential for valuating a company._

fmpsdk.key_metrics(apikey=self.api_key,symbol='LLAP', period='quarter')

### A proportion of an organization's absolute worth, frequently utilized as a more thorough option in contrast to value market capitalization.
fmpsdk.enterprise_values(apikey=self.api_key,symbol='LLAP', period='quarter')

### Financial Statement Growth of a company based on its financial statement, it compares previous financial statement to get growth of all its statement.
fmpsdk.financial_growth(apikey=self.api_key,symbol='LLAP', period='quarter')

### to estimate the money an investor would receive from an long-term investment, adjusted for the time value of money. how much is the actual stock worth if you would invest in it ###

fmpsdk.discounted_cash_flow(apikey=self.api_key,symbol='MSFT')

### comparison of the DCF with the actual stock price over time ###
fmpsdk.historical_discounted_cash_flow(apikey=self.api_key,symbol='AAPL', period='quarter')

### The value of a company is measured by its market capitalization. It's crucial in determining whether a company is undervalued, fairly valued or overvalued. ###
fmpsdk.market_capitalization(apikey=self.api_key,symbol='AAPL')

### include limit to follow market cap in time to certain period ###
fmpsdk.historical_market_capitalization(apikey=self.api_key,symbol='LLAP')

###returns historical EPS earnings. It includes fields such as estimated and actual EPS (Earnings Per Share). ###
fmpsdk.earnings_surprises(apikey=self.api_key, symbol='LLAP')

### Historical open, close, high and low of a given stock ###
fmpsdk.historical_chart(apikey=self.api_key, symbol='LLAP',time_delta="1min")
fmpsdk.historical_price_full(apikey=self.api_key, symbol='LLAP')

### Stock up to date information for today ###
fmpsdk.quote(apikey=self.api_key,symbol='LLAP')

#Overall indicators

### performance by sector to see which one performs the best. ###
fmpsdk.sectors_performance(apikey=self.api_key)

_Insider trading refers to when a company’s executives, board of directors, and/or major shareholders buy or sell company stock based on non-public company information.
Being aware of insider trades can help identify what insiders (i.e., smart money) think will happen in the future._

fmpsdk.insider_trading(apikey=self.api_key, symbol='LLAP')

### The most negative percent change of all supported stocks is returned by this endpoint.
fmpsdk.losers(apikey=self.api_key)
### The biggest percentage change in supported stocks returns the most gainers.
fmpsdk.gainers(apikey=self.api_key)
