import requests

print(requests.__version__)

# r = requests.get('https://www.google.ca')
r = requests.get('https://github.com/jalqueza/404lab1/blob/master/lab1.py')

print(r.text)
