"""Fetch weather information

Usage:
  weather (-h | --help)
  weather [--country=COUNTRY] <city>

Options:
  -h, --help          Show a brief usage summary.
  --country=COUNTRY Restrict cities to an ISO 3166 country code.

An OpenWeatherMap API key MUST be provided via the OPENWEATHERMAP_KEY environment variable.
"""
import os
import sys
import requests
from docopt import docopt

# environment key containing OpenWeatherMap Key
envkey = 'OPENWEATHERMAP_KEY'

if __name__ == '__main__':
    args = docopt(__doc__)

    # check if key set in environment
    if envkey not in os.environ:
        print('Error: missing', envkey, 'environment variable')
        exit(1)

    # get key
    apikey = os.environ[envkey]

    # get city argument
    city = args['<city>']

    # get country argument
    country = args['--country']
    
    # append country to city (with comma) if set
    if (country is not None) and (country != ''):
        city += ','+country

    try:
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?APPID=' + apikey + '&units=metric&q=' + city)
        r.raise_for_status()
        data = r.json()
    except:
        print('Error: failed to get response from openweathermap for', city, '['+str(r.status_code)+']')
        exit(r.status_code)

    print('Temperature for {0}, {1}: {2:.1f}\u2103'.format(data['name'], data['sys']['country'], data['main']['temp']))
