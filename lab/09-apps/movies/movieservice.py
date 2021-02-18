from flask import Flask, request, jsonify
from model.model import Sentiment

# -----------------------------------------------------------------------------
# Simple flask sample with a IMDb best movies sentiment analysis.
# - The trained model predicts a sentiment rating from your movie comment.
# - The prediction value is between 0 (very poor) and 1 (very good) movie.
#
# Further information about teh IMDb best movies data see https://www.imdb.co
# -----------------------------------------------------------------------------

#
# initailize
#
app = Flask(__name__,
            static_url_path='',
            static_folder='static')

sentiment = Sentiment()

#
# request handlers
#
@app.route("/")
def index():
    return app.send_static_file('index.html')


@app.route("/live")
def echo():
    return "Movie service is alive"


@app.route("/test")
def test():
    comment = "The movie was awesome"
    rating = sentiment.predict(comment)
    return "Rating: " + str(rating['probability']) + " for the comment:" + comment


@app.route("/predict", methods=['POST'])
def predict():
    content = request.json
    comment = content['comment']
    rating = sentiment.predict(comment)
    response = {"probability": str(rating['probability'])}
    return jsonify(response)
