# Roku Price Prediction incorporating Sentiment analysis
By: Steven Kyle

## Aim
The goal of this project is to test if incorporating sentiment data gathered on social media would help predict future stock prices.

## Data
- The code to gather data can be found in the Gathering_Data notebook.
- The sentiment data was gathered from Reddit and Twitter.
- 1,183 social media posts were gathered.
- The stock data for ROKU was gathered from yfinance.
- Stock data consisted of the days closing price and spanned from September 28, 2017 - May 28, 2021

## Plot of ROKU Closing price

<img src="https://github.com/stevenkyle2013/Capstone/blob/main/Pictures/RawRokuPrice.png" width="500">


## EDA on Sentiment Analysis
To get a better sense of what kind of chatter ROKU was involved with wordclouds for Reddit and Twitter Data were created.

Reddit

<img src="https://github.com/stevenkyle2013/Capstone/blob/main/Pictures/Reddit_Word_Cloud.png" width="500">

Twitter

<img src="https://github.com/stevenkyle2013/Capstone/blob/main/Pictures/Twitter_Word_Cloud.png" width="500">

As you can see, Reddit posts seem to highly revolve around earnings and Twitter posts seem to incorporate multiple stock tickers in the posts.

To get a better understanding of if there is an apparent correlation between sentiment and price movemen the previous days sentiment was compared to the stock price movement. Shown below is the results from that comparison, there was almost a 50/50 chance that the stock price movement reflected the sentiment from the previous days.

<img src="https://github.com/stevenkyle2013/Capstone/blob/main/Pictures/Sentiment_StockPrice_Cor.png" width="500">
<img src="https://github.com/stevenkyle2013/Capstone/blob/main/Pictures/Price_Movement_Yesterdays_Sentiment.png" width="500">

## Comparison of Model preformance

LSTM Model using stock data

<img src="https://github.com/stevenkyle2013/Capstone/blob/main/Pictures/LSTM_Predictions.png" width="500">

Close up on the test set

<img src="https://github.com/stevenkyle2013/Capstone/blob/main/Pictures/LSTM_Predictions_CloseUp.png" width="500">

LSTM Model using stock and sentiment data

<img src="https://github.com/stevenkyle2013/Capstone/blob/main/Pictures/Multi_LSTM_Predictions.png" width="500">

Close up on the test set

<img src="https://github.com/stevenkyle2013/Capstone/blob/main/Pictures/Multi_LSTM_Predictions_CloseUp.png" width="500">



## Conclusion
In the beginning there seemed to be no apparent correlation between stock price and sentiment. However, the model was able to bring the Test RMSE down from 15.506 to 13.585 when incorporating sentiment analysis data. The model using the sentiment and stock data was also able to follow the training data more closely.

## Future Direction
- Make a more robust way of scoring sentiment data
- Gather more sentiment data from other sources of social media
- Make a dashboard that will report tomorrows predicted closing price

## Recommendation
Sentiment data did help predict next day stock price more accurately. Even though it was only a slight improvement I recommend trying to incorporate it in any Stock Data Anaylsis.
