from pytrends.request import TrendReq
import json

def get_trends():
    result = {}
    pytrend = TrendReq()

    # Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
    pytrend.build_payload(["cryptocurrency","investment", "stock market"])

    
    # Related Queries, returns a dictionary of dataframes
    related_queries_dict = pytrend.related_queries()
    print(related_queries_dict)


    # # Get Google Hot Trends data
    # trending_searches_df = pytrend.trending_searches()
    # print(trending_searches_df.head())
    # save_trend_data(trending_searches_df,"trending")

    # # Get Google Hot Trends data
    # today_searches_df = pytrend.today_searches()
    # print(today_searches_df.head())
    # save_trend_data(today_searches_df,"todaysearch")

    # # Get Google Top Charts
    # top_charts_df = pytrend.top_charts(2018, hl="en-US", tz=300, geo="GLOBAL")
    # print(top_charts_df.head())
    # save_trend_data(top_charts_df,"topcharts")

    # # Get Google Keyword Suggestions
    # suggestions_dict = pytrend.suggestions(keyword="investment")
    # print(suggestions_dict)
    # write_json_to_file(suggestions_dict,"suggestions")

def save_trend_data(trend_data,topic):
    outFileName="/home/pi/dev/augur/data/sentiments/google/" + topic + ".json"
    trend_data.to_json(outFileName)
    
def write_json_to_file(dict,topic):
    jsonString = json.dumps(dict)
    topic = "/home/pi/dev/augur/data/sentiments/google/" + topic + ".json"
    jsonFile = open(topic, "w")
    jsonFile.write(jsonString)
    jsonFile.close()
if __name__ == "__main__":
    get_trends()
    