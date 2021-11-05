#https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask

from flask import Flask, render_template, jsonify
from bingimagescraper import image_scraper



app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')


@app.route("/<query>", methods=['GET'])
def get_image(query):
    data = jsonify(image_scraper(query))
    return data



if __name__ == '__main__':
    # change to your own port
    app.run(host='0.0.0.0', port=2434, debug=True)

