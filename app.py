"""
Implementation of
connection to bbbapi.
https://habr.com/ru/post/193242/
"""

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import requests
import os
from urllib.request import Request, urlopen
from uuid import uuid4
from utils.create_basic_url import Url_Builder



app = Flask(__name__)
api = Api(app)

app.secret_key = os.environ.get("SECRET_KEY")

basic_url = "https://bbb.epublish.ru/bigbluebutton/api/"

resourse = {
    "create" : "create",
    "join" : "join",
    "end" : "end",
    "secret_key": "secret_key",
}

params = {
    "name": "Ghbdtnjktu",
    "meetingID": str(uuid4()),
    "attendeePW":321234,
    "moderatorPW":123321,
}


class Itembbb(Resource):
    def get(self, name, basic_url, resourse, params):
        """
        Именнованный запрос возвращающий инф. о api.
        """
        print(basic_url, resourse, params)
        url = Url_Builder.build_url(basic_url, resourse, params)
        print(url)
        return {"Проверка": name} #requests.get(url).content.decode(encoding="utf-8")
        #return response._content.decode(encoding='utf-8', errors='strict') requests.get(url).content.decode(encoding="utf-8")
    def post(self):
        if requests.method == 'POST':
            url = Url_Builder.build_join_url(basic_url, resourse, params)
        pass
    def put(self):
        pass # response.decode().split('\r\n'):
    def delete(self):
        pass

class ItembbbColection(Resource):
    def get(self):
        a = Url_Builder(basic_url, resourse, params)
        return print(a.build_url.__str__())

api.add_resource(Itembbb, '/item/<string:name>')
api.add_resource(ItembbbColection, '/items/')

if __name__ == "__main__":
    app.run(port=8080, debug=True)
