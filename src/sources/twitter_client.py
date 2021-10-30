import os
from typing import List
import requests
from dotenv import load_dotenv
import pandas as pd
from pandas.core.frame import DataFrame
import json 
import re
from datetime import datetime
from sources.chatter_processor import sentiments_with_nltk 

load_dotenv()

def get_security_list():
    # if match is empty
    return ["BTC","ETH","AAPL","TSLA"]

def mine_twitter():
    security_list = get_security_list()
     #= pd.DataFrame()
    result = {}
    for topic in security_list:
        
        mined_sentiments = mine_twitter_topic(topic, 200)
        result[topic] = mined_sentiments
    return result   
def mine_twitter_topic(search_term: str, count: int) -> List:
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

    sentiments_to_save = []
    # Check that the API response was successful
    if response.status_code == 200:
        
        for tweet in response.json()["statuses"]:
            sentiment_to_save = process_tweet(tweet, search_term)
            if sentiment_to_save != None:
               sentiments_to_save.append(sentiment_to_save)
    else:
        print(response.status_code)
    return sentiments_to_save

def process_tweet(tweet, search_term):
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
        sentiment_score = sentiments_with_nltk(s_text)
        if(abs(sentiment_score["score"]) > 0.5000):
            return (s_datetime,s_text,search_term,"TWITTER",sentiment_score)       
        else:
            return None
    else:
        return None


















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