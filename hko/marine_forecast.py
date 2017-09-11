"""A module to retrieve marine forecast data from Hong Kong Observatory"""

import json

import requests


BASE_URL = 'http://pda.weather.gov.hk/'
URL_UC = 'locspc/android_data/fmar_uc.xml'
URL_EN = 'locspc/android_data/fmar.xml'


def marine_forecast(lang='UC'):

    """A function to retrieve marine forecast data from Hong Kong Observatory"""

    response = {}
    if lang in ['UC', 'EN']:
        try:
            if lang == 'UC':
                data = json.loads(requests.get(BASE_URL + URL_UC).content)
            if lang == 'EN':
                data = json.loads(requests.get(BASE_URL + URL_EN).content)
            response['result'] = data
            response['status'] = 1
        except IndexError:
            response['result'] = ''
            response['status'] = 2
    else:
        response['result'] = ''
        response['status'] = 0
    return response
