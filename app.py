import json
from flask import Flask, render_template

from imagescraper import image_scraper

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def home():
    return render_template('index.html')

@app.route("/<site>", methods = ['GET'])
def get_image(site):
    return json.dumps(image_scraper(site))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2434, debug=True)