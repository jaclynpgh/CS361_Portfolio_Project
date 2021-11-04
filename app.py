#https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
import json
from flask import Flask, render_template

from bingimagescraper import image_scraper

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')


@app.route("/<query>", methods=['GET'])
def get_image(query):
    return json.dumps(image_scraper(query))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2434, debug=True)
