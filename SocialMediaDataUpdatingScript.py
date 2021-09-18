# Installing important packages
import pandas as pd
import numpy as np
import twint
from psaw import PushshiftAPI
import praw
import datetime as dt
import yfinance as yf
import requests 
import requests.auth
from Config import *
import time


pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)


# This is so twint will be able to work
import nest_asyncio
nest_asyncio.apply()


if __name__ == "__main__":
    
    #Fetching latest date we have data on
    S_df = pd.read_csv('StockData_test.csv', header=None)
    Latest_date = S_df.iloc[-1,0]
    
    print("Dataset has data up until {}.".format(Latest_date))
    
    print("Date to update data to: 'yyyy-mm-dd'")
    update_date = input()
    print("Are you sure to update data to...{} 'Y' 'N'".format(update_date))
    response = input()
    
    if response == 'Y':
        
        print('Updating from {} to {}'.format(Latest_date, update_date))
        
          
        # Downloading Roku data from yfinance
        stock_data = yf.Ticker('ROKU')
        new_stock_data = stock_data.history(start = Latest_date, end = update_date)
        print(new_stock_data)
        
        #stock_data.to_csv(path_or_buf='/Users/stevenkyle/Documents/Flatiron/Capstone/Capstone/yesyestest.csv',index=True)
        
        # updating stock data csv
        #stock_data.to_csv('/Users/stevenkyle/Documents/Flatiron/Capstone/Capstone/StockData_test.csv', 
        #                  mode='a', index=False)
         

        
        # Update Twitter csv
        
        # Update Reddit csv
        
        #print()