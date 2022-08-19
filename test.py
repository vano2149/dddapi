"""
teste.py file!
"""

from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring
from json import dumps
import requests
response = requests.get('https://bbb.epublish.ru/bigbluebutton/api')

response1 = response._content.decode()

json1 = dumps(bf.data(fromstring(response1)))

print(json1)

