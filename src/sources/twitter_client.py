import os
import requests
from dotenv import load_dotenv
import pandas as pd
from pandas.core.frame import DataFrame
import json 
import re
from datetime import datetime
import chatter_processor
import storage_manager
load_dotenv()

def get_security_list():
    # if match is empty
    return ["BTC","ETH","AAPL","FB"]

def mine_twitter():
    security_list = get_security_list()
    twitter_data = []
     #= pd.DataFrame()
    for topic in security_list:
        df = mine_twitter_topic(topic, 200)
        storage_manager.save_data(topic,df)
        twitter_data.append(df)
    return twitter_data

def mine_twitter_topic(search_term: str, count: int) -> DataFrame:
    API_TWITTER_BEARER_TOKEN = os.environ.get("TWITTER_BEARER_TOKEN")
    params = {
        "q": search_term,
        "lang": "en",
        "count": count,
    }
    # Request Twitter API
    response = requests.get(
        "https://api.twitter.com/1.1/search/tweets.json",
        params=params,  # type: ignore
        headers={"authorization": "Bearer " + API_TWITTER_BEARER_TOKEN},
    )

    # Create dataframe
    df_tweets = pd.DataFrame()

    # Check that the API response was successful
    if response.status_code == 200:
        for tweet in response.json()["statuses"]:
            row = extract_data(tweet, search_term)
            if row != None:
                df_tweets = df_tweets.append(row, ignore_index=True)
    else:
        print(response.status_code)
    return df_tweets


def extract_data(tweet, search_term):
    # check if the tweet is relevant to the search term
    if "+" in tweet["created_at"]:
        s_datetime = tweet["created_at"].split(" +")[0]
    else:
        s_datetime = iso8601.parse_date(tweet["created_at"]).strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    if "full_text" in tweet.keys():
        s_text = tweet["full_text"]
    else:
        s_text = tweet["text"]
    if search_term in s_text:
        sentiment_score = chatter_processor.sentiments_with_nltk(s_text)
        if(abs(sentiment_score["score"]) > 0.5000):
            return {"creationstamp": s_datetime, "text": s_text, "sentimentlabel":sentiment_score}
        else:
            return None
    else:
        return None



def load_tweets():
    result = []
    tweet_keys = get_security_list()
    for tweet_key in tweet_keys:
        result.append(storage_manager.load_data(tweet_key))
    return result






if __name__ == "__main__":
    count = 3
    for i in range(count):
        tweets_mined_list = mine_twitter()
        print(tweets_mined_list)
    # uniqueList = []
    # for entry in match:
    #     if entry not in uniqueList:
    #         uniqueList.append(entry)
    # print(len(uniqueList),uniqueList)