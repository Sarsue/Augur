import os
from typing import List
import requests
from dotenv import load_dotenv
import pandas as pd
import json 
import re
from datetime import datetime
from text_processor import sentiments_with_nltk 
from datetime import datetime
from prawcore.exceptions import ResponseException
from psaw import PushshiftAPI
import praw
import time

load_dotenv()


def mine_twitter():
    security_list = ["crypto","investing"]
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

def mine_reddit():
    client_id = os.environ.get("REDDIT_CLIENT_ID")
    client_secret = os.environ.get("REDDIT_CLIENT_SECRET")
    user_agent = os.environ.get("REDDIT_USER_AGENT")
    username = os.environ.get("REDDIT_USERNAME")
    password = os.environ.get("REDDIT_PASSWORD")
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        password=password,
        username=username,
        user_agent=user_agent,
    )
   
    subs = os.environ.get('CRYPTO_REDDIT_SUBS').split(",")
    df_posts = pd.DataFrame()

    for sub in subs:
        top_posts = reddit.subreddit(sub).top("week", limit=10)
        for submission in top_posts:
            print("Title of the post :", submission.title)
            submission_comm = reddit.submission(id=submission.id)
            submission_comm.comments.replace_more(limit=0)
            comments = submission.comments.list()
            for comment in comments:
                try:
                    print(comment.body)
                    #if any(query in comment.body.lower() for query in queries):
                    data = {"created_at":  comment.created_utc,
                                "text": comment.body}
                    df_posts = df_posts.append(data, ignore_index=True)

                 # text_blob_sentiment(top_level_comment.body, sub_entries_textblob)
                 # nltk_sentiment(top_level_comment.body, sub_entries_nltk)
                 # replies_of(top_level_comment,
                 #         count_comm,
                 #         sub_entries_textblob,
                 #         sub_entries_nltk)
                except:
                    continue
            time.sleep(5)
    # outFileName="/home/pi/dev/augur/data/sentiments/reddit/" + str(datetime.now()) + ".json"
    # df_posts.to_json(outFileName)
    return df_posts









if __name__ == "__main__":
    count = 3
    for i in range(count):
        tweets_mined_list = mine_twitter()
        print(tweets_mined_list)
    # mined_posts = mine_reddit()
    # for post in mined_posts:
    #     print(post)
    # uniqueList = []
    # for entry in match:
    #     if entry not in uniqueList:
    #         uniqueList.append(entry)
    # print(len(uniqueList),uniqueList)