"""
Module with methods create check_sum
and build first url
"""

from hashlib import sha1
import urllib.parse
from uuid import uuid4
import os
import requests
import xmltodict



class UrlBuilder:
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
    def __init__(self,
        basic_url:str,
        resourse:dict,
        params:dict,
        username:str,
        logout_url:str,)-> str:
        self.basic_url = basic_url
        self.resourse = resourse
        self.params = params
        self.checksum = None
        #self.params = params['role']
        self.params['welcome'] = "Стандартное приведствие!"
        self.params['bannerText'] = 'Тест BannerText'
        self.meeting_id = str(uuid4())
        self.moderator_pw = str(uuid4())
        self.password = self.moderator_pw
        self.fullname = username
        self.logout_url = logout_url
        
        super(UrlBuilder, self).__init__()


class Build_Url_Create(UrlBuilder):
    """
    Функция создания url
    парамерты:
        basic_url -> бызовый url
        params -> параметры запроса.
        resourse -> ресурсы нашего запроса.
    """

    def create_url(self):
        """
        Полноценный create полноценной комнаты:
        """
        url = self.basic_url
        self.params["logoutURL"] = self.logout_url
        self.params["meetingID"] = self.meeting_id
        self.params["password"] = self.password
        self.params["moderatorPW"] = self.moderator_pw
        self.params['allowStartStopRecording'] = 'true'
        self.params['preUploadedPresentationOverrideDefault'] = False
        self.params['disabledFeatures'] = 'breakoutRooms, downloadPresentationWithAnnotations'
        for item in self.resourse:
            if item == "create":
                parametrs = urllib.parse.urlencode(self.params)
                url = "{}{}".format(url, item)
                self.checksum = sha1(bytes(
                item + parametrs + os.environ.get("SECRET_KEY"),
                encoding="utf-8")).hexdigest()
        if self.params:
            url='{}?{}&checksum={}'.format(url, parametrs, self.checksum)
            return url
        if requests.get(url).status_code == 200:
            reg = requests.get(url).content
            parsed_url = xmltodict.parse(reg)
            return parsed_url
        else:
            None

class Build_Join_Url(UrlBuilder):
    """
    Класс преобразования Join -> Запроса\n
    Параметры:\n
        fullname -> пока равна meetingID позже переделать\n
        password -> Равен moderatorPW.\n
    """

    def join_url(self):
        """
        Спросить про проверку 
        """
        url = self.basic_url
        parametrs = urllib.parse.urlencode(self.params)
        for item in self.resourse:
            if item == "join":
                self.params = {k : v for k, v in self.params.items() if k != "logoutURL"}
                self.params["fullName"] = self.fullname
                parametrs = urllib.parse.urlencode(self.params)
                url = "{}{}".format(url, item)
                self.checksum = sha1(bytes(
                item + parametrs + os.environ.get("SECRET_KEY"),
                encoding="utf-8")).hexdigest()
        if self.params:
            url = "{}?{}&checksum={}".format(url, parametrs, self.checksum)
        return url

    def join_url_role_viewer(self):
        '''
        Сознание ссылки на
        подключение с ролью viewer.
        Спросить про проверку.
        '''
        url = self.basic_url
        for item in self.resourse:
            if item == "join":
                for param in self.params:
                    if param != "role":
                        self.params = {k : v for k, v in self.params.items() if k != "moderatorPW"}
                        self.params = {k : v for k, v in self.params.items() if k != "password"}
                        self.params["role"] = "VIEWER"
                parametrs = urllib.parse.urlencode(self.params)
                url = "{}{}".format(url,item)
                self.checksum = sha1(bytes(item + parametrs + os.environ.get("SECRET_KEY"), encoding="utf-8")).hexdigest()
        if self.params:
            url = "{}?{}&checksum={}".format(url, parametrs, self.checksum)
        return url


class Build_End_Url(UrlBuilder):
    """
    Создание ссылки на
    завершение конференции.
    """
    def end_url(self):
        for item in self.resourse:
            if item == "end":
                end = {}
                for k, v in self.params.items():
                    if k == "meetingID":
                        end[k] = v
                    elif k == 'password':
                        end[k] = v
                url = self.basic_url
                parametrs = urllib.parse.urlencode(end)
                url = '{}{}'.format(url, item)
                self.checksum = sha1(bytes(
                item + parametrs + os.environ.get("SECRET_KEY"),
                encoding="utf-8")).hexdigest()
        if self.params:
            url = "{}?{}&checksum={}".format(url, parametrs, self.checksum)
        return url


    def insertDocumentation(self):
        """
        Функция передачи
        документов на трансляцию.
        Написать проверку перед удалением!
        """


class Monitoring(UrlBuilder):
    """
    Дочерний класс Мониторинга
    """
    def isMeetingRunning(self):
        """
        Показывает состоялась ли конфиренция
        позже перенести в другой класс "Monitoring" который будет
        наследоваться от Url_Builder.


        Написать проверку перед удалением!

        """
        url = self.basic_url
        for item in self.resourse:
            if item == "isMeetingRunning":
                url = "{}{}".format(url,item)
                ismeetingrunningparams = {}
                for k, v in self.params.items():
                    if k == "meetingID":
                        ismeetingrunningparams[k] = v
                parametrs = urllib.parse.urlencode(ismeetingrunningparams)
                self.checksum = sha1(bytes(
                item + parametrs + os.environ.get("SECRET_KEY"),
                encoding="utf-8")).hexdigest()
        if self.params:
            url = "{}?{}&checksum={}".format(url, parametrs, self.checksum)
        return url
        

    def getMeetings(self):
        """
        Возвращает все текущии конфиренции!!
        """
        url = self.basic_url
        for item in self.resourse:
            if item == "getMeetings":
                print(item)
                self.checksum = sha1(bytes(
                                    item + os.environ.get("SECRET_KEY"),
                                    encoding="utf-8")).hexdigest()
        if self.params:
            url = "{}{}?checksum={}".format(url,item, self.checksum)
            print("Тестим вот эту функцию!", url)
        resp = requests.get(url)
        if resp.status_code == 200:
            reg = requests.get(url).content
            parsed_url = xmltodict.parse(reg)
            return parsed_url
        else:
            return None


class Recordings(UrlBuilder):
    """
    Класс определяющий функции
    записи конференции!
    НЕРАБОТАЕТ !!!
    """
    def getrecordings(self):
        ''''''
        url = self.basic_url
        for item in self.resourse:
            if item == "getRecordings":
                url = '{}{}'.format(url,item)
                self.params['recordID'] = self.params['meetingID']
                print(self.params)
                self.params = {k : v for k, v in self.params.items() if k != "moderatorPW"}
                self.params = {k : v for k, v in self.params.items() if k != "password"}
                self.params = {k : v for k, v in self.params.items() if k != "logoutURL"}
                self.params = {k : v for k, v in self.params.items() if k != "name"}
                self.params = {k : v for k, v in self.params.items() if k != "attendeePW"}
                self.params = {k : v for k, v in self.params.items() if k != "allowStartStopRecording"}
                print(self.params)
                self.checksum = sha1(bytes(item + os.environ.get('SECRET_KEY'),encoding='utf-8')).hexdigest()
                parametrs = urllib.parse.urlencode(self.params)
        if self.params:
            url = "{}?{}&checksum={}".format(url, parametrs, self.checksum)
            return url
        return None


Base_URL = "https://bbb.epublish.ru/bigbluebutton/api/"

resourse = {
    "create" : "create",
    "join" : "join",
    "end" : "end",
    "isMeetingRunning":"isMeetingRunning",
    "getMeetings": "getMeetings",   
}


params = {
    "name": "Yeplfhjdf",
    "attendeePW":1234567,
}

if __name__ == "__main__":
    """
    Тестим здесь !!!
    """

    print('Ссылка на создание конф.')
    a = Build_Url_Create(Base_URL, resourse, params, username="user6", logout_url = "https://google.com")
    print(a.create_url())
    print("-" * 30)
    print('Ссылка на подключение к конф.')
    b = Build_Join_Url(Base_URL, resourse, params, username="user6", logout_url = "https://google.com")
    print(b.join_url())
    print("Cсылка на подключение к конф. с ролью viewer!")
    print(b.join_url_role_viewer())
    print("-" * 30)
    print("Сссылка на завершения конфж.")
    c = Build_End_Url(Base_URL, resourse, params, username="user6", logout_url = "https://google.com")
    print(c.end_url())
    print("Ссылка на проверку на запуск опредененного совещания")
    d = Monitoring(Base_URL, resourse, params, username="user6", logout_url = "https://google.com")
    print("-" * 30)
    print(d.isMeetingRunning())
    print(d.getMeetings())
    #print(b.getDefaultXMLConf())
    '''c = Recordings(Base_URL, resourse, params, username="user6", logout_url = "https://google.com")
    print("-" * 30)
    print(c.getrecordings())'''