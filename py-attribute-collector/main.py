from flask import Flask, request
from flask.views import MethodView
from flask_cors import CORS

from collector import Collector

app = Flask(__name__)
CORS(app)


class CollectorAPI(MethodView):
    def get(self):
        return "OK"

    def post(self):
        image_bytes = request.data
        collector = Collector(image_bytes)
        attribute_json = collector.collect()
        return attribute_json


app.add_url_rule("/api/collector/", view_func=CollectorAPI.as_view("collector"))

if __name__ == "__main__":
    app.run(host="0.0.0.0")
