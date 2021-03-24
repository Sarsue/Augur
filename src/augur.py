import sched
import time
from DataAcquisition.reddit_client import get_reddit_watchlist

import utility


def get_wishlist(key):
    """Returns a list of securities based on some criterias scraped from many sources """
    subs = utility.get_config(key)
    get_reddit_watchlist(subs)


def get_analysis(security):
    """return Sentiment, Technical and Fundamental analysis for a security on a scale of 1-10"""
    return {"data": {"sentiments": 6, "technical": 7, "fundamental": 5}}


def register_for_notifications(email):
    """registers an email and or phone number for notifications"""


def main():
    get_wishlist("CRYPTO")
    # while True:
    #     get wishlist
    #     get sentiment and ta analysis (price and volume dip on solid projjects)
    #     send notification


if __name__ == "__main__":
    main()
