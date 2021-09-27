from sys import implementation
from typing import Dict

def get_sentiments() -> Dict:
    result = {}
    tweets = ['Sell Everything', 'Hold', 'Buy More Good Companies']
    keys = ['tweet','sentiment_score']
    # load tweets from storage, db, blob store
    for i in enumerate(len(tweets)):
        result[keys[0]] = tweets[i]
        result[keys[1]] = i
    return result



