from flask import Flask,request
app = Flask(__name__)
from sources.twitter_client import mine_twitter_topics

@app.route('/')
def index():
    return 'Welcome to Augur Api'


@app.route('/api/v1/sentiments', methods=['GET', 'POST'])
def sentiments():
    if request.method == "GET":
        result = mine_twitter_topics()
        return {
            'message': result,
            'method': request.method
        }
    if request.method == "POST":
        return {
            'message': 'This endpoint should create an entity',
            'method': request.method,
		    'body': request.json
        }

@app.route('/api/v1/sentiments/<string:ticker_id>', methods=['GET', 'PUT', 'DELETE'])
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
    app.run(debug=True, port=5000, host='0.0.0.0')
