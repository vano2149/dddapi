"""
Module with methods create check_sum 
and build first url 
"""
from hashlib import sha1
import urllib.parse
from uuid import uuid4
import os


def build_url(basic_url, params):
    """
    Функция создания url
    парамерты:
        basic_url -> бызовый url
        params -> параметры запроса.
        url_parts -> список разделенного url-a 
        из третьего элемента списка будем гинерить sha1() сумму.
    """
    # преобразуем 
    url_parts = list(urllib.parse.urlsplit(basic_url))
    url_parts[3] = urllib.parse.urlencode(params)
    print(url_parts[3] + os.environ.get("SECRET_KEY"))
    __check_sum = sha1(bytes(url_parts[3] + os.environ.get("SECRET_KEY"), encoding="utf-8")).hexdigest()
    return print(urllib.parse.urlunsplit(url_parts) + "&checksum=" + __check_sum)

basic_url = "https://bbb.epublish.ru/bigbluebutton/api/"

params = {
    "create" : "",
    "allowStartStopRecording": "false",
    "autoStartRecording": "false",
    "meetingID" : str(uuid4()),
    "name" : "cock1",
    "record": "false",
}


build_url(basic_url, params)
