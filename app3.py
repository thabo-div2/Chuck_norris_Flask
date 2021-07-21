from flask import Flask
import requests


app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_norris_joke_v2():

    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()

    return response['value']


if __name__ == "__main__":
    app.run(debug=True)

