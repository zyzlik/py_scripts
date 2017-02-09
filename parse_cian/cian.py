# -*- coding: utf-8 -*-

"""
Parse cian.ru website to find the old ad about Nezhinskaya 14
"""


import requests

url = u'http://www.cian.ru/rent/suburban/'
id_from = 2398455
id_to = 2400000


def parse_cian(url, id_from, id_to):
    while id_from <= id_to:
        req = requests.get(url + str(id_from))
        if req.status_code != 404:
            content = req.text
            if u'Нежинская' in content:
                print id_from
                break
            else:
                print str(id_from) + 'no'
        else:
            continue
        id_from += 1

parse_cian(url, id_from, id_to)
