

import requests


url = "http://127.0.0.1:5000/books"

resp= requests.get(url)

if resp.status_code != 200:
    print("Request failed with status code:", resp.status_code)
    exit(1)

books = resp.json()
for isbn in books.keys():
    print(isbn)


