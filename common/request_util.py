import requests

class RequestUtils:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.session = requests.session()
        return cls._instance

    def request_api(self, **kwargs):
        res = self.session.request(**kwargs)
        return res
