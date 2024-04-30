from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/get_public_json', methods=['GET'])
def get_public_json():
    try:
        # URL of the public JSON API
        url = "https://jsonplaceholder.typicode.com/posts"

        # Make a GET request to the API
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Return the JSON data received from the API
            return jsonify(response.json())
        else:
            # Return an error message if the request was not successful
            return jsonify({"error": "Failed to fetch data from the API"}), 500
    except Exception as e:
        # Return an error message if an exception occurs
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
