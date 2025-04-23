import requests

r = requests.get('https://api.github.com/events')
res = r.text
print(res)