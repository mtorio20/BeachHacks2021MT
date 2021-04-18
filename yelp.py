import requests 
import json

with open('api.txt', 'r') as f:
    SECRET_API = f.read()
API_KEY = SECRET_API
HEADERS = {'Authorization': 'Bearer %s' % API_KEY}

''' Using Yelp API to return top 5 places according to user input. Example: best_in_town('boba', Irvine) '''
def best_in_town(food: str, location: str):
    dict_of_businesses = {}
    url = 'https://api.yelp.com/v3/businesses/search'
    params = {'term': food,
            'location': location, 
            'sort_by': 'rating',
            'limit': 5}
    req = requests.get(url, params=params, headers=HEADERS)
    parsed = json.loads(req.text)
    businesses = parsed["businesses"]

    for business in businesses:
        dict_of_businesses.update({business["name"]: business["rating"]})
    return dict_of_businesses
