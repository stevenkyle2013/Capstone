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
    
    print("Date to update data to: 'yyyy/mm/dd'")
    update_date = input()
    print("Are you sure to update data to...{} 'Y' 'N'".format(update_date))
    response = input()
    
    if response == 'Y':
         
        #Fetching lastest date we have on file
        S_df = pd.read_csv('StockData.csv', header=None)
        Latest_date = S_df.iloc[-1,0]
        
        print('Updating from {} to {}'.format(Latest_date, update_date))
        
        # Update stock price csv
        S_df 
        
# Need to open and write to stock price csv        dataframe_to_write.to_csv('/Users/stevenkyle/Documents/Flatiron/Capstone/Capstone/redditdata.csv', mode='a', header=False, index=False)

        
        # Update Twitter csv
        
        # Update Reddit csv
        
        print()