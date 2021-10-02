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



# This is so twint will be able to work
import nest_asyncio
nest_asyncio.apply()


if __name__ == "__main__":
    
    #Fetching latest date we have data on
    S_df = pd.read_csv('StockData.csv', header=None)
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
        new_stock_data.drop(columns=['Dividends','Stock Splits'], axis=0, inplace = True)

        
        # updating stock data csv
        new_stock_data.to_csv('/Users/stevenkyle/Documents/Flatiron/Capstone/Capstone/StockData.csv', 
                              mode='a', index=True, header=False, line_terminator=None)
        
        
        
        # Making days to itter through
        New_days = new_stock_data.index.strftime('%Y-%m-%d')
        
        # Update Twitter csv        
        for i in range(len(New_days)-1):   
            
            # Configure
            c = twint.Config()
            c.Search = '$ROKU'
    
            ### Change since and until
            c.Since = New_days[i]
            next_day = i+1
            c.Until = New_days[next_day]
        
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
                df_to_write.to_csv('/Users/stevenkyle/Documents/Flatiron/Capstone/Capstone/TwitterData.csv', 
                                   mode='a', header=False, index=False)
    
            time.sleep(3)
        
        
        # Update Reddit csv
        Reddit_subreddits = ['stocks', 'investing', 'stockmarket', 'economy', 'wallstreetbets', 'options', 'Daytrading']
        
        # Looping throught the dates
        for i in range(len(New_days) - 1):
    
            r = praw.Reddit(client_id=client_id,
                            client_secret=client_secret,
                            user_agent=user_agent)

            api = PushshiftAPI(r)
    
            # Setting parameters and doing a search
            start_epoch = New_days[i]
            next_day = i+1
            end_epoch = New_days[next_day]

            api_request_generator = api.search_submissions(subreddit=Reddit_subreddits,
                                                           after = start_epoch, before=end_epoch,
                                                           q='(ROKU)|(Roku)|(roku)|(#Roku)|(#ROKU)|(#roku)|($ROKU)|($Roku)|($roku)',
                                                           limit=1000)
    
            # Adding search data to a dataframe
            Reddit_df = pd.DataFrame(columns =['ID','Num_Comments','Score','Subreddit','Title','Upvote_Ratio','Created',
                                   'Created_utc','Self_text','Date'] )
            ID=[]
            Num_Comments=[]
            Score=[]
            Subreddit = []
            Title = []
            Upvote_Ratio = []
            Created = []
            Created_utc = []
            Self_text = []
            Date = []
    
            for submissions in api_request_generator:
                ID.append(submissions.id)
                Num_Comments.append(submissions.num_comments)
                Score.append(submissions.score)
                Subreddit.append(submissions.subreddit)
                Title.append(submissions.title)
                Upvote_Ratio.append(submissions.upvote_ratio)
                Created.append(submissions.created)
                Created_utc.append(submissions.created_utc)
                Self_text.append(submissions.selftext)
                Date.append(New_days[i])
    
            temp_df = pd.DataFrame({'ID':ID,
                            'Num_Comments':Num_Comments,
                            'Score':Score,
                            'Subreddit':Subreddit,
                             'Title':Title,
                            'Upvote_Ratio':Upvote_Ratio,
                            'Created':Created,
                            'Created_utc':Created_utc,
                            'Self_text':Self_text,
                            'Date':Date})

            Reddit_df = Reddit_df.append(temp_df)
            Reddit_df.sort_values(by='Score', axis=0, ascending=False, inplace=True)
            Reddit_df.drop(Reddit_df[(Reddit_df['Self_text']=='[deleted]')|(Reddit_df['Self_text']=='[removed]')].index, 
                          inplace=True)
            Reddit_df.drop(Reddit_df[Reddit_df['Score']<10].index, inplace=True)
            dataframe_to_write = Reddit_df[0:5]
    
            # Writing dataframe to a csv
            dataframe_to_write.to_csv('/Users/stevenkyle/Documents/Flatiron/Capstone/Capstone/redditdata.csv', mode='a',
                                     header=False, index=False)
    
            time.sleep(3)
        