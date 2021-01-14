import requests

print(requests.__version__)

r = requests.get('https://www.google.ca')

print(r.text)