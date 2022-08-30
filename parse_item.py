"""
"""

name = {
    "firstName": "Alice",
    "lastName": "Yandex Station"
}

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

print(next(filter(lambda x : x == name, data_base.values()), None))