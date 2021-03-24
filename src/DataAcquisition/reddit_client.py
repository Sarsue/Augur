from prawcore.exceptions import ResponseException
from requests import HTTPError
from psaw import PushshiftAPI
import praw
import os
from dotenv import load_dotenv

load_dotenv()
import pandas as pd


def get_reddit_watchlist(subs):
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

    for sub in subs:
        top_posts = reddit.subreddit(sub).top("week", limit=5)
        for submission in top_posts:
            print("Title of the post :", submission.title)
            submission_comm = reddit.submission(id=submission.id)
            for count, top_level_comment in enumerate(submission_comm.comments):
                print(f"-------------{count} top level comment start--------------")
                count_comm = 0
                try:
                    print(top_level_comment.body)
                    # text_blob_sentiment(top_level_comment.body, sub_entries_textblob)
                    # nltk_sentiment(top_level_comment.body, sub_entries_nltk)
                    # replies_of(top_level_comment,
                    #         count_comm,
                    #         sub_entries_textblob,
                    #         sub_entries_nltk)
                except:
                    continue


if __name__ == "__main__":
    print("ok")
    # function sample call
    # get_reddit_watchlist(subs)
