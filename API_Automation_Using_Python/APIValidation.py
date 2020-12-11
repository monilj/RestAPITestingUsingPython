import json

import requests

response = requests.get(' http://216.10.245.166/Library/GetBook.php',
                        params={'AuthorName': 'Rahul Shetty2'}, )
# print(response)
# print(response.text)
# dict_response = json.loads(response.text)
json_response = response.json()
print(json_response)
print(response.status_code)
assert response.status_code == 200
print(response.headers)
assert response.headers['content-type'] == 'application/json;charset=UTF-8'

# Retrieve the book details with ISBN abc123xyz1
print("=====  Retrieve the book details with ISBN abc123xyz1 =====")
for det in json_response:
    if det['isbn'] == 'abc123xyz1':
        print(det['book_name'])
        print(det['aisle'])
    if det['isbn'] == 'PSRS':
        print(det['book_name'])
        print(det['aisle'])
