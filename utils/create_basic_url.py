"""
Module with methods create check_sum 
and build first url 
"""

from hashlib import sha1
import urllib.parse
from uuid import uuid4
import os


class Url_Builder:
    """
    Класс создающий URL-ы -> (create, join, end)\n
    attr:\t
        basic_url -> наш базоавый url для подключения к api.\n
        resourse -> словарь с administration параметрами.\n
        parans -> словарь с  опциональными параметрами.\n
        password -> равен moderatorPW.\n
        name -> равно fullname.\n
    Переназвать класс Administration
    """
    def __init__(self, basic_url:str, resourse:dict, params:dict, username:str)-> str:
        self.basic_url = basic_url
        self.resourse = resourse
        self.params = params
        self.check_sum = None
        self.meetingID = str(uuid4())
        self.moderatorPW = str(uuid4())
        self.password = self.moderatorPW
        self.fullname = username


    def build_url_create(self) -> str:
        """
        Функция создания url
        парамерты:
            basic_url -> бызовый url
            params -> параметры запроса.
            resourse -> ресурсы нашего запроса.
        """
        url = self.basic_url
        self.params["meetingID"] = self.meetingID
        self.params["password"] = self.password
        self.params["moderatorPW"] = self.moderatorPW
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
        Функция преобразования Join -> Запроса\n
        Параметры:\n
            fullname -> пока равна meetingID позже переделать\n
            password -> Равен moderatorPW.\n
        """

        url = self.basic_url
        parametrs = urllib.parse.urlencode(self.params)
        for item in self.resourse:
            if item == "join":
                self.params["fullName"] = self.fullname
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
        """
        for item in self.resourse:
            if item == "end":
                end = dict()
                for k, v in self.params.items():
                    if k == "meetingID":
                        end[k] = v
                    elif k == 'password':
                        end[k] = v
                url = self.basic_url
                parametrs = urllib.parse.urlencode(end)
                url = '{}{}'.format(url, item)
                self.checksum = sha1(bytes(item + parametrs + os.environ.get("SECRET_KEY"), encoding="utf-8")).hexdigest()
        if self.params:
            url = "{}?{}&checksum={}".format(url, parametrs, self.checksum)
        return url

class Monitoring(Url_Builder):
    """
    Дочерний класс Мониторинга 
    """
    def isMeetingRunning(self):
        """
        Показывает состоялась ли конфиренция
        позже перенести в другой класс "Monitoring" который будет 
        наследоваться от Url_Builder.
        """
        url = self.basic_url
        print("Печать парамса в Monitoring",self.params)
        for item in self.resourse:
            if item == "isMeetingRunning":
                url = "{}{}".format(url,item)
                ismeetingrunningparams = dict()
                for k, v in self.params.items():
                    if k == "meetingID":
                        ismeetingrunningparams[k] = v
                parametrs = urllib.parse.urlencode(ismeetingrunningparams)

                self.checksum = sha1(bytes(item + parametrs + os.environ.get("SECRET_KEY"), encoding="utf-8")).hexdigest()
        if self.params:
            url = "{}?{}&checksum={}".format(url, parametrs, self.checksum)
        return url


Base_URL = "https://bbb.epublish.ru/bigbluebutton/api/"

resourse = {
    "create" : "create",
    "join" : "join",
    "end" : "end",
    "isMeetingRunning":"isMeetingRunning",
}

params = {
    "name": "Yeplfhjdf",
    "attendeePW":1234567,
}



if __name__ == "__main__":
    a = Url_Builder(Base_URL, resourse, params, username="user6")
    print('Ссылка на создание конф.')
    print(a.build_url_create())
    print('Ссылка на подключение к конф.')
    print(a.build_join_url())
    print("Сссылка на завершения конфж.")
    print(a.build_end_url())
    print("Ссылка на проверку на запуск опредененного совещания")
    b = Monitoring(Base_URL, resourse, params, username="user6")
    print(b.isMeetingRunning())
