import hashlib

def create_check_sum():
    secret_key = "super_secret_key"
    h = hashlib.new('sha1')
    h.update(b"super_secret_key")
    return print(h.hexdigest())

"""
Пример строчки из которой необходимо выбить check_sum см.ниже

createname=Test+Meeting&meetingID=abc123&attendeePW=111222&moderatorPW=333444639259d4-9dd8-4b25-bf01-95f9567eaf4b
"""
create_check_sum()
create_check_sum()
create_check_sum()