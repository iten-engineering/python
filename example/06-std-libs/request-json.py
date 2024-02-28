import requests

url = "http://jsonplaceholder.typicode.com/posts"

proxies = {
    "http" : "http://prp04.admin.ch:8080",
    "https": "http://prp04.admin.ch:8080"
}

try:
    # get request to the url
    response = requests.get(url, proxies=proxies)

    # check response status code
    if response.status_code ==200:
        posts = response.json()
    else:
        raise Exception(f"Request failed with status code: {response.status_code}")

    # show response
    print("Show first post:")
    print(posts[0])

    print("\nShow userId and title of all posts:")
    for p in posts:
        print(p["userId"], ":", p["title"])
    print(f"Total {len(posts)} posts received.")

except Exception as e:
    print(f"Request failed with exception:", e)
