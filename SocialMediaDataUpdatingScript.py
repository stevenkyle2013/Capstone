# Installing important packages
import pandas as pd
import numpy as np
import twint
from psaw import PushshiftAPI
import praw
import datetime
from datetime import datetime as dt
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
    S_df = pd.read_csv('StockData_Test.csv', header=None)
    Latest_date = S_df.iloc[-1,0]
    
    print("Dataset has data up until {}.".format(Latest_date))
    
    print("Date to update data to: 'yyyy-mm-dd'")
    update_date = input()
    print("Are you sure to update data to...{} 'Y' 'N'".format(update_date))
    response = input()
    
    if response == 'Y':
                
        #Converting time to datetime to add one day and putting back to string 
        Latest_date = dt.strptime(Latest_date, '%Y-%m-%d') #Not sure if strptime is the right one
        Latest_date += datetime.timedelta(days=1)
        
        print('Updating from {} to {}'.format(Latest_date, update_date))

        
        # Downloading Roku data from yfinance
        stock_data = yf.Ticker('ROKU')
        new_stock_data = stock_data.history(start = Latest_date, end = update_date)
                
        # updating stock data csv
        new_stock_data.to_csv('/Users/stevenkyle/Documents/Flatiron/Capstone/Capstone/StockData_Test.csv', 
                              mode='a', index=True, header=False)
        
        
        
        # Making twitter days to itter through
        twitter_stock_days = new_stock_data.index.strftime('%Y-%m-%d')
        
        # Update Twitter csv        
        for i in range(len(twitter_stock_days)-1):   
            
            # Configure
            c = twint.Config()
            c.Search = '$ROKU'
    
            ### Change since and until
            c.Since = twitter_stock_days[i]
            next_day = i+1
            c.Until = twitter_stock_days[next_day]
        
            c.Lang = 'en'
            c.Limit = 100  #Has to be increments of 20
            c.Pandas = True
            c.Pandas_clean = True
            c.Pandas_au = True
            c.Popular_tweets = True
            c.Min_likes = 10

            # Running the search
            twint.run.Search(c)

            # Storing to dataframe
            Tweets_df = twint.storage.panda.Tweets_df
    
            if len(Tweets_df) > 0:
         
                #Dropping unwanted columns
                Tweets_df.drop(columns=['conversation_id','created_at','place','hashtags','user_id',
                               'user_id_str','name','link','urls','photos','video','thumbnail','retweet',
                               'quote_url','near','geo','source','user_rt_id','user_rt','retweet_id','reply_to',
                               'retweet_date','translate','trans_src','trans_dest'], inplace=True)
    
            
            Tweets_df.sort_values(by='nlikes', axis=0, ascending=False, inplace=True)
    
            # Take the top 5 in dataframe to write
            df_to_write = Tweets_df[0:5]
    
            # Writting to a csv
            df_to_write.to_csv('/Users/stevenkyle/Documents/Flatiron/Capstone/Capstone/TwitterData_Test.csv', 
                               mode='a', header=False, index=False)
    
            time.sleep(3)
        
        
        
        
        # Update Reddit csv
        
        #print()