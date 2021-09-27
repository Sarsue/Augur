from flask import Flask,request

app = Flask(__name__)


# Get rest documented with swagger

@app.route('/', methods=['GET'])
def home():
    return "<h1>Augur Api</h1><p>This site is a prototype API for augur a MVP investment tool. </p>"


@app.route('/api/v1/sentiments', methods=['GET', 'POST'])
def sentiments():
    if request.method == "GET":
        result = sentiments_processor.get_sentiments()
        return {
            'message': result,
            'method': request.method
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
    app.run(debug=True, port=5000, host='0.0.0.0')
