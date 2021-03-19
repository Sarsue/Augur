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
        api = TwitterAPI(
            consumer_key,
            consumer_secret,
            access_token_key,
            access_token_secret,
            api_version="1",
        )
        r = api.request(
            "tweets/search/recent",
            {
                "query": search_term,
                "tweet.fields": "author_id",
                "expansions": "author_id",
            },
        )

        for item in r:
            print(item)

        print("\nINCLUDES")
        print(r.json()["includes"])

        print("\nQUOTA")
        print(r.get_quota())

    except TwitterRequestError as e:
        print(e.status_code)
        for msg in iter(e):
            print(msg)

    except TwitterConnectionError as e:
        print(e.status_code)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    # function sample call
    # coin_data = get_coin_historical_data("bitcoin", "cad", 30)
    # price_data = get_current_prices(['bitcoin', 'ethereum', 'cardano'])
    search_for_tweets("bitcoin")
