import json
import requests
from config import k


class APIException(Exception):
    pass


class perevod:
    @staticmethod
    def get_price(fsym, tsyms, a):
        try:
            fs = k[fsym]
        except KeyError:
            raise APIException(f"валюты {fsym} нет")

        try:
            ts = k[tsyms]
        except KeyError:
            raise APIException(f"валюты {tsyms} нет!")

        if fs == ts:
            raise APIException(f'одинаковые валюты {fsym}!')



        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={fs}&tsyms={ts}")
        resp = json.loads(r.content)
        new_p = resp[ts] * float(a)
        new_p = round(new_p, 3)
        message = f"цена {a} {fsym} в {tsyms} : {new_p}"
        return message