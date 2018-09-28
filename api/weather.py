# test main.py
import os
import sys
import requests

# display usage
def usage():
    print('''
Fetch weather information

Usage:
    weather <location>

An OpenWeatherMap API key MUST be provided via the OPENWEATHERMAP_KEY environment variable.
''')

# environment key containing OpenWeatherMap Key
envkey = 'OPENWEATHERMAP_KEY'

# check if key set in environment
if envkey not in os.environ:
    print('Error: missing', envkey, 'environment variable')
    usage()
    exit(1)

# get key
apikey = os.environ[envkey]

# check enough arguments
if len(sys.argv) < 2:
    print('Error: missing location argument')
    usage()
    exit(2)

# get location argument
location = sys.argv[1]

try:
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?APPID=' + apikey + '&units=metric&q=' + location)
    r.raise_for_status()
except:
    print('Error: failed to get response from openweathermap for', location, '['+str(r.status_code)+']')
    exit(r.status_code)

data = r.json()

print(u'Temperature for {0}, {1}: {2}\u2103'.format(data['name'], data['sys']['country'], data['main']['temp']))
