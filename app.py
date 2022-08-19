"""
Implementation of
connection to bbbapi.
https://habr.com/ru/post/193242/
"""

from hashlib import sha1
from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring
from json import JSONEncoder, dumps
import uuid

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import requests
import os
from urllib.request import Request, urlopen

app = Flask(__name__)
api = Api(app)

app.secret_key = os.environ.get("SECRET_KEY")

# Позже удалить строчку ниже!
Base_URL = "https://bbb.epublish.ru/bigbluebutton/api/"

class Itembbb(Resource):
    def get(self, name):
        """
        Именнованный запрос возвращающий инф. о api.
            attr
                name -> Имя собрания
                checksum -> Генерирует хеш на основе secret_key.
                meetingID -> Уникальный индентификатор собрания! 
        """
        checksum = sha1(bytes(app.secret_key, encoding="utf8")).hexdigest()
        meetingID = str(uuid.uuid4())
        print(meetingID)
        url = Base_URL + "?create/name=" + name + '&meetingID=' + meetingID + '&checksum=' + checksum
        print(url)
        return requests.get(url).content.decode(encoding="utf-8")
        #return response._content.decode(encoding='utf-8', errors='strict') requests.get(url).content.decode(encoding="utf-8")
    def post(self):
        if requests.method == 'POST':
            print("plfhjdf")
    def put(self):
        pass # response.decode().split('\r\n'):
    def delete(self):
        pass

class ItembbbColection(Resource):
    def __init__(self,*args, **kwargs):

        self.name = kwargs[""]
        self.checksum = args
        self.meetingID = kwargs[""]

    def get(self):
        self.checksum = sha1(bytes(app.secret_key, encoding='utf-8')).hexdigest()
        print(self.checksum)
        #print(type(response.content.decode(encoding='utf-8')))
        return print(self.checksum)

api.add_resource(Itembbb, '/item/<string:name>')
api.add_resource(ItembbbColection, '/items/')

if __name__ == "__main__":
    app.run(port=8080, debug=True)
