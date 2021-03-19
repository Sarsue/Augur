import pandas as pd
from prawcore.exceptions import ResponseException
from requests import HTTPError
from psaw import PushshiftAPI
import praw
import os
from dotenv import load_dotenv
load_dotenv()


def get_reddit_watchlist(subs):
    client_id = os.environ.get('REDDIT_CLIENT_ID')
    client_secret = os.environ.get('REDDIT_CLIENT_SECRET')
    user_agent = os.environ.get('REDDIT_USER_AGENT')
    username = os.environ.get('REDDIT_USERNAME')
    password = os.environ.get('REDDIT_PASSWORD')
    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, password=password,
                         username=username, user_agent=user_agent)

    for sub in subs:
        subreddit = reddit.subreddit(sub)
        topics_dict = {"title": [],
                       "score": [],
                       "id": [], "url": [],
                       "comms_num": [],
                       "created": [],
                       "body": []}
        for submission in subreddit.top(limit=50):
            topics_dict["title"].append(submission.title)
            topics_dict["score"].append(submission.score)
            topics_dict["id"].append(submission.id)
            topics_dict["url"].append(submission.url)
            topics_dict["comms_num"].append(submission.num_comments)
            topics_dict["created"].append(submission.created)
            topics_dict["body"].append(submission.selftext)
        topics_data = pd.DataFrame(topics_dict)
        print(topics_data)


if __name__ == "__main__":
    # function sample call
    subs = [
        "pennystocks",
        "RobinHoodPennyStocks",
        "Daytrading",
        "StockMarket",
        "stocks",
        "investing",
        "wallstreetbets",
        "cryptocurrency",
        "cardano",
        "binance",
        "ethereum",
        "fatfire"
    ]
    get_reddit_watchlist(subs)
