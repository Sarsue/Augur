from flask import Flask,request,Response
from sources.twitter_client import mine_twitter
from common.storage_manager import save_data
import time
from flask_apscheduler import APScheduler
import json

app = Flask(__name__)
scheduler = APScheduler()


def mining_tasks():
    """ Function for test purposes. """
    mined_sentiments = mine_twitter()
    if (len(mined_sentiments) > 0):
            print("saving it next mined sentiments",mined_sentiments)
            #insert_sentiments(mined_sentiments)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Augur Api</h1><p>This site is a prototype API for augur a MVP investment tool. </p>"


@app.route('/api/v1/recommendations', methods=['GET', 'POST'])
def recommendations():
    if request.method == "GET":
        # tweets = load_tweets()
        # length = len(tweets)
        # max = 50  
        
        # if(length > 0):
        #     result =[]
        #     for tweetdf in tweets:
        #         count = 0
        #         for row in tweetdf.itertuples():
        #             result.append({"text":row.text, "creationstamp":row.creationstamp, "sentimentlabel":row.sentimentlabel})
        #             if (count >= max):
        #                 break
        #             else:
        #                 count = count + 1
        #     return Response(json.dumps(result), mimetype='application/json')

        # else:
        result = {"security": "Bitcoin"}
        return {
                'message': result,
                # 'method': request.method
            }
    if request.method == "POST":
        # add topic/category to mine ftwitter an reddit for 
        return {
            'message': 'This endpoint should create an entity',
            'method': request.method,
		    'body': request.json
        }

@app.route('/api/v1/sentiments/<string:query>', methods=['GET', 'PUT', 'DELETE'])
def sentiment(ticker_id):
     if request.method == "GET":
        return {
            'id': ticker_id,
            'message': 'This endpoint should return the entity {} details'.format(ticker_id),
            'method': request.method
        }
     if request.method == "PUT":
        return {
            'id': ticker_id,
            'message': 'This endpoint should update the entity {}'.format(ticker_id),
            'method': request.method,
		'body': request.json
        }
     if request.method == "DELETE":
        return {
            'id': ticker_id,
            'message': 'This endpoint should delete the entity {}'.format(ticker_id),
            'method': request.method
        }







if __name__ == '__main__':
    scheduler.add_job(id = 'Scheduled Task', func=mining_tasks, trigger="interval", seconds=30)
    scheduler.start()
    app.run(debug=True, port=5000, host='0.0.0.0')