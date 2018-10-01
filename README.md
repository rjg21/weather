# Simple wrapper for OpenWeatherMap API

### Usage:

```
docker run --rm -e OPENWEATHERMAP_KEY=<key> rjg21/weather [--country=<country>] <city>

  <key>      Your OpenWeatherMap API Key
  <city>     Location to be passed to API (e.g. london, "new york", etc)
  <country>  Optionally, restrict cities to an ISO 3166 country code
```

### Obtaining OpenWeatherMap API Key

1. Goto: https://openweathermap.org and create a free account
2. Sign-in with your new account
3. On the My Home page, select the API Keys tab
4. Copy the default key pre-created for you (32 hex digits)
 
*Note: it can take up to 10 minutes for this key to become active*
