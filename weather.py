import argparse
import json
import requests

KEY = 'e68b4f9fad0d3fd21e7a91c950c75b3c'
URL = 'http://api.openweathermap.org/data/2.5/weather'
DEFAULT_ZIP = '68127,us'
DEFAULT_UNITS = 'metric'


parser = argparse.ArgumentParser()
parser.add_argument("-z", type=int, help="sets zip-code for weather")
args = parser.parse_args()
if args.z:
    zip_code = args.z
else:
    zip_code = DEFAULT_ZIP


def make_request(url, params):
    r = requests.get(url, params=params)
    print('Ask for weather...')
    if r.status_code == 200:
        print('Success...')
        result = json.loads(r.content)
        print('Description: ' + result.get('weather')[0].get('description'))
        print('\033[94m\033[4mTemperature: ' + str(result.get('main').get('temp')) + '\033[0m')
        print('Wind: ' + str(result.get('wind').get('speed')) + ' meters/sec')
    else:
        print('Something went wrong')


params = {
    'zip': zip_code,
    'APPID': KEY,
    'units': DEFAULT_UNITS
}

if __name__ == '__main__':
    make_request(URL, params)
