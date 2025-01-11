from requests import get, post

# print(get("http://localhost:1337", proxies={"http": "http://localhost:8888", "https": "http://localhost:8888"}).text)
print(post("http://localhost:1337/recover", data={"username": "admin", "question": "flag", "answer": "flag"}, headers={"Content-Type": "application/x-www-form-urlencoded"}, proxies={"http": "http://localhost:8888", "https": "http://localhost:8888"}).text)