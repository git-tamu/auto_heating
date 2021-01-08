import requests

URL = "https://notify-api.line.me/api/notify"
ACCESS_TOKEN = '<アクセストークン>'


class LineNotify(object):

    def __init__(self, url=URL, access_token=ACCESS_TOKEN):
        self.__url = url
        self.__access_token = ACCESS_TOKEN
        self.headers = {'Authorization': 'Bearer ' + access_token}

    def send_message(self, message):
        payload = {'message': message}
        requests.post(self.__url, headers=self.headers, data=payload)
