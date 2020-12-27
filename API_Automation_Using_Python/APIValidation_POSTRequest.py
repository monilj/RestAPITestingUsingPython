import requests

from API_Automation_Using_Python.PayLoad import addBookPayLoad

addBook_response = requests.post('http://216.10.245.166/Library/AddBook.php', json=addBookPayLoad()
                                 , headers={"content-type": "application/json"}, )

print(addBook_response.json())
resp = addBook_response.json()
bookId = resp['Id']

resp_deleteBook = requests.post('http://216.10.245.166/Library/DeleteBook.php', json={
    "ID": bookId
}, headers={"content-type": "application/json"}, )

assert resp_deleteBook.status_code == 200
resp_json = resp_deleteBook.json()
# add assert statements
