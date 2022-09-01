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


parse_name("user6")
