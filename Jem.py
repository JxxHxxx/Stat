import numpy as np
from pandas.core.frame import DataFrame
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from datetime import date

Today = date.today()
today = Today.strftime("%Y-%m-%d")

class stockStat:
    def __init__(self, ticker):
        print("show you %s's stock data" % (ticker))
        self._ticker = ticker

    def get_stock_data(self, start=None, end=None):
        if start == None:
            start = '2021-01-01'
        else:
            start = start

        if end == None:
            end = today
        else:
            end = end

        result = web.get_data_yahoo(self._ticker, start, end)    
        #print(result)
        return result

    def log_pct_change(self, col):
        # col은 dataframe 타입에서의 열을 말합니다.
        result = (np.log(col) - np.log(col).shift(1))*100
        result = result.dropna()    
        #print(result)
        return result

    
    
      


















"""start = datetime.datetime(2019, 1, 1)
end = datetime.datetime(2020, 12, 31)

df_aapl = web.get_data_yahoo("AAPL",start,end)
df_sec = web.get_data_yahoo("005930.KS", start, end)
df_kospi = web.get_data_yahoo('^KS11', start, end)

df_kospi["코스피 증감률"] = (np.log(df_kospi["Close"]) - np.log(df_kospi["Close"]).shift(1))*100
df_sec["삼성전자 증감률"] = (np.log(df_sec["Close"]) - np.log(df_sec["Close"]).shift(1))*100
df_sec["애플 증감률"] = (np.log(df_aapl["Close"]) - np.log(df_aapl["Close"]).shift(1))*100

SM = df_sec["삼성전자 증감률"]
KOSPI = df_kospi["코스피 증감률"]
AAPL = df_aapl["애플 증감률"]

inde_variable = df_sec['삼성전자 증감률', '애플 증감률']
model = sm.OLS(KOSPI, inde_variable).fit() 
model.summary """
