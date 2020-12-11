import json

import requests

response = requests.get(' http://216.10.245.166/Library/GetBook.php',
                        params={'AuthorName': 'Rahul Shetty2'}, )
# print(response)
# print(response.text)
# dict_response = json.loads(response.text)
json_response = response.json()
print(json_response)