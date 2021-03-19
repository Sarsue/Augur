import os
import requests
from dotenv import load_dotenv
import pandas as pd
from pandas.core.frame import DataFrame
load_dotenv()


def search_for_tweets(search_term: str, count: int) -> DataFrame:
    API_TWITTER_BEARER_TOKEN = os.environ.get('TWITTER_BEARER_TOKEN')
    params = {
        "q": search_term,
        "tweet_mode": "extended",
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
            print(row)
            df_tweets = df_tweets.append(row, ignore_index=True)
    else:
        print(response.status_code)


def get_data(tweet):
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

    data = {"created_at": s_datetime, "text": s_text}
    return data


if __name__ == "__main__":
    # function sample call
    # coin_data = get_coin_historical_data("bitcoin", "cad", 30)
    # price_data = get_current_prices(['bitcoin', 'ethereum', 'cardano'])
    search_for_tweets("bitcoin", 100)
