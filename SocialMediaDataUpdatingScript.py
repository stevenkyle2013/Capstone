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


#Update StockPrice csv
#Update Twitter csv
#Update Reddit csv

if __name__ == "__main__":
    
    print("Date to update data to: 'mm/dd/yyyy'")
    update_date = input()
    print("Are you sure to update data to...{} 'Y' 'N'".format(update_date)
    response = input()
          