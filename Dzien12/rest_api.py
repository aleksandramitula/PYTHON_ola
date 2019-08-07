## http://www.recipepuppy.com/about/api/

import requests

response = requests.get('http://www.recipepuppy.com/api/',params = {'i': 'onions,garlic', 'q': 'omelet', 'p':'1'})

#onions,garlic


print(response.status_code)
recipes = response.json()['results']

for recipe in recipes:
    print()             # end of line (can be also e.g. "\n")
    print(recipe['title'])
    print(recipe['ingredients'])
    print(recipe['thumbnail'])