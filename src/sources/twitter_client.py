import os
import requests
from dotenv import load_dotenv
import pandas as pd
from pandas.core.frame import DataFrame
import json 
import re
load_dotenv()


def mine_twitter(search_term: str, count: int) -> DataFrame:
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
            row = get_data(tweet)
            df_tweets = df_tweets.append(row, ignore_index=True)
    else:
        print(response.status_code)
    return df_tweets


def get_data(tweet):
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

    data = {"created_at": s_datetime, "clean_text": clean_tweet(s_text)}
    print(s_text)
    return data
def clean_tweet(tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def mine_twitter_topics(topics):
    for topic in topics:
        twitter_data = mine_twitter(topic, 200)
        outFileName="/home/pi/dev/augur/data/sentiments/twitter/" + topic + ".json"
        twitter_data.to_json(outFileName)
    

if __name__ == "__main__":
    # function sample call
    # coin_data = get_coin_historical_data("bitcoin", "cad", 30)
    # price_data = get_current_prices(['bitcoin', 'ethereum', 'cardano'])
    topics = ["investing","business & finance", "cryptocurrency"]
    mine_twitter_topics(topics)
   



        

