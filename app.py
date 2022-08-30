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

from utils.create_basic_url import Url_Builder



app = Flask(__name__)
api = Api(app)


data_base = {
        "user1":{
            "firstName" : "John",
            "lastName" : "Dou",
        },
        "user2": {
            "firstName": "Alice",
            "lastName": "Yandex Station",
        },
        "user3": {
            "firstName" : "Ivan",
            "lastName" : "Ivanov"
        },
        "user4": {
            "firstName" :"Bob",
            "lastName" : "Bob",
        },
        "user5": {
            "firstName" : "Kill",
            "lastName" : "Real"
        },
        "user6": {
            "firstName" : "Dangeon",
            "lastName" : "Master"
        },
        "user7": {
            "firstName" : "Van",
            "lastName" : "Darkholm"
        }
    }

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
    "attendeePW":321234,
    "moderatorPW":123321,
}

class Itembbb(Resource):
    def get(self, name):
        """
        Именнованный запрос возвращающий инф. о api.
        name = name 
        passwors = moderatorPW
        """
        username = next(filter(lambda x : x == name, data_base), None)
        if username:
            password = input("Input Password: ")
            url1 = Url_Builder(basic_url, resourse, params, password=password, name=name)
            print(url1.build_url())
            print(url1.build_join_url())
            print(url1.build_end_url())
            data_base[name]["Create_URL"] = url1.build_url()
            data_base[name]["Join_Url"] = url1.build_join_url()
            return data_base[name], 200
        return {'Error' : "User Name is invalid!"}, 404 #requests.get(url).content.decode(encoding="utf-8")
        #return response._content.decode(encoding='utf-8', errors='strict') requests.get(url).content.decode(encoding="utf-8")
    def post(self):
        """
        Post запрос к нашему API -> передача First and second name.
        """
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
