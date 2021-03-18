import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import json
import urllib

API_URL_BASE = 'https://api.coingecko.com/api/v3/'


def get_coin_historical_data(id, vs_currency, days):
    """Get coin's OHLC"""

    api_url = '{0}coins/{1}/ohlc?vs_currency={2}&days={3}'.format(
        API_URL_BASE, id, vs_currency, days)
    return request(api_url)


def get_current_prices(ids):
    # check list for proper entries
    vs_currencies = ['cad', 'usd', 'btc']
    kwargs = {}
    kwargs['ids'] = ids
    kwargs['vs_currencies'] = vs_currencies
    kwargs['include_market_cap'] = 'true'
    kwargs['include_24hr_vol'] = 'true'
    kwargs['include_24hr_change'] = 'true'
    kwargs['include_last_updated_at'] = 'true'

    api_url = '{0}simple/price'.format(
        API_URL_BASE)
    api_url = api_url_params(api_url, kwargs)
    print(api_url)
    return request(api_url)


def get_market_data(vs_currency):
    kwargs = {}
    kwargs['vs_currency'] = vs_currency
    kwargs['order'] = 'market_cap_desc'
    kwargs['per_page'] = 100
    kwargs['sparkline'] = 'false'
    kwargs['price_change_percentage'] = ['1h', '24h', '7d', '30d', '1y']
    api_url = '{0}coins/markets'.format(
        API_URL_BASE)
    api_url = api_url_params(api_url, kwargs)
    print(api_url)


def get_coins(id):


def api_url_params(api_url, params):
    if params:
        api_url += '?'
        for key, value in params.items():
            if isinstance(value, list):
                query_params = urllib.parse.urlencode({key: ','.join(value)})
                api_url += "{0}&".format(query_params)
            else:
                api_url += "{0}={1}&".format(key, value)
        api_url = api_url[:-1]
    return api_url


def request(url):
    # print(url)
    try:
        request_timeout = 120
        session = requests.Session()
        retries = Retry(total=5, backoff_factor=0.5,
                        status_forcelist=[502, 503, 504])
        session.mount('http://', HTTPAdapter(max_retries=retries))
        response = session.get(url, timeout=request_timeout)
        response.raise_for_status()
        content = json.loads(response.content.decode('utf-8'))
        return content
    except Exception as e:
        # check if json (with error message) is returned
        try:
            content = json.loads(response.content.decode('utf-8'))
            raise ValueError(content)
            # if no json
        except json.decoder.JSONDecodeError:
            pass
            # except UnboundLocalError as e:
            #    pass
        raise


def save_data(path):
    with open(path, 'w') as outfile:
        json.dump(data, outfile)


if __name__ == '__main__':
    # function sample call
    # coin_data = get_coin_historical_data("bitcoin", "cad", 30)
    # price_data = get_current_prices(['bitcoin', 'ethereum', 'cardano'])
    get_market_data('cad')
