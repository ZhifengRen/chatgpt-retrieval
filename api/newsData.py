import requests

url = ('https://newsapi.org/v2/everything?'
       'q=statestreet&'
       'from=2023-09-08&'
       'sortBy=popularity&'
       'apiKey=fb12fb5253154c66b8bbe1da83d30139')

response = requests.get(url)

print (response.json())