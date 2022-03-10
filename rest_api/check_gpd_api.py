import requests
url = 'http://127.0.0.1:5000/Name/'
response = requests.get(url=url)
print(response.text)
