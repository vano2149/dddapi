"""
"""

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
import itertools
def parse_name(name):
    if name == "user6":
        user = [value for value in data_base.get(name).values()]
    return print(" ".join(user))

params = {'name': 'Yeplfhjdf', 'attendeePW': 1234567, 'logoutURL': 'https://google.com', 'meetingID': '7f9aa62e-2f4f-4b43-b0fd-9b3432adde2a', 'password': '21487c27-6a44-4580-a4d0-2c1aaf1a18a1', 'moderatorPW': '21487c27-6a44-4580-a4d0-2c1aaf1a18a1'}

params = {k : v for k, v in params.items() if k != "logoutURL"}


print(params)