import pandas as pd
from prawcore.exceptions import ResponseException
from requests import HTTPError
from psaw import PushshiftAPI
import praw
import os
from dotenv import load_dotenv
from pandas.core.frame import DataFrame
import time
from typing import List

load_dotenv()
alias_config = {
    "BTC": "bitcoin",
    "ETH": "ethereum",
    "ADA": "cardano",
    "XMR": "monero",
    "LINK": "chainlink"
}


def mine_reddit(security: str) -> DataFrame:
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
    queries = []
    specific_sub = alias_config[security.upper()]
    queries.append(security)
    queries.append(specific_sub)
    subs = os.environ.get('CRYPTO_REDDIT_SUBS').split(",")
    subs.append(specific_sub)
    print(subs, queries)
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
                    if any(query in comment.body.lower() for query in queries):
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
    return df_posts

def mine_reddit_list(crypto_list):
    for crypto in crypto_list:
        posts = mine_reddit(crypto)
        outFileName="/home/pi/dev/augur/data/sentiments/reddit/" + crypto + ".json"
        posts.to_json(outFileName)

if __name__ == "__main__":
    crypto_list = ['btc','eth']
    mine_reddit_list(crypto_list)
