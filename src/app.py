import sched
import time
from DataAcquisition.reddit_client import get_reddit_watchlist

import utility


def reddit_sentiments():
    """Returns a list of securities based on some criterias scraped from many sources """
    subs = utility.get_config(key)
   

def coingecko_prices():
    """return Sentiment, Technical and Fundamental analysis for a security on a scale of 1-10"""
    return {"data": {"sentiments": 6, "technical": 7, "fundamental": 5}}


def google_twitter_trends():
    """returns crypto's with increased mentions on social media"""






def main():
    # initialize source provider manager  here pass it confg
    while True:
        get_wishlist("CRYPTO")
        time.sleep(15)
    #     send notification


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
