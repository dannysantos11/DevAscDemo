import requests

base_url = "https://swapi.info/api/"
# Finding Leia Organa
endpoint = "people/5/"

# Response object
response = requests.get(base_url + endpoint)
data = response.json()
print(data)


