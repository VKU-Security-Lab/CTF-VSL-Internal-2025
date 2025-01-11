from faker import Faker
from requests import post

fake = Faker()
url = "http://localhost:8080/article/add"
for i in range(100):
    title = fake.text()
    content = fake.text()
    data = {
        'title': title,
        'content': content,
        'author': fake.user_name()
    }
    r = post(url, data=data, proxies={'http': 'http://localhost:8888'})
    print(r.status_code)