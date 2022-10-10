
import requests

response = requests.get("http://127.0.0.1:5000/books")

if response.status_code != 200:
    print("Invalid request with status code:", response.status_code)
    exit(-1)

books = response.json()
print(type(books))
print(books)
