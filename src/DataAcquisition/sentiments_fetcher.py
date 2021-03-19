import os
from dotenv import load_dotenv
from TwitterAPI import (
    TwitterAPI,
    TwitterOAuth,
    TwitterRequestError,
    TwitterConnectionError,
)

load_dotenv()


def search_for_tweets(search_term):
    try:
        consumer_key = os.environ.get("TWITTER_API_KEY")
        consumer_secret = os.environ.get("TWITTER_API_SECRET")
        access_token_key = os.environ.get("TWITTER_ACCESS_TOKEN")
        access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
        auth_type = "oAuth2"

        api = TwitterAPI(consumer_key, consumer_secret, auth_type)
        r = api.request(
            "tweets/search/recent",
            {
                "query": search_term,
                "tweet.fields": "author_id",
                "expansions": "author_id",
            },
        )

        print(r.status_code)
    except Exception as err:
        print(err)


if __name__ == "__main__":
    # function sample call
    # coin_data = get_coin_historical_data("bitcoin", "cad", 30)
    # price_data = get_current_prices(['bitcoin', 'ethereum', 'cardano'])
    search_for_tweets("bitcoin")
