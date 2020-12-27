import requests
import configparser

from API_Automation_Using_Python.PayLoad import addBookPayLoad
from util import configurations
from util.resources import ApiResources

url = configurations.getConfig()['API']['endpoint'] + ApiResources.addBook
headers = {"content-type": "application/json"}
addBook_response = requests.post(url,
                                 json=addBookPayLoad()
                                 , headers=headers, )

print(addBook_response.json())
resp = addBook_response.json()
bookId = resp['Id']

deleteUrl = configurations.getConfig()['API']['endpoint'] + ApiResources.deleteBook
deleteHeaders = {"content-type": "application/json"}
resp_deleteBook = requests.post(deleteUrl, json={
    "ID": bookId
}, headers=deleteHeaders, )

assert resp_deleteBook.status_code == 200
resp_json = resp_deleteBook.json()
# add assert statements
