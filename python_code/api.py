from urllib import request


import requests

url = 'http://export.arxiv.org/api/query?search_query=ti:supernova&sortBy=lastUpdatedDate&sortOrder=ascending'
html = requests.get(url)
a = html.text
print(a)
html.content
html.status_code

