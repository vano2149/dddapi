"""
Module with methods create check_sum 
and build first url 
"""

from base64 import encode
from hashlib import sha1
import urllib.parse
from uuid import uuid4
import os


class Url_Builder:
    """
    Класс создающий URL-ы -> (create, join, end)
    """
    def __init__(self, basic_url:str, resourse:dict, params:dict)-> str:
        """
        Конструктор переменных
        """
        self.basic_url = basic_url
        self.resourse = resourse
        self.params = params
        self.check_sum = None
        self.meetingID = str(uuid4())


    def build_url(self) -> str:
        """
        Функция создания url
        парамерты:
            basic_url -> бызовый url
            params -> параметры запроса.
            resourse -> ресурсы нашего запроса.
        """
        url = self.basic_url
        self.params["meetingID"] = self.meetingID

        for item in self.resourse:
            if item == "create":
                parametrs = urllib.parse.urlencode(self.params)
                url = "{}{}".format(url, item)
                self.checksum = sha1(bytes(item + parametrs + os.environ.get("SECRET_KEY"), encoding="utf-8")).hexdigest()

        if self.params:
            url='{}?{}&checksum={}'.format(url, parametrs, self.checksum)
        return url

    def build_join_url(self):
        """
        Функция преобразования Join -> Запроса
        Параметры:
            fullname -> пока равна meetingID позже переделать
            password -> равен attendeePW
        """

        url = self.basic_url
        parametrs = urllib.parse.urlencode(self.params)
        for item in self.resourse:
            if item == "join":
                self.params["fullName"] = self.params["meetingID"]
                self.params["password"] = self.params["attendeePW"]
                parametrs = urllib.parse.urlencode(self.params)
                url = "{}{}".format(url, item)
                self.checksum = sha1(bytes(item + parametrs + os.environ.get("SECRET_KEY"), encoding="utf-8")).hexdigest()
        if self.params:
            url = "{}?{}&checksum={}".format(url, parametrs, self.checksum)
        return url


    def build_end_url(self):
        """
        Создание ссылки на
        завершение конференции.
        Добавить в наш create &meta_endCallbackUrl=https%3A%2F%2Fmyapp.example.com%2Fcallback%3FmeetingID%3Dtest01
        """
        #url = Url_Builder.build_url(self.basic_url, self.resourse, self.params)
        #print(url)
        for item in self.resourse:
            if item == "end":
                for param in self.params.items():
                    print(param)
        return None


Base_URL = "https://bbb.epublish.ru/bigbluebutton/api/"

resourse = {
    "create" : "create",
    "join" : "join",
    "end" : "end",
    "secret_key": "secret_key",
}

params = {
    "name": "Yeplfhjdf",
    "attendeePW":1234567,
    "moderatorPW":7654321,
}

if __name__ == "__main__":
    a = Url_Builder(Base_URL, resourse, params)
    print('Ссылка на создание конф.')
    print(a.build_url())
    print('Ссылка на подключение к конф.')
    print(a.build_join_url())
    print(a.build_end_url())

